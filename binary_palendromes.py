def binary_palendrome(num):
    """
    Determines if num is a binary palendrome.
    This converts a number (in any base but two) into it's binary representation. It then compares
    that binary number to the reverse of itself. It returns True if they match.

    >>> binary_palendrome(51)
    True
    >>> binary_palendrome(52)
    False

    """
    first = bin(num)
    if first[2] != first[-1]:
        return False
    else:
        second = first[:1:-1]

    return first == second


if __name__ == "__main__":
    import doctest
    doctest.testmod()
