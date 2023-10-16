import torch
import torch.nn as nn
from utils import generation
from utils import download
from utils import prompt_making
from utils import sentence_cutter
from utils import symbol_table
from utils import g2p
# from icefall.utils import make_pad_mask

from .symbol_table import SymbolTable

# make_pad_mask = make_pad_mask
SymbolTable = SymbolTable


class Transpose(nn.Identity):
    """(N, T, D) -> (N, D, T)"""

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return input.transpose(1, 2)
