from web3.middleware import geth_poa_middleware
from web3 import Web3
import json
import time

#erc20 basic function

class Erc20:
    weth_abi='[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

    def approve(_web3:Web3,_abi,_erc20_address,_approve_address,_amount,_public_key,_private_key):
        erc20_contract=_web3.eth.contract(address=_erc20_address, abi=json.loads(_abi))
        approve_function=erc20_contract.functions.approve(_approve_address,_amount)
        nonce=_web3.eth.get_transaction_count(_public_key)
        tx_param={
            'from': _public_key,
            'value': 0,
            'nonce': nonce,
            'type': '0x2',
            'maxFeePerGas': Web3.to_wei(160, 'gwei'),
            'maxPriorityFeePerGas': Web3.to_wei(30, 'gwei'),
        }
        transaction=approve_function.build_transaction(tx_param)
        signed_transaction=_web3.eth.account.sign_transaction(transaction,private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))

    def withdraw_with_nonce(_web3:Web3,_amount,_weth_address,_gas,_public_key,_private_key,_nonce):
        weth_contract=_web3.eth.contract(address=_weth_address, abi=json.loads(Erc20.weth_abi))
        withdraw_function=weth_contract.functions.withdraw(_amount)
        params={
            'from': _public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2',
            'gas':_gas
        }
        transaction=withdraw_function.build_transaction(params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))
    
    def deposit(_web3:Web3,_amount,_weth_address,_public_key,_private_key):
        nonce=_web3.eth.get_transaction_count(_public_key)
        weth_contract=_web3.eth.contract(address=_weth_address, abi=json.loads(Erc20.weth_abi))
        deposit_function=weth_contract.functions.deposit()
        params={
            'from': _public_key,
            'value': _amount,
            'nonce': nonce,
            'type': '0x2'
        }
        transaction=deposit_function.build_transaction(params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))
    
    def withdraw(_web3:Web3,_amount,_weth_address,_public_key,_private_key):
        nonce=_web3.eth.get_transaction_count(_public_key)
        weth_contract=_web3.eth.contract(address=_weth_address, abi=json.loads(Erc20.weth_abi))
        withdraw_function=weth_contract.functions.withdraw(_amount)
        params={
            'from': _public_key,
            'value': 0,
            'nonce': nonce,
            'type': '0x2'
        }
        transaction=withdraw_function.build_transaction(params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))
    
