print("O(1):")
l = []  # add value to a list
l.append(1)
len(l)

print("O(n):")


def linear_algo(obj):  # print each item
    for item in obj:
        print(item)


linear_algo([4, 5, 6, 8])

print("O(n^3):")  # 3 for loops


def cubic_big_o(list1):
    for item1 in list1:
        for item2 in list1:
            for item3 in list1:
                print(item1, item2, item3)


cubic_big_o([1, 2, 3])

print("O(log(n))):")  # divided searching sections


def binary_search(arr, value):
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < arr[middle]:
            right = middle - 1
        elif value > arr[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(data, 6))

print("O(c^n):")  # recursion as constant in the power of n


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

# Constant	O(c)
# Linear	O(n)
# Quadratic	O(n^2)
# Cubic	O(n^3)
# Exponential	O(2^n)
# Logarithmic	O(log(n))
# Log Linear	O(nlog(n))
