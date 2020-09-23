from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:

    if (x & 1 == 1):
        n = x^(0xFFFFFFFFFFFFFFFF)
        n &= ~(n-1)
        n ^= n>>1
        return (x ^ n)
    else:
        n = x
        n &= ~(n-1)
        n ^= n>>1
        return (x ^ n)

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
