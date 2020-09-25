from test_framework import generic_test


def reverse(x: int) -> int:

    rev = 0
    neg = 1
    if x < 0:
        neg = -1
        x = -x

    while x > 0:
        rev *= 10
        rev += x%10
        x //= 10
    return rev*neg


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
