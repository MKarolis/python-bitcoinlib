from bitcoin.rpc import RawProxy

p = RawProxy()
 
txid ="0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

raw_tx = p.getrawtransaction(txid)
print('raw tx ', raw_tx)

decoded_tx = p.decoderawtransaction(raw_tx)
print('decoded tx', decoded_tx)

for output in decoded_tx['vout']:
    print(output['scriptPubKey']['addresses'], output['value'])