#!/usr/bin/env python
from random import randint as r
from fractions import Fraction as f
from string import ascii_lowercase as abc

c_to_i = {c:i for i,c in enumerate(abc)}
i_to_c = {i:c for i,c in enumerate(abc)}

n = r(1,100)
d = r(1,100)

private_key = f(n,d)
public_key = f(d,n)

print("Public Key:",public_key,", Private Key:",private_key)

def encrypt(plaintext,key):
    cipher = []
    for c in plaintext:
        cipher.append(c_to_i[c] * key)
    return cipher

def decrypt(cipher,key):
    plaintext = []
    for i in cipher:
        plaintext.append(i_to_c[i * key])
    return ''.join(plaintext)

cipher = encrypt('rarrar',private_key)
plaintext = decrypt(cipher,public_key)
print(cipher)
print(plaintext)



