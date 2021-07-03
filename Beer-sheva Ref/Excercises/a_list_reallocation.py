import time


def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print("{} took {:.4f} s".format(func.__name__, (t2 - t1)))
        return res

    return wrapper


@print_timing
def realloc_ignorantly(size):
    result = []
    for i in range(size):
        result = result + [i]
    return result


@print_timing
def prealloc_array(size):
    result = [None] * size
    for i in range(size):
        result[i] = i
    return result


@print_timing
def realloc_array_by_appending(size):
    result = []
    for i in range(size):
        result.append(i)
    return result


@print_timing
def realloc_array_by_extending(size):
    result = []
    for i in range(size):
        result.extend([i])
    return result


n = 10 ** 5
z = realloc_ignorantly(n)
y = realloc_array_by_appending(n)
x = realloc_array_by_extending(n)
w = prealloc_array(n)
print(z == y == x == w)