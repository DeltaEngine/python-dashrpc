# python-dashrpc -- Python2 interface to Dash's JSON-RPC API

AuthServiceProxy is an improved version of python-jsonrpc.

It includes the following generic improvements:

- HTTP connections persist for the life of the AuthServiceProxy object
- sends protocol 'version', per JSON-RPC 1.1
- sends proper, incrementing 'id'
- uses standard Python json lib
- can optionally log all RPC calls and results
- JSON-2.0 batch support

It also includes the following dash-specific details:

- sends Basic HTTP authentication headers
- parses all JSON numbers that look like floats as Decimal,
  and serializes Decimal values to JSON-RPC connections.

Installation:

- This library has only been tested in Python2
  - With Python3 you mostly will run into this issue: https://stackoverflow.com/questions/33520423/python-error-typeerror-getsockaddrarg-af-inet-address-must-be-tuple-not-int/33520658
  - Instead check out https://github.com/DeltaEngine/pycoin and https://github.com/DeltaEngine/pybitcointools
- python setup.py install

Example usage:

```
from dashrpc.authproxy import AuthServiceProxy, JSONRPCException

#check dash.conf for settings
rpcuser = "TestDash"
rpcpassword = "LocalOnly"
rpcip = "127.0.0.1"
rpcport = 19998 #19998 for testnet, 9998 for mainnet
rpc_params = "http://%s:%s@%s:%s"%(rpcuser, rpcpassword, rpcip, rpcport)
rpc = AuthServiceProxy(rpc_params)
print(rpc.getinfo())

best_block_hash = rpc.getbestblockhash()
print(rpc.getblock(best_block_hash))
```