# dex connector
class UniswapV2:
    
    uniswap_v2_factory_abi='[ { "inputs": [ { "internalType": "address", "name": "_feeToSetter", "type": "address" } ], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "token0", "type": "address" }, { "indexed": true, "internalType": "address", "name": "token1", "type": "address" }, { "indexed": false, "internalType": "address", "name": "pair", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "PairCreated", "type": "event" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "allPairs", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "allPairsLength", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "tokenA", "type": "address" }, { "internalType": "address", "name": "tokenB", "type": "address" } ], "name": "createPair", "outputs": [ { "internalType": "address", "name": "pair", "type": "address" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "feeTo", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "feeToSetter", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" } ], "name": "getPair", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "migrator", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "pairCodeHash", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_feeTo", "type": "address" } ], "name": "setFeeTo", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_feeToSetter", "type": "address" } ], "name": "setFeeToSetter", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_migrator", "type": "address" } ], "name": "setMigrator", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]'
    uniswap_v2_pair_abi='[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "sender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" } ], "name": "Burn", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "sender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256" } ], "name": "Mint", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "sender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount0In", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1In", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount0Out", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1Out", "type": "uint256" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" } ], "name": "Swap", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "uint112", "name": "reserve0", "type": "uint112" }, { "indexed": false, "internalType": "uint112", "name": "reserve1", "type": "uint112" } ], "name": "Sync", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "MINIMUM_LIQUIDITY", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "PERMIT_TYPEHASH", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" } ], "name": "burn", "outputs": [ { "internalType": "uint256", "name": "amount0", "type": "uint256" }, { "internalType": "uint256", "name": "amount1", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "factory", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getReserves", "outputs": [ { "internalType": "uint112", "name": "reserve0", "type": "uint112" }, { "internalType": "uint112", "name": "reserve1", "type": "uint112" }, { "internalType": "uint32", "name": "blockTimestampLast", "type": "uint32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" } ], "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "kLast", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" } ], "name": "mint", "outputs": [ { "internalType": "uint256", "name": "liquidity", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "nonces", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "uint256", "name": "deadline", "type": "uint256" }, { "internalType": "uint8", "name": "v", "type": "uint8" }, { "internalType": "bytes32", "name": "r", "type": "bytes32" }, { "internalType": "bytes32", "name": "s", "type": "bytes32" } ], "name": "permit", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "price0CumulativeLast", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "price1CumulativeLast", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" } ], "name": "skim", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amount0Out", "type": "uint256" }, { "internalType": "uint256", "name": "amount1Out", "type": "uint256" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "swap", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "sync", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "token0", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "token1", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]'
    uniswap_v2_erc20_abi='[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]'
    uniswap_v2_route_abi='[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

    '''
        used for uniswap v2 based dex
    '''
    def __init__(self,_web3:Web3,_factory_address,_route_address,_public_key,_private_key):
        self.my_public_key=_public_key
        self.my_private_key=_private_key
        self.factory_address=_factory_address
        self.route_address=_route_address
        self.web3 = _web3
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        print('############################')
        print("contract connection is "+str(self.web3.is_connected()))
        if self.web3.is_connected():
            self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
            print("nonce = ",self.nonce)
        print('############################')
        # uniswap_Factory
        self.factory_abi = json.loads(self.uniswap_v2_factory_abi)
        self.pair_abi=json.loads(self.uniswap_v2_pair_abi)
        self.erc20_abi=json.loads(self.uniswap_v2_erc20_abi)
        self.route_abi=json.loads(self.uniswap_v2_route_abi)

        self.factory_contract = self.web3.eth.contract(address=self.factory_address, abi=self.factory_abi)
        self.route_contract=self.web3.eth.contract(address=self.route_address,abi=self.route_abi)

    def reset_nonce(self):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)

    def send_transaction(self, function, params,_owner_private_key):
        transaction = function.build_transaction(params)
        signedTransaction=self.web3.eth.account.sign_transaction(transaction, private_key=_owner_private_key)
        return self.web3.eth.send_raw_transaction(signedTransaction.rawTransaction)
    
    def send_raw_transation(_web3:Web3,_function,_params,_private_key):
        transaction=_function.build_transaction(_params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    
    ###util###

    def decode_swap_input_data(self,_input):
        return self.route_contract.decode_function_input(_input)

    def set_private_key(self,_private_key):
        self.my_private_key=_private_key

    def set_public_keky(self,_public_key):
        self.my_public_key=_public_key

    ###IUniswapV2Router01###
    def addLiquidity():
        return

    def addLiquidityETH():
        return

    def removeLiquidity():
        return

    def removeLiquidityETH():
        return

    def removeLiquidityWithPermit():
        return

    def removeLiquidityETHWithPermit():
        return

    def swapExactTokensForTokens(self,_amount_in,_amount_out_min,_path,_to,_deadline):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapExactTokensForTokens(_amount_in, _amount_out_min, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)

    def swapExactTokenForTokensWithGas(self,_amount_in,_amount_out_min,_path,_to,_deadline,_gas):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapExactTokensForTokens(_amount_in, _amount_out_min, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2',
            'gas':_gas
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)    

    def swapExactTokenForTokensWithGasWithNonce(self,_amount_in,_amount_out_min,_path,_to,_deadline,_gas,_nonce):
        swapFunction=self.route_contract.functions.swapExactTokensForTokens(_amount_in, _amount_out_min, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2',
            'gas':_gas
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)   

    def swapExactTokenForTokensWithGasWithNonceWithPriority(self,_amount_in,_amount_out_min,_path,_to,_deadline,_gas,_nonce,_priority_fee):
        swapFunction=self.route_contract.functions.swapExactTokensForTokens(_amount_in, _amount_out_min, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2',
            'gas':_gas,
            'maxPriorityFeePerGas': _priority_fee
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response) 

    def swapTokensForExactTokens(self,_amount_out,_amount_in_max,_path,_to,_deadline):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapTokensForExactTokens(_amount_out,_amount_in_max, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)

    def swapExactETHForTokens(self,_amount_out_min,_path,_to,_deadline):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapExactETHForTokens(_amount_out_min, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)

    def swapTokensForExactETH(self,_amount_out,_amount_in_max,_path,_to,_deadline):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapTokensForExactETH(_amount_out,_amount_in_max, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)
    
    def swap_tokens_for_exact_eth_with_nonce(self,_amount_out,_amount_in_max,_path,_to,_deadline,_nonce):
        swapFunction=self.route_contract.functions.swapTokensForExactETH(_amount_out,_amount_in_max, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)

    def swapExactTokensForETH(self,_amount_in,_amount_out_min,_path,_to,_deadline):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapExactTokensForETH(_amount_in,_amount_out_min, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)

    def swapETHForExactTokens(self,_amount_out,_path,_to,_deadline):
        self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
        swapFunction=self.route_contract.functions.swapETHForExactTokens(_amount_out, _path, _to, _deadline)
        params={
            'from': self.my_public_key,
            'value': 0,
            'nonce': self.nonce,
            'type': '0x2'
        }
        response = self.send_transaction(swapFunction,params,self.my_private_key)
        return self.web3.to_hex(response)

    ###IUniswapV2Router02###
    def swap_tokens_for_exact_tokens(_web3:Web3,route_address,route_abi,_public_key,_private_key,
        _amount_out,_amount_in_max,_path,_to):
        route_contract=_web3.eth.contract(address=route_address,abi=route_abi)
        nonce=_web3.eth.get_transaction_count(_public_key)
        deadline=int(time.time())+40
        swap_function=route_contract.functions.swapTokensForExactTokens(_amount_out,_amount_in_max, _path, _to, deadline)
        tx_params={
            'from': _public_key,
            'value': 0,
            'nonce': nonce,
            'type': '0x2'
        }
        response=UniswapV2.send_raw_transation(_web3,swap_function,tx_params,_private_key)
        return _web3.to_hex(response)

    def swap_exact_tokens_for_tokens(_web3:Web3,route_address,route_abi,_public_key,_private_key,
        _amount_in,_amount_out_min,_path,_to):
        route_contract=_web3.eth.contract(address=route_address,abi=route_abi)
        nonce=_web3.eth.get_transaction_count(_public_key)
        deadline=int(time.time())+40
        swap_function=route_contract.functions.swapExactTokensForTokens(_amount_in,_amount_out_min, _path, _to, deadline)
        tx_params={
            'from': _public_key,
            'value': 0,
            'nonce': nonce,
            'type': '0x2'
        }
        response=UniswapV2.send_raw_transation(_web3,swap_function,tx_params,_private_key)
        return _web3.to_hex(response)


    ###IUniswapV2Router02-LIBRARY FUNCTIONS
    def quote(self,_amount0,_reserve0,_reserve1):
        return self.route_contract.functions.quote(_amount0,_reserve0,_reserve1).call()

    def get_amounts_out(_web3:Web3,route_address,route_abi,_amount_in,_path):
        route_contract=_web3.eth.contract(address=route_address,abi=route_abi)
        return route_contract.functions.getAmountsOut(_amount_in,_path).call()
    
    def get_amounts_in(_web3:Web3,route_address,route_abi,_amount_out,_path):
        route_contract=_web3.eth.contract(address=route_address,abi=route_abi)
        return route_contract.functions.getAmountsIn(_amount_out,_path).call()

    #deprecated
    def getAmountOut(self,_amount_in,_reserve_in,_reserve_out):
        return self.route_contract.functions.getAmountOut(_amount_in,_reserve_in,_reserve_out).call()
    #deprecated
    def getAmountIn(self,_amount_out,_reserve_in,_reserve_out):
        return self.route_contract.functions.getAmountIn(_amount_out,_reserve_in,_reserve_out).call()
    #deprecated
    def getAmountsOut(self,_amount_in,_path):
        return self.route_contract.functions.getAmountsOut(_amount_in,_path).call()
    #deprecated
    def getAmountsIn(self,_amount_out,_path):
        return self.route_contract.functions.getAmountsIn(_amount_out,_path).call()


    def getAmountOutLocal(self,_amount_in,_reserve_in,_reserve_out):
        assert _amount_in>0
        assert (_reserve_in>0) & (_reserve_out>0)
        amountInWithFee=997*_amount_in
        numerator=amountInWithFee*_reserve_out
        denominator=(_reserve_in*1000)+amountInWithFee
        amountOut = numerator / denominator
        return amountOut

    def getAmountInLocal(self,_amount_out,_reserve_in,_reserve_out):
        assert _amount_out>0
        assert (_reserve_in>0) & (_reserve_out>0)
        numerator=_reserve_in*1000*_amount_out
        denominator=(_reserve_out-_amount_out)*997
        amountIn=int(numerator/denominator)+1
        return amountIn

    ###UniswapV2ERC20###

    def get_token_name(self,_token_address):
        token_contract=self.web3.eth.contract(address=_token_address,abi=self.erc20_abi)
        return token_contract.functions.name().call()
    
    def get_token_symbol(self,_token_address):
        token_contract=self.web3.eth.contract(address=_token_address,abi=self.erc20_abi)
        return token_contract.functions.symbol().call()

    def get_token_balance_of(self,_token_address,_owner_public_address):
        token_contract=self.web3.eth.contract(address=_token_address,abi=self.erc20_abi)
        return token_contract.functions.balanceOf(_owner_public_address).call()

    def approve():
        return

    def transfer():
        return

    ###UniswapV2Factory###

    def get_all_pairs_length(self):
        return self.factory_contract.functions.allPairsLength().call()

    def get_pair(self,_token0_address,_token1_address):
        return self.factory_contract.functions.getPair(_token0_address,_token1_address).call()

    def get_pair_by_index(self,_index):
        all_pairs_length = self.factory_contract.functions.allPairsLength().call()
        index=_index if _index<all_pairs_length else all_pairs_length
        return self.factory_contract.functions.allPairs(index).call()

    def get_first_length_pairs(self,_length):
        all_pairs_length = self.factory_contract.functions.allPairsLength().call()
        length=_length if _length<all_pairs_length else all_pairs_length
        result=[]
        for i in range(0, length):
            all_pairs_address = self.factory_contract.functions.allPairs(i).call()
            result.append(all_pairs_address)
        return result

    ###UniswapV2Pair###
    def get_pair_reserve(self,pair_address):
        pairContract=self.web3.eth.contract(address=pair_address, abi=self.pair_abi)
        reserve0,reserve1,blockTimeStamp=pairContract.functions.getReserves().call()
        return reserve0,reserve1,blockTimeStamp


    def get_pair_info(self,pair_address):
        pairContract=self.web3.eth.contract(address=pair_address, abi=self.pair_abi)
        token0Address=pairContract.functions.token0().call()
        token1Address=pairContract.functions.token1().call()
        reserve0,reserve1,blockTimeStamp=pairContract.functions.getReserves().call()
        # token0_contract=self.web3.eth.contract(address=token0Address, abi=self.erc20_abi)
        # token1_contract=self.web3.eth.contract(address=token1Address, abi=self.erc20_abi)
        # token0_name=token0_contract.functions.name().call()
        # token1_name=token1_contract.functions.name().call()
        price0=reserve1/reserve0
        price1=reserve0/reserve1
        # print("token0:",str(token0Address),"--name:",str(token0_name),"--price:",str(price0))
        # print("token1:",str(token1Address),"--name:",str(token1_name),"--price:",str(price1))
        # print("reserve0",str(reserve0))
        # print("reserve1",str(reserve1))
        # print("blockTimeStamp",str(blockTimeStamp))
        return token0Address,reserve0,token1Address,reserve1,blockTimeStamp,price0,price1

class UniswapV2Pair:

    def get_reserves(_web3:Web3,_pair_address,_pair_abi):
        pair_contract=_web3.eth.contract(address=_pair_address,abi=_pair_abi)
        reserve0,reserve1,blockTimeStamp=pair_contract.functions.getReserves().call()
        return reserve0,reserve1,blockTimeStamp

class UniswapV3:
    #https://etherscan.io/address/0x1f98431c8ad98523631ae4a59f267346ea31f984
    uniswap_v3_factory_abi='[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":true,"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"FeeAmountEnabled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":true,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":false,"internalType":"int24","name":"tickSpacing","type":"int24"},{"indexed":false,"internalType":"address","name":"pool","type":"address"}],"name":"PoolCreated","type":"event"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"enableFeeAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"","type":"uint24"}],"name":"feeAmountTickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint24","name":"","type":"uint24"}],"name":"getPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"parameters","outputs":[{"internalType":"address","name":"factory","type":"address"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    uniswap_v3_pair_abi='[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "sender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" } ], "name": "Burn", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "sender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256" } ], "name": "Mint", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "sender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "amount0In", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1In", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount0Out", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "amount1Out", "type": "uint256" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" } ], "name": "Swap", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "uint112", "name": "reserve0", "type": "uint112" }, { "indexed": false, "internalType": "uint112", "name": "reserve1", "type": "uint112" } ], "name": "Sync", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "MINIMUM_LIQUIDITY", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "PERMIT_TYPEHASH", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" } ], "name": "burn", "outputs": [ { "internalType": "uint256", "name": "amount0", "type": "uint256" }, { "internalType": "uint256", "name": "amount1", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "factory", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getReserves", "outputs": [ { "internalType": "uint112", "name": "reserve0", "type": "uint112" }, { "internalType": "uint112", "name": "reserve1", "type": "uint112" }, { "internalType": "uint32", "name": "blockTimestampLast", "type": "uint32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" } ], "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "kLast", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" } ], "name": "mint", "outputs": [ { "internalType": "uint256", "name": "liquidity", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "nonces", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" }, { "internalType": "uint256", "name": "deadline", "type": "uint256" }, { "internalType": "uint8", "name": "v", "type": "uint8" }, { "internalType": "bytes32", "name": "r", "type": "bytes32" }, { "internalType": "bytes32", "name": "s", "type": "bytes32" } ], "name": "permit", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "price0CumulativeLast", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "price1CumulativeLast", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" } ], "name": "skim", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amount0Out", "type": "uint256" }, { "internalType": "uint256", "name": "amount1Out", "type": "uint256" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "swap", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [], "name": "sync", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "token0", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "token1", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]'
    uniswap_v3_erc20_abi='[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]'
    #https://etherscan.io/address/0xe592427a0aece92de3edee1f18e0157c05861564#code
    uniswap_v3_route_abi='[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH9","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH9","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"}],"internalType":"struct ISwapRouter.ExactInputParams","name":"params","type":"tuple"}],"name":"exactInput","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactInputSingleParams","name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMaximum","type":"uint256"}],"internalType":"struct ISwapRouter.ExactOutputParams","name":"params","type":"tuple"}],"name":"exactOutput","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMaximum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactOutputSingleParams","name":"params","type":"tuple"}],"name":"exactOutputSingle","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"refundETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowed","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowedIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"sweepToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],"name":"sweepTokenWithFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"int256","name":"amount0Delta","type":"int256"},{"internalType":"int256","name":"amount1Delta","type":"int256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"uniswapV3SwapCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"unwrapWETH9","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],"name":"unwrapWETH9WithFee","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

    '''
        used for uniswap v3 based dex
    '''
    def __init__(self,_web3,_factory_address,_route_address,_public_key,_private_key):
        self.my_public_key=_public_key
        self.my_private_key=_private_key
        self.factory_address=_factory_address
        self.route_address=_route_address
        self.web3 = _web3
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        print('############################')
        print("contract connection is "+str(self.web3.is_connected()))
        if self.web3.is_connected():
            self.nonce=self.web3.eth.get_transaction_count(self.my_public_key)
            print("nonce = ",self.nonce)
        print('############################')
        # uniswap_Factory
        self.factory_abi = json.loads(self.uniswap_v3_factory_abi)
        self.pair_abi=json.loads(self.uniswap_v3_pair_abi)
        self.erc20_abi=json.loads(self.uniswap_v3_erc20_abi)
        self.route_abi=json.loads(self.uniswap_v3_route_abi)

        self.factory_contract = self.web3.eth.contract(address=self.factory_address, abi=self.factory_abi)
        self.route_contract=self.web3.eth.contract(address=self.route_address,abi=self.route_abi)
