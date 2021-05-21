import sys

SEED_SIZE  = 32
GENERATOR  = 79 
MODULUS    = 7919

FUNCTION_L = lambda x: x**2 - 2*x + 1


def function_H(first_half, second_half):
    mod_exp = bin(pow(GENERATOR, int(first_half, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)
    hard_core_bit = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i]))) % 2
    return mod_exp + second_half + str(hard_core_bit)


def function_G(initial_seed):
    binary_string = initial_seed
    result = ''
    for i in range(FUNCTION_L(SEED_SIZE)):
        mid = int(len(binary_string)/2)
        first_half = binary_string[:mid]
        second_half = binary_string[mid:]
        binary_string = function_H(first_half, second_half)
        result += binary_string[-1]
        binary_string = binary_string[:-1]
    return result


def PRNG(seed):
    seed = bin(seed).replace('0b', '').zfill(SEED_SIZE)
    output = function_G(seed)
    return output

if __name__ == "__main__":
    a = PRNG(1)
    print(a)
    print(len(a))