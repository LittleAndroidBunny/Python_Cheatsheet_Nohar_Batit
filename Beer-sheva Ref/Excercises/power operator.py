
import time


def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print("{} took {:.8f} s".format(func.__name__, (t2 - t1)))
        return res

    return wrapper


@print_timing
def power1(num, power):
    # loop implementation of power operator
    res = 1
    for i in range(power):
        res *= num
    return res


def power2(num, power):
    if power == 0:
        return 1
    return num*power2(num, power-1)


def power3(num, power):
    if power == 0:
        return 1
    if power % 2:
        return num*power3(num, power-1)
    tmp = power3(num, power/2)
    return tmp*tmp


print('power loop:')
print(power1(2, 100))

print('power recursive:')
t1 = time.time()
print(power2(2, 100))
t2 = time.time()
print("power2 took {:.8f} s".format( (t2 - t1)))

print('power recursive smart:')
t1 = time.time()
print(power3(2, 100))
t2 = time.time()
print("power3 took {:.8f} s".format( (t2 - t1)))


