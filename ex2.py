from bitcoin.rpc import RawProxy, JSONRPCError, InvalidParameterError
from bitcoin.core import lx, b2x, b2lx;
from bitcoin.core.serialize import Hash

p = RawProxy()

block_hash = None
while True:
    try:
        blockheight = int(raw_input("Enter block's height: "))
        block_hash = p.getblockhash(blockheight)
        break
    except ValueError:
        print("Invalid value, please enter an integer")
    except (InvalidParameterError, JSONRPCError, KeyError):
        print("Ivalid parameter, block with such height does not exist")

block = p.getblock(block_hash)
print(block_hash)

version_hex = block['versionHex']
prev_block_hash = block['previousblockhash'] if 'previousblockhash' in block else '0' * 64
merkle_root = block['merkleroot']
time = block['time']
diff_bitts = block['bits']
nonce = block['nonce']

print("%s %s" % ("\nBlock's hash:", block_hash))
print("\nProperties:")
print("%s %s" % ("Version hex:", version_hex))
print("%s %s" % ("Previous block hash:", prev_block_hash))
print("%s %s" % ("Merkle root:", merkle_root))
print("%s %s" % ("Timestamp:", time))
print("%s %s" % ("Difficulty hex:", diff_bitts))
print("%s %s" % ("Nonce:", nonce))

reversed_version_hex = b2x(lx(version_hex))
reversed_prev_block_hash = b2x(lx(prev_block_hash))
reversed_merkle_root = b2x(lx(merkle_root))
reversed_time_hex = b2x(lx("%08x" % time))
reversed_diff_bits = b2x(lx(diff_bitts))
reversed_nonce_hex = b2x(lx("%08x" % nonce));

print("\nTransformed properties")
print("%s %s" % ("Version hex little endian:", reversed_version_hex))
print("%s %s" % ("Previous block hash little endian:", reversed_prev_block_hash))
print("%s %s" % ("Merkle root little endian:", reversed_merkle_root))
print("%s %s" % ("Timestamp hex little endian:", reversed_time_hex))
print("%s %s" % ("Difficulty hex little endian:", reversed_diff_bits))
print("%s %s" % ("Nonce hex little endian:", reversed_nonce_hex))

header_str = (
    reversed_version_hex 
    + reversed_prev_block_hash 
    + reversed_merkle_root 
    + reversed_time_hex
    + reversed_diff_bits
    + reversed_nonce_hex
)

header_bytes = header_str.decode('hex')
block_hash_bytes_le = Hash(header_bytes)

computed_block_hash = b2lx(block_hash_bytes_le)
print("%s %s" % ("\nComputed block hash:", computed_block_hash))

if computed_block_hash == block_hash:
    print("Block's hash is valid!")
else:
    print("Block's hash is not valid!")
    print("%s %s" % ("Expected:", computed_block_hash))
    print("%s %s" % ("Actual:", block_hash))
print("")