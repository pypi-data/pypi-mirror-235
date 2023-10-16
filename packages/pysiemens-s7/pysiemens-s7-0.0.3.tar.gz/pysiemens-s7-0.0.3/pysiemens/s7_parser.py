from pysiemens import utils

from pysiemens.address_patterns import (
    A_BOOLEAN,
    A_DWORD,
    A_WORD,
    A_LWORD,
    DB_BOOLEAN,
    DB_BYTE,
    DB_DWORD,
    DB_LWORD,
    DB_WORD,
    E_BOOLEAN,
    E_DWORD,
    E_LWORD,
    E_WORD,
    M_BOOLEAN,
    M_BYTE,
    M_DWORD,
    M_LWORD,
    M_WORD,
)
from typing import Union
from pysiemens.errors import S7ParsingError, S7DataParsingError
from pysiemens.schemas.memory_areas import DATA_BLOCK, INPUT, MARK, OUTPUT
from pysiemens.schemas.s7_data_schema import (
    VariableBase,
    S7Boolean,
    S7DInt,
    S7DWord,
    S7Int,
    S7Real,
    S7SmallInt,
    S7UnsignedSmallInt,
    S7Word,
    S7LReal,
)
from snap7.util import (
    get_bool,
    set_bool,
    get_int,
    set_int,
    get_dint,
    set_dint,
    get_real,
    set_real,
    get_byte,
    set_byte,
    get_sint,
    set_sint,
)


