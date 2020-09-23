from test_framework import generic_test

def swap_bits(x, i, j):
    """ O(1) """
    if (x >> i)&1 != (x >> j)&1:

        x ^= 1 << i
        x ^= 1 << j

    return x

def reverse_bits(x: int) -> int:

    for i in range(0,32,1):
        x = swap_bits(x, i, (63-i))
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
