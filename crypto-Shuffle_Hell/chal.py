from random import *
from itertools import *
from pwn import *
import os
from secret import FLAG

def xor(a:bytes, b:bytes)->bytes:
    return bytes([x ^ y for (x, y) in zip(a, b)])

def shuffle(layer:list):
    for i in range(len(layer) - 1, 0, -1):
        j = randint(0, i)
        layer[i], layer[j] = layer[j], layer[i]
    return layer

def gen_shuffled_map(n:int):
    return shuffle(list(range(n)))

def encrypt(plain:bytes, key_a:bytes, key_b:bytes)->bytes:
    cipher = xor(plain, key_a)
    cipher = xor(cipher, key_b)
    return cipher

flag_size = len(FLAG) # 23
layers = [[os.urandom(flag_size) for _ in range(1337)] for _ in range(39)] #  39 * (1337*23bytes)
shuffled_mapX = [gen_shuffled_map(1337) for _ in range(39)] # (39*1337) 0~1336 random order
shuffled_mapY = [gen_shuffled_map(1337) for _ in range(39)]

for i in range(1337):
    cipher = FLAG # b'THJCC{AAAAAAAAfakeflag}'
    for j in range(39):
        x = shuffled_mapX[j][i]
        y = shuffled_mapY[j][i]
        cipher = encrypt(cipher, layers[j][x], layers[j][y]) # cipher ^= layers[j][X1] ^ layers[j][Y1]
    print(cipher.hex()) # FLAG ^ (keyX1 ^ keyX2 ^ ... ^ keyX39) ^ (keyY1 ^ keyY2 ^ ... ^ keyY39)
