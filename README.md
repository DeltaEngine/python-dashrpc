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

Support for Special Transaction in Dash 0.13 (use testnet for block 7000, which has 2 special transactions):

```
block_hash = rpc.getblockhash(7000)
print(rpc.getblock(block_hash))
```

Returns:

```
{
	u 'merkleroot': u '5339c3b37049fc41c1e75194d36b8958dea0134cec42c5715bdae36cde87eff2',
	u 'nonce': 767772160,
	u 'previousblockhash': u '0000001f14402a48dffad2020ff158962ca57cb83c674d79a64b1a9222351b5d',
	u 'cbTx': {
		u 'merkleRootMNList': u '0000000000000000000000000000000000000000000000000000000000000000',
		u 'version': 1,
		u 'height': 7000
	},
	u 'hash': u '0000001e8b87719178a7b2b86def5ff918285fa9993e561f2ef04da18c6044bf',
	u 'version': 536870913,
	u 'tx': [u '61bc32c39a523a7705eaa52724b80d52741025547d6562d9fc588617790a06ce', u '5af494fdedadd2e2a637134e8ee59fdf52bc70b6f688764d08d26bccca9855e9'],
	u 'chainwork': u '000000000000000000000000000000000000000000000000000006498dfffa69',
	u 'mediantime': 1545086480,
	u 'height': 7000,
	u 'difficulty': Decimal('0.02184410439171994'),
	u 'nextblockhash': u '00000017758c119977653518dc971db7bd95497fcfc6e580bfcb28076e38e9f2',
	u 'confirmations': 24654,
	u 'time': 1545087335,
	u 'versionHex': u '20000001',
	u 'bits': u '1d2dc73b',
	u 'size': 684
}
```

Let's take a look at the first tx in the testnet block 7000:

```
print(rpc.getrawtransaction("61bc32c39a523a7705eaa52724b80d52741025547d6562d9fc588617790a06ce", 1))
```

which returns (take note of both the extraPayload for the actual new special transaction data, but also the cbTx for the https://github.com/dashpay/dips/blob/master/dip-0002-special-transactions.md DIP004 https://github.com/dashpay/dips/blob/master/dip-0004.md data)

```
{
	u 'cbTx': {
		u 'merkleRootMNList': u '0000000000000000000000000000000000000000000000000000000000000000',
		u 'version': 1,
		u 'height': 7000
	},
	u 'blockhash': u '0000001e8b87719178a7b2b86def5ff918285fa9993e561f2ef04da18c6044bf',
	u 'vout': [{
			u 'valueSat': 6817518157,
			u 'scriptPubKey': {
				u 'reqSigs': 1,
				u 'hex': u '76a9144f79c383bc5d3e9d4d81b98f87337cedfa78953688ac',
				u 'addresses': [u 'yTZg6eePKxbJZyoaC93bVrTUq5vjhFrbst'],
				u 'asm': u 'OP_DUP OP_HASH160 4f79c383bc5d3e9d4d81b98f87337cedfa789536 OP_EQUALVERIFY OP_CHECKSIG',
				u 'type': u 'pubkeyhash'
			},
			u 'value': Decimal('68.17518157'),
			u 'n': 0
		}, {
			u 'valueSat': 6885000000,
			u 'scriptPubKey': {
				u 'reqSigs': 1,
				u 'hex': u '76a914bafef41416718b231d5ca0143dccbc360d06b77688ac',
				u 'addresses': [u 'ydNBxMkDgHxdj6vn9K3SxZXnh159mxUieh'],
				u 'asm': u 'OP_DUP OP_HASH160 bafef41416718b231d5ca0143dccbc360d06b776 OP_EQUALVERIFY OP_CHECKSIG',
				u 'type': u 'pubkeyhash'
			},
			u 'value': Decimal('68.85000000'),
			u 'n': 1
		}, {
			u 'valueSat': 67481843,
			u 'scriptPubKey': {
				u 'reqSigs': 1,
				u 'hex': u '76a914badadfdebaa6d015a0299f23fbc1fcbdd72ba96f88ac',
				u 'addresses': [u 'ydMSjYqwv4xTossPJ1xndTxwS1Hho9DmuM'],
				u 'asm': u 'OP_DUP OP_HASH160 badadfdebaa6d015a0299f23fbc1fcbdd72ba96f OP_EQUALVERIFY OP_CHECKSIG',
				u 'type': u 'pubkeyhash'
			},
			u 'value': Decimal('0.67481843'),
			u 'n': 2
		}, {
			u 'valueSat': 0,
			u 'scriptPubKey': {
				u 'type': u 'nulldata',
				u 'hex': u '6a28421df280ea438199057112738c5149e4307689d1201c96a66fbe83f4aa0c40160000000003000000',
				u 'asm': u 'OP_RETURN 421df280ea438199057112738c5149e4307689d1201c96a66fbe83f4aa0c40160000000003000000'
			},
			u 'value': Decimal('0E-8'),
			u 'n': 3
		}
	],
	u 'vin': [{
			u 'coinbase': u '02581b0e2f5032506f6f6c2d74444153482f',
			u 'sequence': 4294967295
		}
	],
	u 'time': 1545087335,
	u 'hex': u '03000500010000000000000000000000000000000000000000000000000000000000000000ffffffff1202581b0e2f5032506f6f6c2d74444153482fffffffff044d125b96010000001976a9144f79c383bc5d3e9d4d81b98f87337cedfa78953688ac40c3609a010000001976a914bafef41416718b231d5ca0143dccbc360d06b77688acf3b00504000000001976a914badadfdebaa6d015a0299f23fbc1fcbdd72ba96f88ac00000000000000002a6a28421df280ea438199057112738c5149e4307689d1201c96a66fbe83f4aa0c4016000000000300000000000000260100581b00000000000000000000000000000000000000000000000000000000000000000000',
	u 'txid': u '61bc32c39a523a7705eaa52724b80d52741025547d6562d9fc588617790a06ce',
	u 'blocktime': 1545087335,
	u 'version': 3,
	u 'confirmations': 24654,
	u 'extraPayloadSize': 38,
	u 'extraPayload': u '0100581b00000000000000000000000000000000000000000000000000000000000000000000',
	u 'instantlock': False,
	u 'locktime': 0,
	u 'height': 7000,
	u 'type': 5,
	u 'size': 261
}
```
