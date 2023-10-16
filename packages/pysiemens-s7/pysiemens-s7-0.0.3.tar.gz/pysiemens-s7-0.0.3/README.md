# Pysiemens-S7


Pysiemens-s7 offers an abstraction level for the package [python-snap7](https://python-snap7.readthedocs.io/en/latest/index.html). What it provides is a siemens native way to interact with the classes, using [pytdantic](https://docs.pydantic.dev/latest/) to validate and parse all the addresses and parameters.

  

The objective is to be able to use the same names address you will read in TIA Portal interface or Step7.

## Installation

```shell
pip install pysiemens-s7
```


## PLCClient


This class inherits from the snap7 [Client](https://python-snap7.readthedocs.io/en/latest/API/client.html) class, so you can still use all its native methods. 

The key difference is that you can use a *siemens-s7* vocabulary to interact with the client, instead of byte index and byte arrays. So basically what it does is to parse human readable addresses/data while using the powerful [python-snap7](https://python-snap7.readthedocs.io/en/latest/index.html) library, using the amazing data validator package [pydantic](https://docs.pydantic.dev/latest/)


#### PLCClient Instance


To connect to a PLC you can configure the client using two ways:

- Using a Python Dict:

```python
  from pysiemens.s7_plc import PLCClient
  plc_address = {
      "ip_address": "127.0.0.1",
      "rack": 0,  # default 0
      "slot": 1,  # default 1
      "port": 102 # defaul 102,
      "cycle_time": 5000 # time slot behind scan cycles, default 5000
  }
  new_plc = PLCClient(plc_address)
```


- Using the provided pydantic class:
  
```python
from pysiemens.s7_plc import PLCClient
from pysiemens.schemas.s7_plc_schema import PLCSchemaConnection # plc address schema

plc_address = PLCSchemaConnection(
  ip_address = "127.0.0.1",
  rack = 0,  # default 0
  slot = 1,  # default 1
  port = 102 # defaul 102,
  cycle_time = 5000 # time slot behind scan cycles, default 5000
)

new_plc = PLCClient(plc_address)

```


In both cases the `PLCClient`object will try to parse the provided values to valid parameters. If it doesn't succeed, it will raise a validation error. For example, if we try to use a non valid IP address:


```python
from pysiemens.s7_plc import PLCClient
from pysiemens.schemas.s7_plc_schema import PLCSchemaConnection # plc address schema

plc_address = PLCSchemaConnection(
  ip_address = "2,5,7,8",
  rack = 0,  # default 0
  slot = 1,  # default 1
  port = 102 # defaul 102,
  cycle_time = 5000 # time slot behind scan cycles, default 5000
)

new_plc = PLCClient(plc_address)


#> pydantic_core._pydantic_core.ValidationError: 1 validation error for PLCSchema
#> ip_address
#> Input is not a valid IPv4 address [type=ip_v4_address, input_value='2,5,7,8',  
#> input_type=str]

```

Using pydantic classes allows you to access variables data in a more easily way, with class properties.

> Note:
> On populating all the PLC Parameters you will see also `variables`set to `None`. This is 
> because we are setting just the connection parameters. Later we will add some addresses to 
> read/write  

```python
print(new_plc.params)
#> PLCSchema(ip_address=IPv4Address('127.0.0.1'), rack=0, slot=1, port=102, cycle_time=5000, variables=None)

```
You can also access to nested properties with the simple dot notation:

```python
print(new_plc.params.ip_address)
#>IPv4Address('127.0.0.1')
```

You can also populate all the parameters from the pydantic class using the method `model_dump()`, which will return a python Dict with all the parameters:

```python
print(plc.params.model_dump())
#>{'cycle_time': 5000,
#> 'ip_address': IPv4Address('127.0.0.1'),
#> 'port': 102,
#> 'rack': 0,
#> 'slot': 1,
#> 'variables': None}
```
#### Declaring Variables

To declare PLC variables it can be used the native siemens naming patterns, for example if we want to declare a Boolean from Data Block 0 we can pass a dict with the type and the absolute address in the PLC:

First, we need to create a new plc client:

```python
from pysiemens.s7_plc import PLCClient
from pysiemens.schemas.s7_plc_schema import PLCSchema

plc_address = PLCSchema(plc_name="plc_01", ip_address="192.168.1.1")
client = PLCClient(plc_address)

```

Once we have a client, we can declare variables to the object by using the `PLCClient.declare_variables()` method:


> Note
> The Data Block must be unoptimized in the source PLC in series 1200 and 1500 in order to have the absolute address, eg. DB1.DBX3.2



```python

client.declare_variables(
    {"name": "Test_bool", "type": "bool", "address": "DB0.DBX0.3"},
)

```
The client will attempt to parse the input dict to a valid S7 Address pydantic class. If we print the client variables after declaring the previous Data Block boolean we should recieve a variable object:

```python
print(client.variables)

#>[S7Boolean(name='Test_bool', address='DB0.DBX0.3', type='BOOL', mem_area='DB', db_num=0, start_byte=0, bit_size=1, value=None, bit_position=3, byte_size=1)]

```
As you can see, the variables itself are pydantic objects.

Now lets declare different type variables:

```python
client.declare_variables(
    {"name": "Test_bool", "type": "bool", "direction": "DB0.DBX0.3"},
    {"name": "Test_int", "type": "int", "direction": "DB0.DBw6"},
)
print(client.variables)

#>[S7Boolean(name='Test_bool', direction='DB0.DBX0.3', type='BOOL', mem_area='DB', db_num=0, start_byte=0, bit_size=1, value=None, bit_position=3, byte_size=1), 
#> S7Int(name='Test_int', direction='DB0.DBW6', type='INT', mem_area='DB', db_num=0, start_byte=6, bit_size=16, value=None, byte_size=2)]

```

### Variables validation

While declaring variables, PLCClient class will validate the addresses are valid and corresponds to its direction and data type.

For example if we try to add an integer with a Bool direction (note the 'X' instead of 'W'), it will raise an error:

```python
client.declare_variables(
    {"name": "Test_int", "type": "int", "direction": "DB0.DBX6"},
)
#>pysiemens.errors.S7ParsingError: S7Error: Invalid address provided. Can not parse DB0.DBX6 to a valid INT
```


```python

```


