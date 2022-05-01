from web3 import Web3
from decouple import config

#INFURA_URL=''https://mainnet.infura.io/v3/c6246e3831ab49fdb3217fe0f2623268


#infura_url = config('INFURA_URL')
infura_url = "https://mainnet.infura.io/v3/c6246e3831ab49fdb3217fe0f2623268"
print(infura_url)

#HttpProvider
w3 = Web3(Web3.HTTPProvider(infura_url))
res = w3.isConnected()
print(res)

latest_block = w3.eth.getBlock('latest')
print(latest_block)