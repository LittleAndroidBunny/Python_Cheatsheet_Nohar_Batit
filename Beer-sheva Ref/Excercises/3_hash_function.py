#example of user defined hash function for strings (not recommended)
def hash4strings(st):
    """ ord(c) is the ascii value of character c
          2**120+451 is a prime number """
    s = 0
    for i in range(len(st)):
        s = (128*s + ord(st[i])) % (2**120+451)
    return s**2 % (2**120+451)


s = 'Tis but a scratch'

x = hash4strings(s)
print(x)
print(bin(x))

y = hash(s)
print(y)
print(bin(y))


ls = [4, 3]
# Will this work?
#hash(ls)

# Will this work?
#dic = {ls: 1, 'a': 2}

m = 1000
z = hash(s) % m
print(z)
print(bin(z))
