from Crypto.Util.number import bytes_to_long
from secret import NAME, SIGN
from random import randint
assert(len(NAME)==11)
M=randint(2**8191, 2**8192)
seed=[randint(2**8191, 2**8192) for _ in range(7)]
r=0
for i in range(6):
    r=(r+SIGN[i]*seed[i])%M
r=r+bytes_to_long(NAME)*seed[6]%M
print(f"{r=}\n{M=}\n{seed=}")
