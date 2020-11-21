from bitcoin.rpc import RawProxy, InvalidParameterError, InvalidAddressOrKeyError

p = RawProxy()

raw_tx = None

while True:
    try:
        tx_id = raw_input('Enter transaction id: ')
        raw_tx = p.getrawtransaction(tx_id)
        break
    except InvalidParameterError:
        print("Invalid transaction id, please enter a 64 symbol hex")
    except InvalidAddressOrKeyError:
        print("Transaction not found, check it's id and try gain")

decoded_tx = p.decoderawtransaction(raw_tx)

input_sum = 0
output_sum = 0

for input in decoded_tx['vin']:
    input_tx_id = input['txid']
    raw_input_tx = p.getrawtransaction(input_tx_id)
    decoded_input_tx = p.decoderawtransaction(raw_input_tx)
    
    target_output = decoded_input_tx['vout'][input['vout']]
    input_sum += target_output['value']

for output in decoded_tx['vout']:
    output_sum += output['value']

print("%s %s" % ("Input sum:", input_sum))
print("%s %s" % ("Output sum:", output_sum))
print("%s %s" % ("Transaction cost:", input_sum - output_sum))