class AddressParser:
    """Class to parse plc addresses from siemens typing style to S7XXtype to perform actions with snap7 library"""

    def __init__(self) -> None:
        self._internal_byte_patterns = {
            DB_BYTE: DATA_BLOCK,
            M_BYTE: MARK,
        }

        self._internal_word_patterns = {
            DB_WORD: DATA_BLOCK,
            M_WORD: MARK,
        }
        self._internal_dword_patterns = {
            DB_DWORD: DATA_BLOCK,
            M_DWORD: MARK,
        }

        self._word_patterns = {
            DB_WORD: DATA_BLOCK,
            M_WORD: MARK,
            E_WORD: INPUT,
            A_WORD: OUTPUT,
        }

        self._dword_patterns = {
            DB_DWORD: DATA_BLOCK,
            M_DWORD: MARK,
            E_DWORD: INPUT,
            A_DWORD: OUTPUT,
        }

        self._lword_patterns = {
            DB_LWORD: DATA_BLOCK,
            M_LWORD: MARK,
            E_LWORD: INPUT,
            A_LWORD: OUTPUT,
        }
        self._bool_patterns = {
            DB_BOOLEAN: DATA_BLOCK,
            E_BOOLEAN: INPUT,
            A_BOOLEAN: OUTPUT,
            M_BOOLEAN: MARK,
        }

    def parse_usint(self, name: str, address: str) -> S7UnsignedSmallInt:
        """Parses address to Unsigned Small Integer type

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7UnsignedSmallInt: Specific address type
        """
        type = "USINT"
        db_num = None

        mem_area = utils.get_type(self._internal_byte_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7UnsignedSmallInt(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_sint(self, name: str, address: str) -> S7SmallInt:
        """Parses address to Small Integer type

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7SmallInt: Specific address type
        """
        type = "SINT"
        db_num = None

        mem_area = utils.get_type(self._internal_byte_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7SmallInt(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_word(self, name: str, address: str) -> S7Word:
        """Parses a word type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7Word: Pydantic class for the datatype
        """
        type = "WORD"
        db_num = None

        mem_area = utils.get_type(self._word_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7Word(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_int(self, name: str, address: str) -> S7Int:
        """Parses an Integer type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7Int: Pydantic class for the datatype
        """
        type = "INT"
        mem_area = utils.get_type(self._internal_word_patterns, address)
        db_num = None
        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)

        else:
            raise S7ParsingError(variable=address, type=type)

        return S7Int(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_dword(self, name: str, address: str) -> S7DWord:
        """Parses an Double Word type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7DWord: Pydantic class for the datatype
        """
        type = "DWORD"
        db_num = None

        mem_area = utils.get_type(self._dword_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7DWord(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_dint(self, name: str, address: str) -> S7DInt:
        """Parses an Double Int type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7DInt: Pydantic class for the datatype
        """
        type = "DINT"
        db_num = None

        mem_area = utils.get_type(self._internal_dword_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7DInt(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_real(self, name: str, address: str) -> S7Real:
        """Parses a Real type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7Real: Pydantic class for the datatype
        """
        type = "REAL"
        db_num = None

        mem_area = utils.get_type(self._internal_dword_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7Real(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_lreal(self, name: str, address: str) -> S7LReal:
        """Parses a Long Real type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7LReal: Pydantic class for the datatype
        """
        type = "LREAL"
        db_num = None

        mem_area = utils.get_type(self._lword_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address, True)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7LReal(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
        )

    def parse_bool(self, name: str, address: str) -> S7Boolean:
        """Parses a Boolean type variable

        Args:
            name (str): Variable name
            address (str): Absolute PLC address

        Raises:
            S7ParsingError: If the provided variable and type are not parseable

        Returns:
            S7Boolean: Pydantic class for the datatype
        """
        type = "BOOL"
        db_num = None

        mem_area = utils.get_type(self._bool_patterns, address)

        if mem_area:
            start_byte = utils.get_start_byte(address, True)
            bit = utils.get_bit(address)
            if mem_area == "DB":
                db_num = utils.get_db_number(address)
        else:
            raise S7ParsingError(variable=address, type=type)

        return S7Boolean(
            name=name,
            address=address,
            type=type,
            mem_area=mem_area,
            db_num=db_num,
            start_byte=start_byte,
            bit_position=bit,
        )

    def parse_address(self, *, name: str, address: str, var_type: str) -> VariableBase:
        """Parses provided address to a S7 format by its type and plc address to the memory type

        Args:
            name (str): Address name
            address (str): PLC absolute adress
            var_type (str): variable type

        Returns:
            parsed_var: Parsed address
        """
        dir_parsers = {
            "INT": self.parse_int,
            "DINT": self.parse_dint,
            "WORD": self.parse_word,
            "REAL": self.parse_real,
            "DWORD": self.parse_dword,
            "BOOL": self.parse_bool,
            "SINT": self.parse_sint,
            "USINT": self.parse_usint,
            "LREAL": self.parse_lreal,
        }

        if (
            not var_type.upper() in dir_parsers
        ):  # Raise error if type is not implemented on parsing
            raise ValueError(f"{var_type} not yet implemented")

        return dir_parsers.get(var_type.upper())(name, address)


class DataParser:
    def bytes_to_human(self, variable: VariableBase) -> VariableBase:
        """Parses data from bytearray to human readable data format

        Args:
            variable (VariableBase): variable to parse

        Returns:
            VariableBase: variable with its data parsed
        """
        byte_to_human = {
            "INT": get_int,
            "REAL": get_real,
            "BYTE": get_byte,
            "SINT": get_sint,
            "DINT": get_dint,
            "BOOL": get_bool,
        }

        if isinstance(variable, S7Boolean):
            data = byte_to_human.get(variable.type)(
                variable.value, 0, 7 - variable.bit_position
            )
        else:
            data = byte_to_human.get(variable.type)(variable.value, 0)

        variable.value = data

        return variable.value

    def human_to_bytes(self, variable: VariableBase) -> VariableBase:
        """Parses a variable from human readable to byte array snap7 format

        Args:
            variable (VariableBase): A pydantic variable instance of variable

        Returns:
            VariableBase: variable with bytearray value for the variable
        """
        human_to_byte = {
            "INT": set_int,
            "REAL": set_real,
            "BYTE": set_byte,
            "SINT": set_sint,
            "DINT": set_dint,
            "BOOL": set_bool,
        }
        data_types = {
            "INT": int,
            "REAL": float,
            "BYTE": Union[int, str],
            "SINT": int,
            "DINT": int,
            "BOOL": bool,
        }
        if not isinstance(variable.value, data_types.get(variable.type)):
            raise S7DataParsingError("Bool", f"{variable.value}")

        buffer = bytearray(variable.byte_size)
        if isinstance(variable, S7Boolean):
            human_to_byte.get(variable.type)(
                buffer, 0, 7 - variable.bit_position, variable.value
            )

        else:
            human_to_byte.get(variable.type)(buffer, 0, variable.value)

        variable.value = buffer
        return variable
