# Copied from https://github.com/gijzelaerr/s7commplus
# See the s7commplus documentation for the complete user guide and API reference.
from s7commplus import Client
from s7commplus import device_family, device_name

with Client() as client:
    client.connect("192.168.1.10", 0, 1)
    data = client.db_read(1, 0, 4)

# Optimized blocks are read and written by tag name, as Python values; a struct, UDT or array name gives a dict or list:

with Client() as client:
    client.connect("192.168.1.10", use_tls=True, tls_ca="plc-ca.pem")  # verify the PLC certificate
    temperature = client.read_value("Data_block_1.temperature")
    client.write_value("Data_block_1.recipe", {"speed": 120, "name": "batch 7"})

# S7CommPlus is used by newer S7-1200/1500 PLCs when classic PUT/GET access is disabled. This is an unofficial implementation and is not affiliated with, endorsed by, or supported by Siemens AG. Test against an isolated controller before using it in production or safety-relevant environments.
# Some older PLCs advertise only their SessionKey family instead of a complete public-key fingerprint. Client and AsyncClient try the bounded set of bundled keys from that family on fresh sessions and cache the confirmed key for the PLC. Set allow_legacy_key_fallback=False on connect() when key probing must be disabled.
# The order number a PLC reports during connect can be turned into a readable module name and family:

device_name("6ES7 512-1DK01-0AB0")   # 'CPU 1512SP-1 PN'
device_family("6ES7 512-1DK01-0AB0")  # 's7-1500-sp'
