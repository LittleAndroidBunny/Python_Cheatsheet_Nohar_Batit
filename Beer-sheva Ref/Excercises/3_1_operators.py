# This script is part of lecture number 2 of introduction of cumpoter scienc for EE students.
# Uncomment the parts that you want to run.
# explain some operators
# explain conditions

print(type(1))

print(type(1) == type(2))
print(type(1) == type(1.2))

print(type(type(1) == type(1.2)))

print(type('1.5'))

print('And now for something completely different')


# Operators:

a = 4
b = 5
c = None
d = 7
print(a == b)
print(a == b-1)
print(b != c)
print(a < b < d)

s1 = 'european swallow'
s2 = 'african swallow'
print(s1 > s2)
print(s2 == s1)
s1 = 'swallow'
s2 = 'swallow'
print(s1 >= s2)

print(s1 == s2 and b > a)
print(not (s1 == s2 and b <= a))
print(s1 == s2 or b < a)


# conditions
your_favourite_color = 'blue'

if your_favourite_color == 'blue':
    print('Right, off you go')

if 5 > 3:
    print('correct')
    print('multiple statement can be used')

if True:
    print('Will always happen')

if None:
    print('Will it work?')

if 5:
    print('Will it work?')

# if-else
a = 3
b = 5
your_favourite_color ='blue! no, yellow...'

if your_favourite_color == 'blue':
    print('Right, off you go')
else:
    print('Wrong answer')

if b > a:
    pass    # leave this option for future use
else:
    print('only else for now')

# if-elif

if a>0:
    print('Positive')
elif a<0:
    print('Negative')
else:
    print('Zero')

# nested condition
a = 3
b = -9
c = 1
if b >= a:
    if b >= c:
        print('b is the largest')
    else:
        print('c is the largest')
else:
    if a >= c:
        print('a is the largest')
    else:
        print('c is the largest')

# Example
your_number = 6

if your_number % 2 == 0:
    print('test')
    if your_number % 3 == 0:
        print('The number ' + str(your_number) + ' is dividable by 2 and by 3')
    else:
        print('The number' + str(your_number) + 'is dividable by 2')
    print('test2')


