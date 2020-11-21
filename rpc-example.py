# `rpc_example.py` example
from bitcoin.rpc import RawProxy
from btc_utils import format_json
import json

# Create a connection to local Bitcoin Core node
p = RawProxy()

# Run the getblockchaininfo command, store the resulting data in info
info = p.getblockchaininfo()

# Retrieve the 'blocks' element from the info
print(info['blocks'])