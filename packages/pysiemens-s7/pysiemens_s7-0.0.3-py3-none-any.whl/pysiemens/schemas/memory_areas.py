"""
PLC memory area types
"""

from typing import List

__all__ = ("MARK", "DATA_BLOCK", "INPUT", "OUTPUT")

MARK = "M"
DATA_BLOCK = "DB"
INPUT = "E"
OUTPUT = "A"


def __dir__() -> List[str]:
    return sorted(list(__all__))
