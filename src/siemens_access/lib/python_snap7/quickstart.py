# Recommended on https://github.com/gijzelaerr/python-snap7
from s7 import Client

client = Client()
client.connect("192.168.1.10", 0, 1)
data = client.db_read(1, 0, 4)
client.disconnect()
