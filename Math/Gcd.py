import time
#beer-sheva lecture

def naive_gcd(x, y):
    gcd = 0
    for i in range(1, (x if x < y else y) + 1):
        if not (x % i or y % i):
            gcd = i
    return gcd


def recursive_gcd(x, y):
    if y == 0:
        return x
    else:
        return recursive_gcd(y, x % y)


def better_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


from math import gcd as math_gcd

for func in [naive_gcd, recursive_gcd, better_gcd, math_gcd]:
    t = time.perf_counter()
    res = func(1529, 1265)
    t = time.perf_counter() - t
    print("the function {} result is {}, it ran for {}".format(func.__name__, res, t))
