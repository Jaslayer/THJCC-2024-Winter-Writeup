from sage.all import *
from Crypto.Util.number import long_to_bytes
from data import r, M, seeds

# Set up the LLL matrix
B = Matrix(ZZ, 8, 8)
K = floor(sqrt(M))
R = Integers(M)

# Fill in the matrix
for i in range(6):
    B[i+1, 0] = R(seeds[i]*pow(seeds[6],-1,M))
    B[i+1, i+1] = -1
B[0, 0] = M
B[7, 0] = R(r*pow(seeds[6],-1,M))
B[7, 7] = K

# Apply LLL
L = B.LLL()

# Extract solutions
print(f"{L[-1] = }")
'''
L[-1] = [103279413057035146916876895,     101,      51,      55,      54,      97,      98, K]
      = [                       NAME, SIGN[0], SIGN[1], SIGN[2], SIGN[3], SIGN[4], SIGN[5], K]
'''
NAME, *SIGN = L[-1][:-2]
flag = long_to_bytes(NAME).decode() + "".join(chr(c) for c in SIGN)
print(flag)