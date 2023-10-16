"""PyS7 Custom errors"""


class S7Error(Exception):
    """Base S7Exception"""

    def __init__(self, message: str, *args) -> None:
        """Initialize the exception

        Args:
            string (str): The message to appendo to error
        """
        super().__init__(args)
        self.string = message

    def __str__(self) -> str:
        """Return string representation."""
        return f"S7Error: {self.string}"


class S7ParsingError(S7Error):
    def __init__(self, variable: str, type: str, *args) -> None:
        """PLC Variable parsing error

        Args:
            variable (str): Variable address that could not be parsed
        """
        message = f"Invalid address provided. Can not parse {variable.upper()} to a valid {type.upper()}"
        super().__init__(message, *args)


class S7ConnectionError(S7Error):
    def __init__(self, conn_name: str, *args) -> None:
        """PLC Connection error

        Args:
            conn_name (str): The name of the plc which tries to connect
        """

        message = f"PLC '{conn_name}' not connected"
        super().__init__(message, *args)


class S7DataParsingError(S7Error):
    def __init__(self, var_type: str, value: str, *args) -> None:
        """PLC Variable data parsing error

        Args:
            var_type (str): Variable type
            value (str): Variable value
        """
        message = f"Can not parse {value} to a valid {var_type}"
        super().__init__(message, *args)


class S7VariableNotDeclared(S7Error):
    def __init__(self, address: str, *args) -> None:
        """Variable not declared on the PLC Client object

        Args:
            address (str): plc absolute address
        """
        message = f"Address {address} not declared on the PLC"
        super().__init__(message, *args)


class S7VariableType(S7Error):
    def __init__(self, type: str, value: str, *args) -> None:
        """Provided wrong type value for S7 variable

        Args:
            message (str): _description_
        """
        message = f"Value {value} is not a valid type for variable of type {type}"
        super().__init__(message, *args)
