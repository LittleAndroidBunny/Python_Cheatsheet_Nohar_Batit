# This script is part of tutorial number 4 of introduction of computer science for EE students at BGU.
# Topics:
#   - It presents lists

# list data type
numeric_lst = [0, 1, 2, 3, 4]
names_list = ["Black night", "knights who say NI", "Brian"]
empty_lst = []
mixed_lst = numeric_lst + names_list
print(type(numeric_lst))
print(mixed_lst)

# indexing
print(mixed_lst[2:3])
print(mixed_lst[:4])
print(mixed_lst[5:])
print(mixed_lst[1:6:2])
# what will this do
print(mixed_lst[::-1])

# list constructor
s = "And now for something completely different"
str_lst = list(s)
rng = range(10)
rng_lst = list(rng)

# char list vs. string
a = list("knights who say NI")
a[0] = "change"
print(a)
print(id(a))
for element in a:
    element = "*"
print(a)
print(id(a))
for index in range(0, len(a), 2):
    a[index] = "*"
print(a)
print(id(a))

# dot product
a = list(range(1, 14, 2))
b = list(range(-5, 15, 3))
product = 0
for i in range(len(a)):
    product += a[i] * b[i]
print(product)


# list assignment
c = a
print(c == a)
print(c is a)
d = a + []
print(d == a)
print(d is a)
e = a.copy()
print(e == a)
print(e is a)

# arithmetic
print(a + b)
print(2*a)

# extension
a = [1, 2, 3]
b = [4, 5, 6]
# bad code - new allocation
a = a + b
# good code
a = [1, 2, 3]
a.extend(b)
# is this the same?
a = [1, 2, 3]
a.append(b)


# insertion and removal
a = [1, 2, 3, 4]
a.insert(1, 12)
# will this work?
a.insert(9, 10)
print(a)
a.remove(10)
print(a)
# will this work?
# a.remove(20)
print(a)

# better check it first
if 20 in a:
    a.remove(20)
