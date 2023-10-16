import torch
import torch.nn as nn
from vall.utils import generation
from vall.utils import download
from vall.utils import prompt_making
from vall.utils import sentence_cutter
from vall.utils import symbol_table
from vall.utils import g2p
# from icefall.utils import make_pad_mask

from .symbol_table import SymbolTable

# make_pad_mask = make_pad_mask
SymbolTable = SymbolTable


class Transpose(nn.Identity):
    """(N, T, D) -> (N, D, T)"""

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return input.transpose(1, 2)
