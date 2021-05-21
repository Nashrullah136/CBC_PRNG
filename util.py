import re

def omit_0b(text: str) -> str:
    return re.sub("0b", "", text)


def text_to_bin(text: str) -> list:
    return ''.join([padding_at_beginning(omit_0b(bin(ord(char)))) for char in text])

def dec_to_bins(dec: int) -> str:
    return padding_at_beginning(omit_0b(bin(dec)))

def bin_to_dec(bin: str) -> int:
    return int(bin, 2)


def left_shift_cyclic(bins: str, n: int) -> str:
    return (bins[n:] + bins[:n])


def right_shift_cyclic(bins: str, n: int) -> str:
    pos = len(bins)-n
    return (bins[pos:] + bins[:pos])


def bins_to_string(cipher_bins: list) -> str:
    temp = r''.join(cipher_bins)
    string = []
    while temp != '':
        char = temp[:8]
        char = chr(bin_to_dec(char))
        string.append(char)
        temp = temp[8:]
    return r"".join(string)

def xor_two_bins(bins1: str, bins2: str, block_size: int) -> int:
    in_dec = bin_to_dec(bins1) ^ bin_to_dec(bins2)
    return dec_to_bins(in_dec).zfill(block_size)

def padding_at_beginning(bins: str) -> str:
    padding = "0" * (8-len(bins))
    return (padding + bins)