import pytest
from pydantic_core import ValidationError

from pysiemens.s7_plc import PLCClient

from . import utils
from typing import Generator


class TestPLCClient:
    @pytest.fixture(scope="class", autouse=True)
    def test_create_client_correct(self) -> None:
        rand_plc = {
            "ip_address": utils.random_v4ip(),
            "rack": utils.random_int(max=5),
            "slot": utils.random_int(max=5),
            "port": 102,
        }
        plc = PLCClient(rand_plc)

        assert str(plc.params.ip_address) == rand_plc["ip_address"]
        assert plc.params.rack == int(rand_plc["rack"])
        assert plc.params.slot == int(rand_plc["slot"])

    def test_create_client_wrong_ip(self) -> None:
        plc = {
            "ip_address": "2,5,7,8",
            "rack": utils.random_int(max=5),
            "slot": utils.random_int(max=5),
        }
        with pytest.raises(ValidationError):
            PLCClient(plc_data=plc)
        plc.update({"ip_address": "20.21.260.3"})
        with pytest.raises(ValidationError):
            PLCClient(plc_data=plc)

    def test_create_client_wrong_rack(self) -> None:
        rand_plc = {
            "ip_address": utils.random_v4ip(),
            "rack": "s",
            "slot": utils.random_int(max=5),
        }
        with pytest.raises(ValidationError):
            PLCClient(plc_data=rand_plc)

    def test_create_client_wrong_slot(self) -> None:
        rand_plc = {
            "ip_address": utils.random_v4ip(),
            "rack": utils.random_int(max=5),
            "slot": "s",
        }
        with pytest.raises(ValidationError):
            PLCClient(plc_data=rand_plc)

    @pytest.mark.xfail(raises=RuntimeError)
    def test_connect_to_server(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.connect()
        assert plc.get_connected() is True
        plc.disconnect()

    @pytest.mark.xfail(raises=RuntimeError)
    def test_read_db_int(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_DB_floor_int", "type": "int", "address": "DB0.DBW30"},
        )
        plc.connect()
        plc.read_multi_from_plc()
        assert isinstance(plc.params.variables[0].value, int)
        plc.disconnect()

    @pytest.mark.xfail(raises=RuntimeError)
    def test_read_db_float(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_DB_floor_float", "type": "real", "address": "DB0.DBD60"},
        )
        plc.connect()
        plc.read_multi_from_plc()

        assert isinstance(plc.params.variables[0].value, float)
        plc.disconnect()

    @pytest.mark.xfail(raises=RuntimeError)
    def test_read_db_bool(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_DB_bool_0", "type": "bool", "address": "DB0.DBX0.0"},
            {"name": "Test_DB_bool_1", "type": "bool", "address": "DB0.DBX0.1"},
            {"name": "Test_DB_bool_2", "type": "bool", "address": "DB0.DBX0.2"},
            {"name": "Test_DB_bool_3", "type": "bool", "address": "DB0.DBX0.3"},
            {"name": "Test_DB_bool_4", "type": "bool", "address": "DB0.DBX0.4"},
            {"name": "Test_DB_bool_5", "type": "bool", "address": "DB0.DBX0.5"},
            {"name": "Test_DB_bool_6", "type": "bool", "address": "DB0.DBX0.6"},
            {"name": "Test_DB_bool_7", "type": "bool", "address": "DB0.DBX0.7"},
        )
        plc.connect()

        plc.read_multi_from_plc()
        for index, variable in enumerate(plc.variables):
            assert isinstance(variable.value, bool)
            if index % 2 != 0:
                assert variable.value is False
            else:
                assert variable.value is True
        plc.disconnect()

    @pytest.mark.skip("!WIP Check correct bool index in cpu")
    @pytest.mark.xfail(raises=RuntimeError)
    def test_write_db_bool(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_DB_bool_0", "type": "bool", "address": "DB0.DBX0.0"},
            {"name": "Test_DB_bool_1", "type": "bool", "address": "DB0.DBX0.1"},
            {"name": "Test_DB_bool_2", "type": "bool", "address": "DB0.DBX0.2"},
            {"name": "Test_DB_bool_3", "type": "bool", "address": "DB0.DBX0.3"},
            {"name": "Test_DB_bool_4", "type": "bool", "address": "DB0.DBX0.4"},
            {"name": "Test_DB_bool_5", "type": "bool", "address": "DB0.DBX0.5"},
            {"name": "Test_DB_bool_6", "type": "bool", "address": "DB0.DBX0.6"},
            {"name": "Test_DB_bool_7", "type": "bool", "address": "DB0.DBX0.7"},
        )
        plc.connect()

        for indx, var in enumerate(plc.variables):
            var_value = False if indx < 4 else True
            plc.set_variable_value(var, var_value)

        plc.write_multi_to_plc(plc.variables)

        plc.disconnect()

    @pytest.mark.xfail(raises=RuntimeError)
    def test_write_db_int(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_DB_floor_int", "type": "int", "address": "DB0.DBW30"},
        )
        plc.connect()

        plc.set_variable_value(plc.variables[0], 15)
        plc.write_multi_to_plc(plc.variables)

        plc.disconnect()

    @pytest.mark.skip("TODO test marks not available on fake server")
    @pytest.mark.xfail(raises=RuntimeError)
    def test_write_m_bool(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_M_bool_0", "type": "bool", "address": "M0.0"},
            {"name": "Test_M_bool_1", "type": "bool", "address": "M0.1"},
        )

        plc.connect()
        import pdb

        pdb.set_trace()
        plc.set_variable_value(plc.variables[0], True)
        plc.set_variable_value(plc.variables[1], False)
        plc.write_multi_to_plc(plc.variables)

        plc.read_multi_from_plc()

        plc.disconnect()

    @pytest.mark.skip("TODO test marks not available on fake server")
    @pytest.mark.xfail(raises=RuntimeError)
    def test_write_m_int(self, plc: PLCClient, fake_server: Generator) -> None:
        plc.declare_variables(
            {"name": "Test_M_int_0", "type": "int", "address": "MW0"},
        )

        plc.connect()
        import pdb

        pdb.set_trace()
        plc.set_variable_value(plc.variables[0], 10)
        plc.write_multi_to_plc(plc.variables)

        plc.read_multi_from_plc()

        plc.disconnect()
