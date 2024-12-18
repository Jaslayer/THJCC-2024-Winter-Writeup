from Crypto.Util.number import *
with open("output.txt", "r") as f:
    lines = f.read().splitlines()

flag_bytearrays = [bytes.fromhex(line) for line in lines]

result = flag_bytearrays[0]
for array in flag_bytearrays[1:]:
    result = [a ^ b for a, b in zip(result, array)]
print("".join([chr(c) for c in result]))
