import torch
import torchaudio.transforms as T


def create_spectrogram(waveform: torch.Tensor, n_fft: int, hop_length: int = None):
    if hop_length is None:
        hop_length = n_fft // 2
    spectrogram_transform = T.Spectrogram(n_fft=n_fft, win_length=n_fft, hop_length=hop_length)
    spectrogram = spectrogram_transform(waveform)
    return spectrogram


def reconstruct_from_spectrogram(spectrogram: torch.Tensor, num_iterations=100):
    _, half_fft, _ = spectrogram.shape
    n_fft = (half_fft - 1) * 2
    transform = T.GriffinLim(n_fft=n_fft, n_iter=num_iterations, rand_init=False)
    return transform(spectrogram)
