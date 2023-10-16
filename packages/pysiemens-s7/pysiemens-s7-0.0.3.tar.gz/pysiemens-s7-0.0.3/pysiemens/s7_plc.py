from typing import Any, Dict, List, Union, Optional

from pydantic import TypeAdapter
from snap7.client import Client

from pysiemens.s7_parser import AddressParser, DataParser
from pysiemens.schemas.s7_data_schema import UnsettedVariable, VariableBase
from pysiemens.schemas.s7_plc_schema import PLCSchema, PLCSchemaConnection
from pysiemens.errors import S7VariableNotDeclared


class PLCClient(Client):
    """Client object for PLC

    Args:
        Client (snap7.Client): Abstracts snap7 wrapper class and adds automatic variable parsing
    """

    def __init__(self, plc_data: Union[PLCSchemaConnection, Dict[str, Any]]) -> None:
        """Creates a new 'PLCClient' instance.

        Args:
            plc_data (Union[PLCSchemaConnection, Dict[str, Any]]): An instance of PLCSchemaConnection or
            a dict with PLC Connection parameters

        Examples:
            # Using a dict
            >>> from pysiemens.s7_plc import PLCClient
            >>> plc=PLCClient({
                    "plc_name":"foo_plc" #optional, default is sysNotSet
                    "ip_address":192.168.1.1,
                    "rack": 0, # optional, default 0
                    "slot": 1, # optional, default 1
                    "port": 102 # optional, default 102
                    "cycle_time": 5000 # cycle time in milliseconds, default 5000
                })
            >>> plc
            <pysiemens.s7_plc.PLCClient object at 0x106caa650>
        """

        super().__init__()
        if isinstance(plc_data, dict):
            self._params = PLCSchema(**plc_data)
        else:
            self._params = PLCSchema(**plc_data.model_dump())

    @property
    def params(self) -> PLCSchema:
        """PLC Parameters

        Returns:
            PLCSchema: Returns a pydantic schema with all the PLC Parameters
        """
        return self._params

    @property
    def variables(self) -> Optional[List[VariableBase]]:
        """PLC Variables

        Returns:
            Optional[List[VariableBase]]: Returns a list with all the variables parsed, if any
        """
        return self._params.variables

    def _find_declared_var(self, address: str) -> VariableBase:
        for var in self._params.variables:
            if var.address == address:
                return var

        raise S7VariableNotDeclared(address=address)

    def declare_variables(
        self, *variables: Union[UnsettedVariable, Dict[str, str]]
    ) -> None:
        """Parses a list of `siemens-like` addresses and adds them to the client object
        Examples:
            >>> from pysiemens.s7_plc import PLCClient
            >>> plc=PLCClient({
                    "plc_name":"foo_plc" #optional, default is sysNotSet
                    "ip_address":192.168.1.1,
                    "rack": 0, # optional, default 0
                    "slot": 1, # optional, default 1
                    "port": 102 # optional, default 102
                    "cycle_time": 5000 # cycle time in milliseconds, default 5000
                })
                # Declaration of a Data Block int
            >>> plc.declare_variables({"name":"foo","type":"int","address":"DB4.DBW10"})
                # As it is an object we can populate parametes with its atribute `params`
            >>> print(plc.params)
            >>> plc_name='foo_plc',
                ip_address=IPv4Address('192.168.1.1'),
                rack=0,
                slot=1,
                port=102,
                cycle_time=5000,
                variables=[S7Int(
                    name='foo',
                    address='DB4.DBW10',
                    type='INT',
                    mem_area='DB',
                    db_num=4,
                    start_byte=10,
                    bit_size=16,
                    value=None,
                    byte_size=2
                    )]

        """
        unsetted_vars = TypeAdapter(List[UnsettedVariable]).validate_python(variables)

        setted_vars: List[Any] = []

        parser = AddressParser()

        for unset_var in unsetted_vars:
            setted_vars.append(
                parser.parse_address(
                    name=unset_var.name,
                    address=unset_var.address,
                    var_type=unset_var.type,
                )
            )
        self._params.variables = setted_vars

    def connect(self) -> int:
        """Attempts to connect to the configured PLC

        Returns:
            int: snap7 connection code
        """
        return super().connect(
            address=str(self._params.ip_address),
            rack=self._params.rack,
            slot=self._params.slot,
            tcpport=self._params.port,
        )

    def set_variable_value(
        self, variable: Union[str, VariableBase], value: Any
    ) -> None:
        """Changes the value of a provided variable

        Args:
            variable (Union[str, VariableBase]): Variable to update
            value (Any): Value to set
        """
        if not isinstance(variable, VariableBase):
            variable = self._find_declared_var(variable)

        variable.value = value

    def set_mulit_var_value(self, variables: List[Union[str, VariableBase]]) -> None:
        # TODO needs the values to be setted
        for variable in variables:
            self.set_variable_value(variable)

    def read_multi_from_plc(self) -> List[VariableBase]:
        """Reads the actual values of the PLCClient configured variables

        Returns:
            List[VariableBase]: Updated variables list
        """
        read_mem = {
            "DB": super().db_read,
            "M": super().mb_read,
            "E": super().eb_read,
            "I": super().eb_read,
            "A": super().ab_read,
            "Q": super().ab_read,
        }

        parser = DataParser()
        for var in self._params.variables:
            if var.mem_area == "DB":
                var.value = read_mem.get(var.mem_area)(
                    var.db_num, var.start_byte, var.byte_size
                )
            else:
                var.value = read_mem.get(var.mem_area)(var.start_byte, var.byte_size)

            var = parser.bytes_to_human(var)

        return self._params.variables

    def write_multi_to_plc(self, variables: List[VariableBase]) -> List[VariableBase]:
        write_area = {
            "DB": super().db_write,
            "M": super().mb_write,
            "E": super().eb_write,
            "I": super().eb_write,
            "A": super().ab_write,
            "Q": super().ab_write,
        }

        parser = DataParser()
        for var in variables:
            parser.human_to_bytes(var)
            if var.mem_area == "DB":
                write_area.get(var.mem_area)(var.db_num, var.start_byte, var.value)