class UniswapV3Factory:

    #factory
    #return address of pool for tokenA and tokenB with specific fee
    #10000 for 1% fee, 3000 for 0.3%, and 500 for 0.05%
    def getPool(_web3:Web3,_factory_address,_abi,_tokenA:str,_tokenB:str,_fee:int):
        return _web3.eth.contract(address=_factory_address, abi=_abi).functions.getPool(_tokenA,_tokenB,_fee).call()
    
class UniswapV3Quoter:
    #return address of pool for tokenA and tokenB with specific fee
    #10000 for 1% fee, 3000 for 0.3%, and 500 for 0.05%
    def getPool(_web3:Web3,_quoter_address,_abi,_tokenA:str,_tokenB:str,_fee:int):
        return _web3.eth.contract(address=_quoter_address, abi=_abi).functions.getPool(_tokenA,_tokenB,_fee).call()
    
    # struct QuoteExactInputSingleParams {
    #     address tokenIn;
    #     address tokenOut;
    #     uint256 amountIn;
    #     uint24 fee;
    #     uint160 sqrtPriceLimitX96;
    # }
    def quoteExactInputSingle(_web3:Web3,_quoter_address,_abi,_param):
        return _web3.eth.contract(address=_quoter_address, abi=_abi).functions.quoteExactInputSingle(_param).call()

    #path startwith input token
    def quoteExactInput(_web3:Web3,_quoter_address,_abi,path,_amount_in):
        return _web3.eth.contract(address=_quoter_address, abi=_abi).functions.quoteExactInput(path,_amount_in).call()
    
    # struct QuoteExactOutputSingleParams {
    #     address tokenIn;
    #     address tokenOut;
    #     uint256 amount;
    #     uint24 fee;
    #     uint160 sqrtPriceLimitX96;
    # }
    def quoteExactOutputSingle(_web3:Web3,_quoter_address,_abi,_param):
        return _web3.eth.contract(address=_quoter_address, abi=_abi).functions.quoteExactOutputSingle(_param).call()
    
    #path start with output token
    def quoteExactOutput(_web3:Web3,_quoter_address,_abi,path,_amount_out):
        return _web3.eth.contract(address=_quoter_address, abi=_abi).functions.quoteExactOutput(path,_amount_out).call()

