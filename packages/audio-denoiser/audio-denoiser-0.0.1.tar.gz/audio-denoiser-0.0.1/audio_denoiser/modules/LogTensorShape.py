import logging
from typing import List

import torch
from torch import nn


class LogTensorShape(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor):
        logging.warning(f'Tensor of shape {x.shape}')
        return x
