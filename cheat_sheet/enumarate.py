# lets play Sheva Boom
import this
# you can read here the Zen of Python

s = "".join([this.d.get(c, c) for c in this.s])  # the Zen of Python is decoded with ROT13

# first implementation
print('************************************')
idx = 0
for word in s.split(' '):
    if not(idx % 7):
        print('**boom**', end=' ')
        idx = idx + 1
        continue
    idx = idx + 1
    print(word, end=' ')
print('')

# another implementation
print('************************************')
for idx, word in enumerate(s.split(' ')):
    if not(idx % 7):
        print('**boom**', end=' ')
        continue
    print(word, end=' ')
print('')

# lets dive in
print('************************************')


for t in enumerate(s.split(' ')):
    print(t)
print('************************************')

for t in enumerate(s.split(' '), 46):
    print(t)

"""The enumerate() method adds counter to an iterable and returns it (the enumerate object).The syntax of enumerate() 
is: enumerate(iterable, start=0)enumerate() Parameters

enumerate() method takes two parameters:

iterable - a sequence, an iterator, or objects that supports iteration start (optional) - enumerate() starts counting 
from this number. If start is omitted, 0 is taken as start.Return Value from enumerate() 

enumerate() method adds counter to an iterable and returns it. The returned object is a enumerate object.

You can convert enumerate objects to list and tuple using list() and tuple() method respectively.Example 1: How 
enumerate() works in Python? 

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
Output

<class 'enumerate'>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]"""
