# This script is part of tutorial number 3 of introduction of computer science for EE students at BGU.
# Topics, Comprehensive review of:
#   - loops
#   - conditionals
#   - strings
#   - introduce the input function
import math
from typing import List


def first_function(arg):
    """
    This is my first function.
    :param int arg: numeric value to be squared
    :return int: argument squared
    """
    return arg ** 2


x = 2
y = first_function(x)  # calling the function
print(y)
help(first_function)


# second_function(y)  # Will this work


def second_function(arg):
    return arg / 2


second_function(y)


# third function - type hints
def third_function(text: str) -> str:
    """
    The function removes all spaces from text
    :rtype: str
    :param str text: input text
    :return: input text without spaces
    """
    return text.replace(" ", "")


print(third_function('  ab cd '))


def element_wise_log(numeric_list: List[int]):
    """Returns a list of natural base log of argument list elements.
    If input has values<=0 returns None

    :rtype: float
    :param List[int] numeric_list: values to be computed
    :return: natural logarithm of elements
    """
    result = []
    for element in numeric_list:
        if element > 0:
            result.append(math.log(element))
        else:
            return
    return result


x = element_wise_log([1, 2, 3])
print(x)
y = element_wise_log([2, -5, 3])
print(y)
