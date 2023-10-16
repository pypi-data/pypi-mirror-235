import logging
import math
from typing import Union

import torch
import torchaudio
from torch import nn

from audio_denoiser.helpers.torch_helper import batched_apply
from audio_denoiser.modules.AudioDenosingAutoencoder import AudioDenoisingAutoencoder
from audio_denoiser.helpers.audio_helper import create_spectrogram, reconstruct_from_spectrogram


class AudioDenoiser:
    def __init__(self, model_name='jose-h-solorzano/audio-denoiser-512-32-v1',
                 device: Union[str, torch.device] = None, num_iterations: int = 100):
        super().__init__()
        if device is None:
            is_cuda = torch.cuda.is_available()
            if not is_cuda:
                logging.warning('CUDA not available. Will use CPU.')
            device = torch.device('cuda:0') if is_cuda else torch.device('cpu')
        self.device = device
        self.model = AudioDenoisingAutoencoder.from_pretrained(model_name).to(device)
        self.model_sample_rate = self.model.sample_rate
        self.scaler = self.model.scaler
        self.n_fft = self.model.n_fft
        self.segment_num_frames = self.model.num_frames
        self.num_iterations = num_iterations

    @staticmethod
    def _sp_log(spectrogram: torch.Tensor, eps=0.01):
        return torch.log(spectrogram + eps)

    @staticmethod
    def _sp_exp(log_spectrogram: torch.Tensor, eps=0.01):
        return torch.clamp(torch.exp(log_spectrogram) - eps, min=0)

    def process_waveform(self, waveform: torch.Tensor, sample_rate: int) -> torch.Tensor:
        if sample_rate != self.model_sample_rate:
            transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=self.model_sample_rate)
            waveform = transform(waveform)
        hop_len = self.n_fft // 2
        spectrogram = create_spectrogram(waveform, n_fft=self.n_fft, hop_length=hop_len)
        spectrogram = spectrogram.to(self.device)
        num_a_channels = spectrogram.size(0)
        with torch.no_grad():
            results = []
            for c in range(num_a_channels):
                c_spectrogram = spectrogram[c]
                # c_spectrogram: (257, num_frames)
                fft_size, num_frames = c_spectrogram.shape
                num_segments = math.ceil(num_frames / self.segment_num_frames)
                adj_num_frames = num_segments * self.segment_num_frames
                if adj_num_frames > num_frames:
                    c_spectrogram = nn.functional.pad(c_spectrogram, (0, adj_num_frames - num_frames))
                c_spectrogram = c_spectrogram.view(fft_size, num_segments, self.segment_num_frames)
                # c_spectrogram: (257, num_segments, 32)
                c_spectrogram = torch.permute(c_spectrogram, (1, 0, 2))
                # c_spectrogram: (num_segments, 257, 32)
                log_c_spectrogram = self._sp_log(c_spectrogram)
                scaled_log_c_sp = self.scaler(log_c_spectrogram)
                log_denoised_sp = batched_apply(self.model, scaled_log_c_sp, detached=True)
                denoised_sp = self._sp_exp(log_denoised_sp)
                # denoised_sp: (num_segments, 257, 32)
                denoised_sp = torch.permute(denoised_sp, (1, 0, 2))
                # denoised_sp: (257, num_segments, 32)
                denoised_sp = denoised_sp.contiguous().view(1, fft_size, adj_num_frames)
                # denoised_sp: (1, 257, adj_num_frames)
                denoised_sp = denoised_sp[:, :, :num_frames]
                denoised_sp = denoised_sp.cpu()
                denoised_waveform = reconstruct_from_spectrogram(denoised_sp, num_iterations=self.num_iterations)
                # denoised_waveform: (1, num_samples)
                results.append(denoised_waveform)
            cpu_results = torch.cat(results)
            return cpu_results.to(self.device)

    def process_audio_file(self, in_audio_file: str, out_audio_file: str):
        waveform, sample_rate = torchaudio.load(in_audio_file)
        denoised_waveform = self.process_waveform(waveform, sample_rate)
        torchaudio.save(out_audio_file, denoised_waveform, sample_rate=self.model_sample_rate)
