"""
    Regex collection to identify variables type
"""

from typing import List

__all__ = (
    "DB_BOOLEAN",
    "DB_BYTE",
    "DB_WORD",
    "DB_DWORD",
    "DB_LWORD",
    "M_BOOLEAN",
    "M_BYTE",
    "M_WORD",
    "M_DWORD",
    "E_BOOLEAN",
    "E_BYTE",
    "E_WORD",
    "E_DWORD",
    "A_BOOLEAN",
    "A_BYTE",
    "A_WORD",
    "A_DWORD",
)

DB_BOOLEAN = "^DB\d+.DBX\d+\.[0-7]$"  # noqa:W605
DB_BYTE = "^DB\d+.DBB\d+$"  # noqa:W605
DB_WORD = "^DB\d+.DBW\d+$"  # noqa:W605
DB_DWORD = "^DB\d+.DBD\d+$"  # noqa:W605
DB_LWORD = "^DB\d+.DBX\d+\.[0-7]$"  # noqa:W605
M_BOOLEAN = "^M\d+\.[0-7]$"  # noqa:W605
M_BYTE = "^MB\d+$"  # noqa:W605
M_WORD = "^MW\d+$"  # noqa:W605
M_DWORD = "^MD\d+$"  # noqa:W605
M_LWORD = "^M\d+\.[0-7]$"  # noqa:W605
E_BOOLEAN = "^E\d+\.[0-7]$|I\d+\.[0-7]$"  # noqa:W605
E_BYTE = "^EB\d+$|IB\d+$"  # noqa:W605
E_WORD = "^EW\d+$|IW\d+$"  # noqa:W605
E_DWORD = "^ED\d+$|ID\d+$"  # noqa:W605
E_LWORD = "^E\d+\.[0-7]$|E\d+\.[0-7]$"  # noqa:W605
A_BOOLEAN = "^A\d+\.[0-7]$|Q\d+\.[0-7]$"  # noqa:W605
A_BYTE = "^AB\d+$|QB\d+$"  # noqa:W605
A_WORD = "^AW\d+$|QW\d+$"  # noqa:W605
A_DWORD = "^AD\d+$|QD\d+$"  # noqa:W605
A_LWORD = "^A\d+\.[0-7]$|Q\d+\.[0-7]$"  # noqa:W605


def __dir__() -> List[str]:
    return sorted(list(__all__))
