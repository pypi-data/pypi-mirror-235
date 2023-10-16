from typing import List

import torch
from torch import nn


class Slicer2d(nn.Module):
    def __init__(self, slice1: slice, slice2: slice):
        super().__init__()
        self.slice2 = slice2
        self.slice1 = slice1

    def forward(self, x: torch.Tensor):
        return x[:, :, self.slice1, self.slice2]
