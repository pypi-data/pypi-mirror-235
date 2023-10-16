import re
from typing import Dict, Optional


def check_start_address(address: str, pattern: str) -> bool:
    if re.search(pattern, address, re.IGNORECASE):
        return True
    else:
        return False


def get_db_start_byte(db_address: str) -> int:
    return db_address.split(".")[1][3:]


def is_db_address(address: str) -> bool:
    return True if address[0:2] == "DB" else False


def get_type(patterns: Dict[str, str], address: str) -> Optional[str]:
    for pattern in patterns.keys():
        if check_start_address(address, pattern):
            return patterns.get(pattern)
    return None


def get_bit(address: str) -> int:
    return address[-1:]


def get_start_byte(address: str, is_bool_patt: bool = False) -> str:
    if is_db_address(address):
        return get_db_start_byte(address)
    else:
        return address.split(".")[0][1:] if is_bool_patt else address[2:]


def get_db_number(address: str) -> int:
    return int(address.split(".")[0][2:])