class UniswapV3Router:

    # struct ExactInputSingleParams {
    #     address tokenIn;
    #     address tokenOut;
    #     uint24 fee;
    #     address recipient;
    #     uint256 deadline;
    #     uint256 amountIn;
    #     uint256 amountOutMinimum;
    #     uint160 sqrtPriceLimitX96;
    # }
    def exactInputSingle(_web3:Web3,_route_address,_abi,_nonce,_public_key,_private_key,
        _token_in,_token_out,_fee,_recipient,_deadline,_amount_in,_amount_out_min,_sqrt_price_limit):
        route_contract=_web3.eth.contract(address=_route_address, abi=_abi)
        function_params={
            'tokenIn':_token_in,
            'tokenOut':_token_out,
            'fee':_fee,
            'recipient':_recipient,
            'deadline':_deadline,
            'amountIn':_amount_in,
            'amountOutMinimum':_amount_out_min,
            'sqrtPriceLimitX96':_sqrt_price_limit
        }
        # function_params=(_token_in,_token_out,_fee,_recipient,_deadline,_amount_in,_amount_out_min,_sqrt_price_limit)
        swap_function=route_contract.functions.exactInputSingle(function_params)
        tx_params={
            'from': _public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2'
        }
        transaction=swap_function.build_transaction(tx_params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))

    # struct ExactInputParams {
    #     bytes path;
    #     address recipient;
    #     uint256 deadline;
    #     uint256 amountIn;
    #     uint256 amountOutMinimum;
    # }
    def exactInput(_web3:Web3,_route_address,_abi,_nonce,_public_key,_private_key,
        _path,_recipient,_deadline,_amountIn,_amountOutMin):
        route_contract=_web3.eth.contract(address=_route_address, abi=_abi)

        # type=['bytes','address','uint256','uint256','uint256']
        # data=[_path,_recipient,_deadline,_amountIn,_amountOutMin]
        # function_params=encode_abi(type,data)
        function_params={
            'path':_path,
            'recipient':_recipient,
            'deadline':_deadline,
            'amountIn':_amountIn,
            'amountOutMinimum':_amountOutMin
        }
        # function_params=(_path,_recipient,_deadline,_amountIn,_amountOutMin)
        swap_function=route_contract.functions.exactInput(function_params)
        tx_params={
            'from': _public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2',
            # 'gas':_gas
        }
        transaction=swap_function.build_transaction(tx_params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))

    # struct ExactOutputSingleParams {
    #     address tokenIn;
    #     address tokenOut;
    #     uint24 fee;
    #     address recipient;
    #     uint256 deadline;
    #     uint256 amountOut;
    #     uint256 amountInMaximum;
    #     uint160 sqrtPriceLimitX96;
    # }
    def exactOutputSingle(_web3:Web3,_route_address,_abi,_nonce,_public_key,_private_key,
        _token_in,_token_out,_fee,_recipient,_deadline,_amount_out,_amount_in_max,_sqrt_price_limit):
        route_contract=_web3.eth.contract(address=_route_address, abi=_abi)
        function_param={
            'tokenIn':_token_in,
            'tokenOut':_token_out,
            'fee':_fee,
            'recipient':_recipient,
            'deadline':_deadline,
            'amountOut':_amount_out,
            'amountInMaximum':_amount_in_max,
            'sqrtPriceLimitX96':_sqrt_price_limit
        }
        swap_function=route_contract.functions.exactOutputSingle(function_param)
        tx_params={
            'from': _public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2'
        }
        transaction=swap_function.build_transaction(tx_params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))


    # struct ExactOutputParams {
    #     bytes path;
    #     address recipient;
    #     uint256 deadline;
    #     uint256 amountOut;
    #     uint256 amountInMaximum;
    # }
    def exactOutput(_web3:Web3,_route_address,_abi,_nonce,_public_key,_private_key,
        _path,_recipient,_deadline,_amount_out,_amount_in_max):
        route_contract=_web3.eth.contract(address=_route_address, abi=_abi)
        function_param={
            'path':_path,
            'recipient':_recipient,
            'deadline':_deadline,
            'amountOut':_amount_out,
            'amountInMaximum':_amount_in_max
        }
        swap_function=route_contract.functions.exactOutput(function_param)
        tx_params={
            'from': _public_key,
            'value': 0,
            'nonce': _nonce,
            'type': '0x2'
        }
        transaction=swap_function.build_transaction(tx_params)
        signed_transaction=_web3.eth.account.sign_transaction(transaction, private_key=_private_key)
        return _web3.to_hex(_web3.eth.send_raw_transaction(signed_transaction.rawTransaction))
