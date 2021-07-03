def example2(num):
    if num == 0:
        return 0
    return example2(num//10) + num % 10


def example2_5(num):
    if num < 10:
        return num
    return example2(num//10) + num % 10


def example3(str):
    if len(str) == 1:
        return str
    return example3(str[1:]) + str[0]



print(example2(15426))
print(example2_5(15426))
print(example3('abc'))



def factorial1(n):
    sum = 1
    num = 1
    while num <= n:
        sum *= num
        num += 1
    return sum


def factorial2(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return n*factorial2(n-1)


print(factorial1(4))
print(factorial2(4))

def iteratively(n):
    sum = 1
    num = 1
    while num <= n:
        sum *= num
        num += 1
    return sum

print(iteratively(4))

