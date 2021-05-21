""""
Cipher Block Chaining Algorithm
### I have yet explore the limitation toward unseen character in ASCII,
### It will display nothing if there are characters identified as unseen
### character. i.e. the message 131 -> converted to *\r* (unseen char)
"""

import random
from util import *


def decrypt(cipher_text, key, initial_vector):
    random.seed(key)
    cipher_bins = text_to_bin(cipher_text)

    plain_bins = []
    for i, cipher_bin in enumerate(cipher_bins):
        key = omit_0b(bin(int(random.random() * 256))).zfill(8)
        last_block = initial_vector if i == 0 else cipher_bins[i-1]
        temp = right_shift_cyclic(cipher_bin, 2)
        temp = xor_two_bins(temp, key)
        temp = xor_two_bins(temp, last_block)
        plain_bins.append(temp)

    return bins_to_string(plain_bins)

def encrypt(plain_text, key, initial_vector):
    random.seed(key)
    last_block = initial_vector
    plain_bins = text_to_bin(plain_text)

    cipher_bins = []
    for plain_bin in plain_bins:
        key = omit_0b(bin(int(random.random() * 256))).zfill(8)
        temp = xor_two_bins(plain_bin, last_block)
        temp = xor_two_bins(temp, key)
        temp = left_shift_cyclic(temp, 2)
        last_block = temp
        cipher_bins.append(temp)
        
    return bins_to_string(cipher_bins)

def main():
    initial_vector = "00000000"
    plain_text = "1a"
    key = 1
    cipher_text = encrypt(plain_text, key, initial_vector)
    print(cipher_text)
    plain_text = decrypt(cipher_text, key, initial_vector)
    print(plain_text)

if __name__ == "__main__":
    main()