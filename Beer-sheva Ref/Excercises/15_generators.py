def fibonacci_with_generator(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b


a = fibonacci_with_generator(10)
print(next(a))
print(next(a))
print('**** generator in for loop ***')
for num in fibonacci_with_generator(10):
    print(num)
