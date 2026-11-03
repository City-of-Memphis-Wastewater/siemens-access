# Siemens Access

An attempt to access Siemens hardare using open source Python libraries, like s7commplus and python-snap7.

Useful libraries as Python dependencies:
- https://github.com/gijzelaerr/python-snap7
- https://github.com/gijzelaerr/s7commplus

## Helptree

See the `siemens-access` Typer CLI structure.

```bash
siemens-access helptree
```

## s7commplus CLI

Run the s7commplus CLI directly if installed with pipx or installed in the active environment.

```bash
uv add s7commplus
# or 
pipx install s7commplus
 
s7commplus --version 
s7commplus --help   
```

See `s7commplus` library, with import `s7commplus`.

```bash
python3 -c "import s7commplus;print(dir(s7commplus))" 
>> ['Alarm', 'AlarmNotification', 'AlarmText', 'ArrayDimension', 'AsyncClient', 'AsyncSubscriptionQueue', 'CPUState', 'Client', 'DBWriteItem', 'DEVICE_NAMES', 'DataBlock', 'ExploreDataBlock', 'LanguageId', 'Member', 'PresetIdentity', 'PresetStream', 'S7CommPlusConnection', 'Server', 'SubscriptionDiagnostics', 'SubscriptionItem', 'SubscriptionNotification', 'SubscriptionRestoreResult', 'SymbolCatalog', 'SymbolicReadItem', 'SymbolicTag', 'Tag', 'TagResult', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'alarm', 'async_client', 'attribute_name', 'blob_decompressor', 'block_interface_from_explore', 'catalog', 'client', 'codec', 'connection', 'datablocks_from_explore', 'decompress_blob', 'describe_attribute', 'device_family', 'device_name', 'devices', 'error', 'find_and_decompress', 'iter_preset_headers', 'iter_preset_streams', 'legitimation', 'object_model', 'protocol', 'server', 'subscription', 'tag_browser', 'tags_from_explore', 'transport', 'typeinfo', 'v1_session_key', 'values', 'vlq', 'zlib_dicts']
s7commplus --version 
>> s7commplus 0.3.0
```

## python-snap7

See `python-snap7` library, with import `s7`.

```bash
python3 -c "import s7;print(s7.__version__);print(dir(s7))"
>> 3.3.1
>> ['Area', 'AsyncClient', 'Block', 'Client', 'DB', 'ForceEntry', 'Logo', 'NodeS7Tag', 'PLC4XTag', 'PPIArea', 'PPIClient', 'Partner', 'Row', 'Server', 'SrvArea', 'SrvEvent', 'Tag', 'WordLen', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'from_browse', 'importlib', 'load_csv', 'load_json', 'load_tia_xml', 'parse_tag', 'snap7', 'sys']
```
