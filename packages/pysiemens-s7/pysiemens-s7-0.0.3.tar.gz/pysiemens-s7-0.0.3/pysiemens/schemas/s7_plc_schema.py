from typing import List, Optional, Union

from pydantic import BaseModel
from pydantic.networks import IPv4Address


from .s7_data_schema import (
    S7Boolean,
    S7Char,
    S7DInt,
    S7DWord,
    S7Int,
    S7LInt,
    S7LReal,
    S7LTime,
    S7LWord,
    S7Real,
    S7S5Time,
    S7SmallInt,
    S7Time,
    S7UnsignedDInt,
    S7UnsignedInt,
    S7UnsignedLInt,
    S7UnsignedSmallInt,
    S7WChar,
    S7Word,
)


class PLCSchemaConnection(BaseModel):
    plc_name: str = "nameNotSet"
    ip_address: IPv4Address
    rack: int = 0
    slot: int = 1
    port: int = 102
    cycle_time: int = 5000


class PLCSchema(PLCSchemaConnection):
    variables: Optional[
        List[
            Union[
                S7Boolean,
                S7SmallInt,
                S7UnsignedSmallInt,
                S7Int,
                S7UnsignedInt,
                S7DInt,
                S7UnsignedDInt,
                S7LInt,
                S7UnsignedLInt,
                S7Real,
                S7LReal,
                S7S5Time,
                S7Time,
                S7LTime,
                S7Char,
                S7WChar,
                S7Word,
                S7DWord,
                S7LWord,
            ]
        ]
    ] = None
