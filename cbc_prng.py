""""
Cipher Block Chaining Algorithm
### I have yet explore the limitation toward unseen character in ASCII,
### It will display nothing if there are characters identified as unseen
### character. i.e. the message 131 -> converted to *\r* (unseen char)
"""

import random
from util import *
from prng import *

def decrypt(cipher_text, key, initial_vector, BLOCK_SIZE):
    random.seed(key)
    cipher_bins = text_to_bin(cipher_text)
    i = 0
    plain_bins = []
    last_block = initial_vector
    while cipher_bins != '':
        rand = PRNG(key)
        key = rand[:BLOCK_SIZE]
        cipher_bin = cipher_bins[:BLOCK_SIZE]
        temp = right_shift_cyclic(cipher_bin, 2)
        # print(temp, key)
        temp = xor_two_bins(temp, key, BLOCK_SIZE)
        temp = xor_two_bins(temp, last_block, BLOCK_SIZE)
        key = int(rand[-BLOCK_SIZE:], 2)
        last_block = cipher_bins[:BLOCK_SIZE]
        cipher_bins = cipher_bins[BLOCK_SIZE:]
        i += 1
        plain_bins.append(temp)

    return bins_to_string(plain_bins)

def encrypt(plain_text, key, initial_vector, BLOCK_SIZE):
    random.seed(key)
    last_block = initial_vector
    plain_bins = text_to_bin(plain_text)
    size = BLOCK_SIZE//8
    plain_bins = plain_bins + "00100000"*((size - (len(plain_bins)//8)%size)%size)
    print(len(plain_bins))

    cipher_bins = []
    while plain_bins != '':
        rand = PRNG(key)
        key = rand[:BLOCK_SIZE]
        plain_bin = plain_bins[:BLOCK_SIZE]
        temp = xor_two_bins(plain_bin, last_block, BLOCK_SIZE)
        temp = xor_two_bins(temp, key, BLOCK_SIZE)
        temp = left_shift_cyclic(temp, 2)
        last_block = temp
        key = int(rand[-BLOCK_SIZE:], 2)
        plain_bins = plain_bins[BLOCK_SIZE:]
        cipher_bins.append(temp)
    return bins_to_string(cipher_bins)

def main():
    BLOCK_SIZE = 32
    initial_vector = "0"*BLOCK_SIZE
    plain_text = "asdasdasdasd"
    key = 0
    print(plain_text)
    print()
    cipher_text = encrypt(plain_text, key, initial_vector)
    print(repr(cipher_text), len(cipher_text))
    print()
    plain_text = decrypt(cipher_text, key, initial_vector)
    print(plain_text)

if __name__ == "__main__":
    main()