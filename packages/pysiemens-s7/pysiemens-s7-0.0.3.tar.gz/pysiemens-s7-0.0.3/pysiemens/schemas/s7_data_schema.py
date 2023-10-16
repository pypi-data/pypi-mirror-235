from typing import Annotated, Optional, Any

from pydantic import BaseModel, Field, computed_field, constr

from .primitive import BIT, BYTE, DWORD, LWORD, WORD

# Base variable


class UnsettedVariable(BaseModel):
    name: str
    type: str
    address: str


class VariableBase(BaseModel):
    name: constr(strip_whitespace=True)
    address: constr(to_upper=True)
    type: constr(to_upper=True)
    mem_area: constr(to_upper=True)
    db_num: Optional[int] = None
    start_byte: int
    bit_size: int
    value: Optional[Any] = None

    @computed_field
    @property
    def byte_size(self) -> int:
        if self.bit_size % BYTE == 0:
            return self.bit_size // BYTE
        else:
            return 1


# Boolean


class S7Boolean(VariableBase):
    bit_size: int = BIT
    bit_position: Annotated[int, Field(le=7, ge=0)]
    value: bool = None


# Small Integers


class S7SmallInt(VariableBase):
    bit_size: int = BYTE
    value: Optional[int] = None


class S7UnsignedSmallInt(VariableBase):
    bit_size: int = BYTE
    value: Optional[int] = None


# Integers


class S7Int(VariableBase):
    bit_size: int = WORD
    value: Optional[int] = None


class S7UnsignedInt(VariableBase):
    bit_size: int = WORD
    value: Optional[int] = None


# Double Integers


class S7DInt(VariableBase):
    bit_size: int = DWORD
    value: Optional[int] = None


class S7UnsignedDInt(VariableBase):
    bit_size: int = DWORD
    value: Optional[int] = None


# Long Integers


class S7LInt(VariableBase):
    bit_size: int = LWORD
    value: Optional[int] = None


class S7UnsignedLInt(VariableBase):
    bit_size: int = LWORD
    value: Optional[int] = None


# Floats


class S7Real(VariableBase):
    bit_size: int = DWORD
    value: Optional[float] = None


class S7LReal(VariableBase):
    bit_size: int = LWORD
    value: Optional[float] = None


# Temps


class S7S5Time(VariableBase):
    bit_size: int = WORD
    value: Optional[str] = None


class S7Time(VariableBase):
    bit_size: int = DWORD
    value: Optional[str] = None


class S7LTime(VariableBase):
    bit_size: int = LWORD
    value: Optional[str] = None


# Strings


class S7Char(VariableBase):
    bit_size: int = BYTE
    value: Optional[str] = None


class S7WChar(VariableBase):
    bit_size: int = WORD
    value: Optional[str] = None


# Binary data


class S7Word(VariableBase):
    bit_size: int = WORD
    value: Optional[str] = None


class S7DWord(VariableBase):
    bit_size: int = DWORD
    value: Optional[str] = None


class S7LWord(VariableBase):
    bit_size: int = LWORD
    value: Optional[str] = None
