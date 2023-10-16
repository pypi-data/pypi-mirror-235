"""
Primitive data types on Siemens PLC
"""
from typing import List

__all__ = ("BIT", "BYTE", "WORD", "DWORD", "LWORD")

BIT = 1
BYTE = 8
WORD = 16
DWORD = 32
LWORD = 64


def __dir__() -> List[str]:
    return sorted(list(__all__))
