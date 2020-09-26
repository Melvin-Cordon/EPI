from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
        
    def reverse(x: int) -> int:

        rev = 0
        neg = 1
        if x < 0:
            neg = -1
            x = x*neg

        while x > 0:
            rev *= 10
            rev += x%10
            x //= 10
        return rev*neg

    if x == reverse(x):
        return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