class JoeV2Factory:
    joe_factory_v2_abi=json.loads('[{"inputs":[{"internalType":"address","name":"_feeRecipient","type":"address"},{"internalType":"uint256","name":"_flashLoanFee","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"bp","type":"uint256"}],"name":"BinHelper__BinStepOverflows","type":"error"},{"inputs":[],"name":"BinHelper__IdOverflows","type":"error"},{"inputs":[],"name":"LBFactory__AddressZero","type":"error"},{"inputs":[{"internalType":"uint256","name":"binStep","type":"uint256"}],"name":"LBFactory__BinStepHasNoPreset","type":"error"},{"inputs":[{"internalType":"uint256","name":"lowerBound","type":"uint256"},{"internalType":"uint16","name":"binStep","type":"uint16"},{"internalType":"uint256","name":"higherBound","type":"uint256"}],"name":"LBFactory__BinStepRequirementsBreached","type":"error"},{"inputs":[{"internalType":"uint16","name":"filterPeriod","type":"uint16"},{"internalType":"uint16","name":"decayPeriod","type":"uint16"}],"name":"LBFactory__DecreasingPeriods","type":"error"},{"inputs":[],"name":"LBFactory__FactoryLockIsAlreadyInTheSameState","type":"error"},{"inputs":[{"internalType":"uint256","name":"fees","type":"uint256"},{"internalType":"uint256","name":"maxFees","type":"uint256"}],"name":"LBFactory__FeesAboveMax","type":"error"},{"inputs":[{"internalType":"uint256","name":"fees","type":"uint256"},{"internalType":"uint256","name":"maxFees","type":"uint256"}],"name":"LBFactory__FlashLoanFeeAboveMax","type":"error"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"LBFactory__FunctionIsLockedForUsers","type":"error"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"}],"name":"LBFactory__IdenticalAddresses","type":"error"},{"inputs":[],"name":"LBFactory__ImplementationNotSet","type":"error"},{"inputs":[{"internalType":"contract IERC20","name":"tokenX","type":"address"},{"internalType":"contract IERC20","name":"tokenY","type":"address"},{"internalType":"uint256","name":"_binStep","type":"uint256"}],"name":"LBFactory__LBPairAlreadyExists","type":"error"},{"inputs":[],"name":"LBFactory__LBPairIgnoredIsAlreadyInTheSameState","type":"error"},{"inputs":[{"internalType":"contract IERC20","name":"tokenX","type":"address"},{"internalType":"contract IERC20","name":"tokenY","type":"address"},{"internalType":"uint256","name":"binStep","type":"uint256"}],"name":"LBFactory__LBPairNotCreated","type":"error"},{"inputs":[{"internalType":"address","name":"LBPairImplementation","type":"address"}],"name":"LBFactory__LBPairSafetyCheckFailed","type":"error"},{"inputs":[{"internalType":"uint16","name":"protocolShare","type":"uint16"},{"internalType":"uint256","name":"max","type":"uint256"}],"name":"LBFactory__ProtocolShareOverflows","type":"error"},{"inputs":[{"internalType":"contract IERC20","name":"quoteAsset","type":"address"}],"name":"LBFactory__QuoteAssetAlreadyWhitelisted","type":"error"},{"inputs":[{"internalType":"contract IERC20","name":"quoteAsset","type":"address"}],"name":"LBFactory__QuoteAssetNotWhitelisted","type":"error"},{"inputs":[{"internalType":"uint16","name":"reductionFactor","type":"uint16"},{"internalType":"uint256","name":"max","type":"uint256"}],"name":"LBFactory__ReductionFactorOverflows","type":"error"},{"inputs":[{"internalType":"address","name":"feeRecipient","type":"address"}],"name":"LBFactory__SameFeeRecipient","type":"error"},{"inputs":[{"internalType":"uint256","name":"flashLoanFee","type":"uint256"}],"name":"LBFactory__SameFlashLoanFee","type":"error"},{"inputs":[{"internalType":"address","name":"LBPairImplementation","type":"address"}],"name":"LBFactory__SameImplementation","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"},{"internalType":"int256","name":"y","type":"int256"}],"name":"Math128x128__PowerUnderflow","type":"error"},{"inputs":[],"name":"PendingOwnable__AddressZero","type":"error"},{"inputs":[],"name":"PendingOwnable__NoPendingOwner","type":"error"},{"inputs":[],"name":"PendingOwnable__NotOwner","type":"error"},{"inputs":[],"name":"PendingOwnable__NotPendingOwner","type":"error"},{"inputs":[],"name":"PendingOwnable__PendingOwnerAlreadySet","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds16Bits","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"unlocked","type":"bool"}],"name":"FactoryLockedStatusUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"contract ILBPair","name":"LBPair","type":"address"},{"indexed":false,"internalType":"uint256","name":"binStep","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"baseFactor","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"filterPeriod","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"decayPeriod","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"reductionFactor","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"variableFeeControl","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"protocolShare","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"maxVolatilityAccumulated","type":"uint256"}],"name":"FeeParametersSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldRecipient","type":"address"},{"indexed":false,"internalType":"address","name":"newRecipient","type":"address"}],"name":"FeeRecipientSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldFlashLoanFee","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newFlashLoanFee","type":"uint256"}],"name":"FlashLoanFeeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"contract IERC20","name":"tokenX","type":"address"},{"indexed":true,"internalType":"contract IERC20","name":"tokenY","type":"address"},{"indexed":true,"internalType":"uint256","name":"binStep","type":"uint256"},{"indexed":false,"internalType":"contract ILBPair","name":"LBPair","type":"address"},{"indexed":false,"internalType":"uint256","name":"pid","type":"uint256"}],"name":"LBPairCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"contract ILBPair","name":"LBPair","type":"address"},{"indexed":false,"internalType":"bool","name":"ignored","type":"bool"}],"name":"LBPairIgnoredStateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldLBPairImplementation","type":"address"},{"indexed":false,"internalType":"address","name":"LBPairImplementation","type":"address"}],"name":"LBPairImplementationSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"pendingOwner","type":"address"}],"name":"PendingOwnerSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"binStep","type":"uint256"}],"name":"PresetRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"binStep","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"baseFactor","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"filterPeriod","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"decayPeriod","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"reductionFactor","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"variableFeeControl","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"protocolShare","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"maxVolatilityAccumulated","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"sampleLifetime","type":"uint256"}],"name":"PresetSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"contract IERC20","name":"quoteAsset","type":"address"}],"name":"QuoteAssetAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"contract IERC20","name":"quoteAsset","type":"address"}],"name":"QuoteAssetRemoved","type":"event"},{"inputs":[],"name":"LBPairImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_BIN_STEP","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_PROTOCOL_SHARE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_BIN_STEP","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_quoteAsset","type":"address"}],"name":"addQuoteAsset","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allLBPairs","outputs":[{"internalType":"contract ILBPair","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"becomeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"},{"internalType":"uint24","name":"_activeId","type":"uint24"},{"internalType":"uint16","name":"_binStep","type":"uint16"}],"name":"createLBPair","outputs":[{"internalType":"contract ILBPair","name":"_LBPair","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"creationUnlocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"flashLoanFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILBPair","name":"_LBPair","type":"address"}],"name":"forceDecay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllBinSteps","outputs":[{"internalType":"uint256[]","name":"presetsBinStep","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"}],"name":"getAllLBPairs","outputs":[{"components":[{"internalType":"uint16","name":"binStep","type":"uint16"},{"internalType":"contract ILBPair","name":"LBPair","type":"address"},{"internalType":"bool","name":"createdByOwner","type":"bool"},{"internalType":"bool","name":"ignoredForRouting","type":"bool"}],"internalType":"struct ILBFactory.LBPairInformation[]","name":"LBPairsAvailable","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenA","type":"address"},{"internalType":"contract IERC20","name":"_tokenB","type":"address"},{"internalType":"uint256","name":"_binStep","type":"uint256"}],"name":"getLBPairInformation","outputs":[{"components":[{"internalType":"uint16","name":"binStep","type":"uint16"},{"internalType":"contract ILBPair","name":"LBPair","type":"address"},{"internalType":"bool","name":"createdByOwner","type":"bool"},{"internalType":"bool","name":"ignoredForRouting","type":"bool"}],"internalType":"struct ILBFactory.LBPairInformation","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNumberOfLBPairs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNumberOfQuoteAssets","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_binStep","type":"uint16"}],"name":"getPreset","outputs":[{"internalType":"uint256","name":"baseFactor","type":"uint256"},{"internalType":"uint256","name":"filterPeriod","type":"uint256"},{"internalType":"uint256","name":"decayPeriod","type":"uint256"},{"internalType":"uint256","name":"reductionFactor","type":"uint256"},{"internalType":"uint256","name":"variableFeeControl","type":"uint256"},{"internalType":"uint256","name":"protocolShare","type":"uint256"},{"internalType":"uint256","name":"maxVolatilityAccumulated","type":"uint256"},{"internalType":"uint256","name":"sampleLifetime","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getQuoteAsset","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_token","type":"address"}],"name":"isQuoteAsset","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_binStep","type":"uint16"}],"name":"removePreset","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_quoteAsset","type":"address"}],"name":"removeQuoteAsset","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"revokePendingOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_locked","type":"bool"}],"name":"setFactoryLockedState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeRecipient","type":"address"}],"name":"setFeeRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"},{"internalType":"uint16","name":"_binStep","type":"uint16"},{"internalType":"uint16","name":"_baseFactor","type":"uint16"},{"internalType":"uint16","name":"_filterPeriod","type":"uint16"},{"internalType":"uint16","name":"_decayPeriod","type":"uint16"},{"internalType":"uint16","name":"_reductionFactor","type":"uint16"},{"internalType":"uint24","name":"_variableFeeControl","type":"uint24"},{"internalType":"uint16","name":"_protocolShare","type":"uint16"},{"internalType":"uint24","name":"_maxVolatilityAccumulated","type":"uint24"}],"name":"setFeesParametersOnPair","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_flashLoanFee","type":"uint256"}],"name":"setFlashLoanFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"},{"internalType":"uint256","name":"_binStep","type":"uint256"},{"internalType":"bool","name":"_ignored","type":"bool"}],"name":"setLBPairIgnored","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_LBPairImplementation","type":"address"}],"name":"setLBPairImplementation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"pendingOwner_","type":"address"}],"name":"setPendingOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_binStep","type":"uint16"},{"internalType":"uint16","name":"_baseFactor","type":"uint16"},{"internalType":"uint16","name":"_filterPeriod","type":"uint16"},{"internalType":"uint16","name":"_decayPeriod","type":"uint16"},{"internalType":"uint16","name":"_reductionFactor","type":"uint16"},{"internalType":"uint24","name":"_variableFeeControl","type":"uint24"},{"internalType":"uint16","name":"_protocolShare","type":"uint16"},{"internalType":"uint24","name":"_maxVolatilityAccumulated","type":"uint24"},{"internalType":"uint16","name":"_sampleLifetime","type":"uint16"}],"name":"setPreset","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

    #joe facotry
    def get_number_of_lb_pairs(_web3:Web3,_factory_address):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.getNumberOfLBPairs().call()

    def get_number_of_quote_assets(_web3:Web3,_factory_address):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.getNumberOfQuoteAssets().call()

    def get_quote_asset(_web3:Web3,_factory_address,_index):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.getQuoteAsset(_index).call()

    def is_quote_asset(_web3:Web3,_factory_address,_address:str):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.isQuoteAsset(_address).call()

    def get_pair_information(_web3:Web3,_factory_address,_token_a:str,_token_b:str,_bin_step):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.getLBPairInformation(_token_a,_token_b,_bin_step).call()

    def get_all_lb_pairs(_web3:Web3,_factory_address,_token_a:str,_token_b:str):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.getAllLBPairs(_token_a,_token_b).call()

    def get_all_bin_steps(_web3:Web3,_factory_address):
        return _web3.eth.contract(address=_factory_address, abi=JoeV2Factory.joe_factory_v2_abi).functions.getAllBinSteps().call()

class JoeV2Quote:
    joe_quote_v2_abi='[{"inputs":[{"internalType":"address","name":"_routerV2","type":"address"},{"internalType":"address","name":"_factoryV1","type":"address"},{"internalType":"address","name":"_factoryV2","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"bp","type":"uint256"}],"name":"BinHelper__BinStepOverflows","type":"error"},{"inputs":[],"name":"BinHelper__IdOverflows","type":"error"},{"inputs":[],"name":"JoeLibrary__AddressZero","type":"error"},{"inputs":[],"name":"JoeLibrary__IdenticalAddresses","type":"error"},{"inputs":[],"name":"JoeLibrary__InsufficientAmount","type":"error"},{"inputs":[],"name":"JoeLibrary__InsufficientLiquidity","type":"error"},{"inputs":[],"name":"LBQuoter_InvalidLength","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"},{"internalType":"int256","name":"y","type":"int256"}],"name":"Math128x128__PowerUnderflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"prod1","type":"uint256"},{"internalType":"uint256","name":"denominator","type":"uint256"}],"name":"Math512Bits__MulDivOverflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"prod1","type":"uint256"},{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"Math512Bits__MulShiftOverflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"Math512Bits__OffsetOverflows","type":"error"},{"inputs":[],"name":"factoryV1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factoryV2","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_route","type":"address[]"},{"internalType":"uint256","name":"_amountIn","type":"uint256"}],"name":"findBestPathFromAmountIn","outputs":[{"components":[{"internalType":"address[]","name":"route","type":"address[]"},{"internalType":"address[]","name":"pairs","type":"address[]"},{"internalType":"uint256[]","name":"binSteps","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"uint256[]","name":"virtualAmountsWithoutSlippage","type":"uint256[]"},{"internalType":"uint256[]","name":"fees","type":"uint256[]"}],"internalType":"struct LBQuoter.Quote","name":"quote","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_route","type":"address[]"},{"internalType":"uint256","name":"_amountOut","type":"uint256"}],"name":"findBestPathFromAmountOut","outputs":[{"components":[{"internalType":"address[]","name":"route","type":"address[]"},{"internalType":"address[]","name":"pairs","type":"address[]"},{"internalType":"uint256[]","name":"binSteps","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"uint256[]","name":"virtualAmountsWithoutSlippage","type":"uint256[]"},{"internalType":"uint256[]","name":"fees","type":"uint256[]"}],"internalType":"struct LBQuoter.Quote","name":"quote","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"routerV2","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'

    #return quote
    #    struct Quote {
    #     address[] route; in token 在前
    #     address[] pairs;
    #     uint256[] binSteps;
    #     uint256[] amounts; 数组,顺序与路径一致
    #     uint256[] virtualAmountsWithoutSlippage;
    #     uint256[] fees;
    # }
    def find_best_path_for_amount_in(_web3:Web3,_quote_address,_quote_abi,_path,_amount_in):
        return _web3.eth.contract(address=_quote_address,abi=_quote_abi).functions.findBestPathFromAmountIn(_path,_amount_in).call()
    #return quote
    #    struct Quote {
    #     address[] route; out token在前
    #     address[] pairs;
    #     uint256[] binSteps;
    #     uint256[] amounts;
    #     uint256[] virtualAmountsWithoutSlippage;
    #     uint256[] fees;
    # }
    def find_best_path_for_amount_out(_web3:Web3,_quote_address,_quote_abi,_path,_amount_out):
        return _web3.eth.contract(address=_quote_address,abi=_quote_abi).functions.findBestPathFromAmountIn(_path,_amount_out).call()


class JoeV2Erc20:
    joe_erc20_abi='[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]'  

class JoeV2Route:
    joe_route_v2_abi=json.loads('[{"inputs":[{"internalType":"contract ILBFactory","name":"_factory","type":"address"},{"internalType":"contract IJoeFactory","name":"_oldFactory","type":"address"},{"internalType":"contract IWAVAX","name":"_wavax","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"bp","type":"uint256"}],"name":"BinHelper__BinStepOverflows","type":"error"},{"inputs":[],"name":"BinHelper__IdOverflows","type":"error"},{"inputs":[],"name":"JoeLibrary__InsufficientAmount","type":"error"},{"inputs":[],"name":"JoeLibrary__InsufficientLiquidity","type":"error"},{"inputs":[{"internalType":"uint256","name":"amountXMin","type":"uint256"},{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountYMin","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"}],"name":"LBRouter__AmountSlippageCaught","type":"error"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"LBRouter__BinReserveOverflows","type":"error"},{"inputs":[],"name":"LBRouter__BrokenSwapSafetyCheck","type":"error"},{"inputs":[{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"currentTimestamp","type":"uint256"}],"name":"LBRouter__DeadlineExceeded","type":"error"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LBRouter__FailedToSendAVAX","type":"error"},{"inputs":[{"internalType":"uint256","name":"idDesired","type":"uint256"},{"internalType":"uint256","name":"idSlippage","type":"uint256"}],"name":"LBRouter__IdDesiredOverflows","type":"error"},{"inputs":[{"internalType":"int256","name":"id","type":"int256"}],"name":"LBRouter__IdOverflows","type":"error"},{"inputs":[{"internalType":"uint256","name":"activeIdDesired","type":"uint256"},{"internalType":"uint256","name":"idSlippage","type":"uint256"},{"internalType":"uint256","name":"activeId","type":"uint256"}],"name":"LBRouter__IdSlippageCaught","type":"error"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"LBRouter__InsufficientAmountOut","type":"error"},{"inputs":[{"internalType":"address","name":"wrongToken","type":"address"}],"name":"LBRouter__InvalidTokenPath","type":"error"},{"inputs":[],"name":"LBRouter__LengthsMismatch","type":"error"},{"inputs":[{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"}],"name":"LBRouter__MaxAmountInExceeded","type":"error"},{"inputs":[],"name":"LBRouter__NotFactoryOwner","type":"error"},{"inputs":[{"internalType":"address","name":"tokenX","type":"address"},{"internalType":"address","name":"tokenY","type":"address"},{"internalType":"uint256","name":"binStep","type":"uint256"}],"name":"LBRouter__PairNotCreated","type":"error"},{"inputs":[],"name":"LBRouter__SenderIsNotWAVAX","type":"error"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"LBRouter__SwapOverflows","type":"error"},{"inputs":[{"internalType":"uint256","name":"excess","type":"uint256"}],"name":"LBRouter__TooMuchTokensIn","type":"error"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"reserve","type":"uint256"}],"name":"LBRouter__WrongAmounts","type":"error"},{"inputs":[{"internalType":"address","name":"tokenX","type":"address"},{"internalType":"address","name":"tokenY","type":"address"},{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"},{"internalType":"uint256","name":"msgValue","type":"uint256"}],"name":"LBRouter__WrongAvaxLiquidityParameters","type":"error"},{"inputs":[],"name":"LBRouter__WrongTokenOrder","type":"error"},{"inputs":[],"name":"Math128x128__LogUnderflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"},{"internalType":"int256","name":"y","type":"int256"}],"name":"Math128x128__PowerUnderflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"prod1","type":"uint256"},{"internalType":"uint256","name":"denominator","type":"uint256"}],"name":"Math512Bits__MulDivOverflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"prod1","type":"uint256"},{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"Math512Bits__MulShiftOverflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"Math512Bits__OffsetOverflows","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds128Bits","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds40Bits","type":"error"},{"inputs":[],"name":"TokenHelper__CallFailed","type":"error"},{"inputs":[],"name":"TokenHelper__NonContract","type":"error"},{"inputs":[],"name":"TokenHelper__TransferFailed","type":"error"},{"inputs":[{"components":[{"internalType":"contract IERC20","name":"tokenX","type":"address"},{"internalType":"contract IERC20","name":"tokenY","type":"address"},{"internalType":"uint256","name":"binStep","type":"uint256"},{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"},{"internalType":"uint256","name":"amountXMin","type":"uint256"},{"internalType":"uint256","name":"amountYMin","type":"uint256"},{"internalType":"uint256","name":"activeIdDesired","type":"uint256"},{"internalType":"uint256","name":"idSlippage","type":"uint256"},{"internalType":"int256[]","name":"deltaIds","type":"int256[]"},{"internalType":"uint256[]","name":"distributionX","type":"uint256[]"},{"internalType":"uint256[]","name":"distributionY","type":"uint256[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"internalType":"struct ILBRouter.LiquidityParameters","name":"_liquidityParameters","type":"tuple"}],"name":"addLiquidity","outputs":[{"internalType":"uint256[]","name":"depositIds","type":"uint256[]"},{"internalType":"uint256[]","name":"liquidityMinted","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"contract IERC20","name":"tokenX","type":"address"},{"internalType":"contract IERC20","name":"tokenY","type":"address"},{"internalType":"uint256","name":"binStep","type":"uint256"},{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"},{"internalType":"uint256","name":"amountXMin","type":"uint256"},{"internalType":"uint256","name":"amountYMin","type":"uint256"},{"internalType":"uint256","name":"activeIdDesired","type":"uint256"},{"internalType":"uint256","name":"idSlippage","type":"uint256"},{"internalType":"int256[]","name":"deltaIds","type":"int256[]"},{"internalType":"uint256[]","name":"distributionX","type":"uint256[]"},{"internalType":"uint256[]","name":"distributionY","type":"uint256[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"internalType":"struct ILBRouter.LiquidityParameters","name":"_liquidityParameters","type":"tuple"}],"name":"addLiquidityAVAX","outputs":[{"internalType":"uint256[]","name":"depositIds","type":"uint256[]"},{"internalType":"uint256[]","name":"liquidityMinted","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"},{"internalType":"uint24","name":"_activeId","type":"uint24"},{"internalType":"uint16","name":"_binStep","type":"uint16"}],"name":"createLBPair","outputs":[{"internalType":"contract ILBPair","name":"pair","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"contract ILBFactory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILBPair","name":"_LBPair","type":"address"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"getIdFromPrice","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILBPair","name":"_LBPair","type":"address"},{"internalType":"uint24","name":"_id","type":"uint24"}],"name":"getPriceFromId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILBPair","name":"_LBPair","type":"address"},{"internalType":"uint256","name":"_amountOut","type":"uint256"},{"internalType":"bool","name":"_swapForY","type":"bool"}],"name":"getSwapIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"feesIn","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILBPair","name":"_LBPair","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"bool","name":"_swapForY","type":"bool"}],"name":"getSwapOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"feesIn","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"oldFactory","outputs":[{"internalType":"contract IJoeFactory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"},{"internalType":"uint16","name":"_binStep","type":"uint16"},{"internalType":"uint256","name":"_amountXMin","type":"uint256"},{"internalType":"uint256","name":"_amountYMin","type":"uint256"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_token","type":"address"},{"internalType":"uint16","name":"_binStep","type":"uint16"},{"internalType":"uint256","name":"_amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"_amountAVAXMin","type":"uint256"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"address payable","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"removeLiquidityAVAX","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountAVAX","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountOut","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapAVAXForExactTokens","outputs":[{"internalType":"uint256[]","name":"amountsIn","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountOutMin","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapExactAVAXForTokens","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountOutMin","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapExactAVAXForTokensSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMinAVAX","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address payable","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapExactTokensForAVAX","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMinAVAX","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address payable","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapExactTokensForAVAXSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMin","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountIn","type":"uint256"},{"internalType":"uint256","name":"_amountOutMin","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountAVAXOut","type":"uint256"},{"internalType":"uint256","name":"_amountInMax","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address payable","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapTokensForExactAVAX","outputs":[{"internalType":"uint256[]","name":"amountsIn","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amountOut","type":"uint256"},{"internalType":"uint256","name":"_amountInMax","type":"uint256"},{"internalType":"uint256[]","name":"_pairBinSteps","type":"uint256[]"},{"internalType":"contract IERC20[]","name":"_tokenPath","type":"address[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amountsIn","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"sweep","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ILBToken","name":"_lbToken","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"}],"name":"sweepLBToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"wavax","outputs":[{"internalType":"contract IWAVAX","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')

    def get_id_from_price(_web3:Web3,_route_address:str,_route_abi,_lb_pair,_price):
        return _web3.eth.contract(address=_route_address, abi=_route_abi).functions.getIdFromPrice(_lb_pair,_price).call()

    def get_price_from_id(_web3:Web3,_route_address:str,_route_abi,_lb_pair,_id):
        return _web3.eth.contract(address=_route_address, abi=_route_abi).functions.getPriceFromId(_lb_pair,_id).call()

    #return [amount_in,fee]
    def get_swap_in(_web3:Web3,_route_address:str,_route_abi:str,_lb_pair,_amount_out,_swap_for_y:bool):
        return _web3.eth.contract(address=_route_address, abi=_route_abi).functions.getSwapIn(_lb_pair,_amount_out,_swap_for_y).call()
    
    #return [amount_out,fee]
    def get_swap_out(_web3:Web3,_route_address:str,_route_abi:str,_lb_pair,_amount_in,_swap_for_y:bool):
        return _web3.eth.contract(address=_route_address, abi=_route_abi).functions.getSwapOut(_lb_pair,_amount_in,_swap_for_y).call()

    def swap_exact_tokens_for_tokens(_web3:Web3,_route_address:str,_route_abi,
                                     _amount_in,_amount_out_min,_pair_bin_steps,_token_path,_to,_deadline,
                                     _public_key,_private_key):
        nonce=_web3.eth.get_transaction_count(_public_key)
        route_contract=_web3.eth.contract(address=_route_address, abi=_route_abi)
        swap_function=route_contract.functions.swapExactTokensForTokens(_amount_in,_amount_out_min,_pair_bin_steps,_token_path,_to,_deadline)
        params={
            'from': _public_key,
            'value': 0,
            'nonce': nonce,
            'type': '0x2'
        }
        signed_transaction=_web3.eth.account.sign_transaction(swap_function.build_transaction(params),private_key=_private_key)
        response=_web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        return Web3.to_hex(response)
    
    def swap_tokens_for_exact_tokens(_web3:Web3,_route_address:str,_route_abi,
                                     _amount_out,_amount_in_max,_pair_bin_steps,_token_path,_to,_deadline,
                                     _public_key,_private_key):
        nonce=_web3.eth.get_transaction_count(_public_key)
        route_contract=_web3.eth.contract(address=_route_address, abi=_route_abi)
        swap_function=route_contract.functions.swapTokensForExactTokens(_amount_out,_amount_in_max,_pair_bin_steps,_token_path,_to,_deadline)
        params={
            'from': _public_key,
            'value': 0,
            'nonce': nonce,
            'type': '0x2'
        }
        signed_transaction=_web3.eth.account.sign_transaction(swap_function.build_transaction(params),private_key=_private_key)
        response=_web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        return Web3.to_hex(response)

class JoeV2Pair:

    joe_pair_v2_abi=json.loads('[{"inputs":[{"internalType":"contract ILBFactory","name":"_factory","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"bp","type":"uint256"}],"name":"BinHelper__BinStepOverflows","type":"error"},{"inputs":[],"name":"BinHelper__IdOverflows","type":"error"},{"inputs":[],"name":"LBPair__AddressZero","type":"error"},{"inputs":[],"name":"LBPair__AddressZeroOrThis","type":"error"},{"inputs":[],"name":"LBPair__AlreadyInitialized","type":"error"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"LBPair__CompositionFactorFlawed","type":"error"},{"inputs":[],"name":"LBPair__DistributionsOverflow","type":"error"},{"inputs":[],"name":"LBPair__FlashLoanCallbackFailed","type":"error"},{"inputs":[],"name":"LBPair__FlashLoanInvalidBalance","type":"error"},{"inputs":[],"name":"LBPair__FlashLoanInvalidToken","type":"error"},{"inputs":[],"name":"LBPair__InsufficientAmounts","type":"error"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"LBPair__InsufficientLiquidityBurned","type":"error"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"LBPair__InsufficientLiquidityMinted","type":"error"},{"inputs":[],"name":"LBPair__OnlyFactory","type":"error"},{"inputs":[{"internalType":"address","name":"feeRecipient","type":"address"},{"internalType":"address","name":"sender","type":"address"}],"name":"LBPair__OnlyFeeRecipient","type":"error"},{"inputs":[],"name":"LBPair__OnlyStrictlyIncreasingId","type":"error"},{"inputs":[{"internalType":"uint256","name":"newSize","type":"uint256"},{"internalType":"uint256","name":"oracleSize","type":"uint256"}],"name":"LBPair__OracleNewSizeTooSmall","type":"error"},{"inputs":[],"name":"LBPair__WrongLengths","type":"error"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LBToken__BurnExceedsBalance","type":"error"},{"inputs":[],"name":"LBToken__BurnFromAddress0","type":"error"},{"inputs":[{"internalType":"uint256","name":"accountsLength","type":"uint256"},{"internalType":"uint256","name":"idsLength","type":"uint256"}],"name":"LBToken__LengthMismatch","type":"error"},{"inputs":[],"name":"LBToken__MintToAddress0","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"LBToken__SelfApproval","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"LBToken__SpenderNotApproved","type":"error"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LBToken__TransferExceedsBalance","type":"error"},{"inputs":[],"name":"LBToken__TransferFromOrToAddress0","type":"error"},{"inputs":[],"name":"LBToken__TransferToSelf","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"},{"internalType":"int256","name":"y","type":"int256"}],"name":"Math128x128__PowerUnderflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"prod1","type":"uint256"},{"internalType":"uint256","name":"denominator","type":"uint256"}],"name":"Math512Bits__MulDivOverflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"prod1","type":"uint256"},{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"Math512Bits__MulShiftOverflow","type":"error"},{"inputs":[{"internalType":"uint256","name":"offset","type":"uint256"}],"name":"Math512Bits__OffsetOverflows","type":"error"},{"inputs":[{"internalType":"uint256","name":"_minTimestamp","type":"uint256"},{"internalType":"uint256","name":"_lookUpTimestamp","type":"uint256"}],"name":"Oracle__LookUpTimestampTooOld","type":"error"},{"inputs":[],"name":"Oracle__NotInitialized","type":"error"},{"inputs":[],"name":"ReentrancyGuardUpgradeable__AlreadyInitialized","type":"error"},{"inputs":[],"name":"ReentrancyGuardUpgradeable__ReentrantCall","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds112Bits","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds128Bits","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds24Bits","type":"error"},{"inputs":[{"internalType":"uint256","name":"x","type":"uint256"}],"name":"SafeCast__Exceeds40Bits","type":"error"},{"inputs":[],"name":"TokenHelper__CallFailed","type":"error"},{"inputs":[],"name":"TokenHelper__NonContract","type":"error"},{"inputs":[],"name":"TokenHelper__TransferFailed","type":"error"},{"inputs":[],"name":"TreeMath__ErrorDepthSearch","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"feesX","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"feesY","type":"uint256"}],"name":"CompositionFee","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountX","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountY","type":"uint256"}],"name":"DepositedToBin","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountX","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountY","type":"uint256"}],"name":"FeesCollected","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"contract ILBFlashLoanCallback","name":"receiver","type":"address"},{"indexed":false,"internalType":"contract IERC20","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"FlashLoan","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"previousSize","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newSize","type":"uint256"}],"name":"OracleSizeIncreased","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountX","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountY","type":"uint256"}],"name":"ProtocolFeesCollected","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"bool","name":"swapForY","type":"bool"},{"indexed":false,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOut","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"volatilityAccumulated","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"fees","type":"uint256"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountX","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountY","type":"uint256"}],"name":"WithdrawnFromBin","type":"event"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"_accounts","type":"address[]"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"batchBalances","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"},{"internalType":"address","name":"_to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"}],"name":"collectFees","outputs":[{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"collectProtocolFees","outputs":[{"internalType":"uint128","name":"amountX","type":"uint128"},{"internalType":"uint128","name":"amountY","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"contract ILBFactory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeParameters","outputs":[{"components":[{"internalType":"uint16","name":"binStep","type":"uint16"},{"internalType":"uint16","name":"baseFactor","type":"uint16"},{"internalType":"uint16","name":"filterPeriod","type":"uint16"},{"internalType":"uint16","name":"decayPeriod","type":"uint16"},{"internalType":"uint16","name":"reductionFactor","type":"uint16"},{"internalType":"uint24","name":"variableFeeControl","type":"uint24"},{"internalType":"uint16","name":"protocolShare","type":"uint16"},{"internalType":"uint24","name":"maxVolatilityAccumulated","type":"uint24"},{"internalType":"uint24","name":"volatilityAccumulated","type":"uint24"},{"internalType":"uint24","name":"volatilityReference","type":"uint24"},{"internalType":"uint24","name":"indexRef","type":"uint24"},{"internalType":"uint40","name":"time","type":"uint40"}],"internalType":"struct FeeHelper.FeeParameters","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint24","name":"_id","type":"uint24"},{"internalType":"bool","name":"_swapForY","type":"bool"}],"name":"findFirstNonEmptyBinId","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ILBFlashLoanCallback","name":"_receiver","type":"address"},{"internalType":"contract IERC20","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"flashLoan","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"forceDecay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"_id","type":"uint24"}],"name":"getBin","outputs":[{"internalType":"uint256","name":"reserveX","type":"uint256"},{"internalType":"uint256","name":"reserveY","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getGlobalFees","outputs":[{"internalType":"uint128","name":"feesXTotal","type":"uint128"},{"internalType":"uint128","name":"feesYTotal","type":"uint128"},{"internalType":"uint128","name":"feesXProtocol","type":"uint128"},{"internalType":"uint128","name":"feesYProtocol","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getOracleParameters","outputs":[{"internalType":"uint256","name":"oracleSampleLifetime","type":"uint256"},{"internalType":"uint256","name":"oracleSize","type":"uint256"},{"internalType":"uint256","name":"oracleActiveSize","type":"uint256"},{"internalType":"uint256","name":"oracleLastTimestamp","type":"uint256"},{"internalType":"uint256","name":"oracleId","type":"uint256"},{"internalType":"uint256","name":"min","type":"uint256"},{"internalType":"uint256","name":"max","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_timeDelta","type":"uint256"}],"name":"getOracleSampleFrom","outputs":[{"internalType":"uint256","name":"cumulativeId","type":"uint256"},{"internalType":"uint256","name":"cumulativeVolatilityAccumulated","type":"uint256"},{"internalType":"uint256","name":"cumulativeBinCrossed","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReservesAndId","outputs":[{"internalType":"uint256","name":"reserveX","type":"uint256"},{"internalType":"uint256","name":"reserveY","type":"uint256"},{"internalType":"uint256","name":"activeId","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_newLength","type":"uint16"}],"name":"increaseOracleLength","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"_tokenX","type":"address"},{"internalType":"contract IERC20","name":"_tokenY","type":"address"},{"internalType":"uint24","name":"_activeId","type":"uint24"},{"internalType":"uint16","name":"_sampleLifetime","type":"uint16"},{"internalType":"bytes32","name":"_packedFeeParameters","type":"bytes32"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_spender","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_distributionX","type":"uint256[]"},{"internalType":"uint256[]","name":"_distributionY","type":"uint256[]"},{"internalType":"address","name":"_to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256[]","name":"liquidityMinted","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"}],"name":"pendingFees","outputs":[{"internalType":"uint256","name":"amountX","type":"uint256"},{"internalType":"uint256","name":"amountY","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256[]","name":"_ids","type":"uint256[]"},{"internalType":"uint256[]","name":"_amounts","type":"uint256[]"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"bool","name":"_approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_packedFeeParameters","type":"bytes32"}],"name":"setFeesParameters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"_interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_swapForY","type":"bool"},{"internalType":"address","name":"_to","type":"address"}],"name":"swap","outputs":[{"internalType":"uint256","name":"amountXOut","type":"uint256"},{"internalType":"uint256","name":"amountYOut","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"tokenX","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenY","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_id","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

    # returns (uint256 reserveX, uint256 reserveY, uint256 activeId)
    def get_reserve_and_id(_web3:Web3,_pair_address:str):
        pair_contract=_web3.eth.contract(address=_pair_address, abi=JoeV2Pair.joe_pair_v2_abi)
        return pair_contract.functions.getReservesAndId().call()

    # function getGlobalFees() external view override returns (uint256 feesXTotal, uint256 feesYTotal, uint256 feesXProtocol, uint256 feesYProtocol)
    def get_global_fee(_web3:Web3,_pair_address:str):
        pair_contract=_web3.eth.contract(address=_pair_address, abi=JoeV2Pair.joe_pair_v2_abi)
        return pair_contract.functions.getGlobalFees().call()

    # function findFirstNonEmptyBinId(uint24 _id, bool _swapForY) external view override returns (uint24)
    def find_first_non_empty_bin_id(_web3:Web3,_pair_address:str,_id,_swap_for_y):
        pair_contract=_web3.eth.contract(address=_pair_address, abi=JoeV2Pair.joe_pair_v2_abi)
        return pair_contract.functions.findFirstNonEmptyBinId(_id,_swap_for_y).call()

    # function getBin(uint24 _id) external view override returns (uint256 reserveX, uint256 reserveY)
    def get_bin(_web3:Web3,_pair_address:str,_id):
        pair_contract=_web3.eth.contract(address=_pair_address, abi=JoeV2Pair.joe_pair_v2_abi)
        return pair_contract.functions.getBin(_id).call()

    # function swap(bool _swapForY, address _to) external override nonReentrant returns (uint256 amountXOut, uint256 amountYOut)
    def swap(_web3:Web3,_pair_address:str,_swap_for_y,_to):
        pair_contract=_web3.eth.contract(address=_pair_address, abi=JoeV2Pair.joe_pair_v2_abi)
        return pair_contract.functions.swap(_swap_for_y,_to).call()