from typing import Tuple


def is_prime(n: int) -> bool:
    """ The function check if the input is prime
    :return: True if the number is prime, False otherwise
    :param int n: a positive integer
    :rtype: bool
    """

    if n < 2:
        return False
    i = 2
    while i**2 <= n:
        if not n % i:
            return False
        i += 1
    return True


def goldbach_pair(n: int) -> Tuple[int, int]:
    """ The function receives an even integer greater than 2 and returns a Goldbach pair
    :param n: a positive even number greater than 2
    :return: a tuple of a Goldbach  pair
    :rtype: (int, int)
    """
    if n == 4:
        return 2, 2
    j = 1
    while j < n:
        if is_prime(j):
            if is_prime(n-j):
                return j, n-j
        j += 2
