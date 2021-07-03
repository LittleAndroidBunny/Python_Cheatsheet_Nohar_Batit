a = iter([2, 4, 6])
print(a)
print(next(a))
print(next(a))
print(next(a))
# after the last element of the iterable is exhausted,
# a stop iteration exception is raised
print(next(a))