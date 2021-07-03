# This script is part of tutorial number 3 of introduction of computer science for EE students at BGU.
# Uncomment the parts that you want to run.
# Topics:
#    - strings, indexing, and methods


# String variables
s1 = "a"
s2 = 'b'
s3 = 'I\'m a lumberjack, and I\'m okay.\nI sleep all night and ' \
     'I work all day.'

# strings can be added and multiplied
print(s1 + 3 * s2)


# string to numeric conversion - chr and ord
numeric_a = ord(s1)
print(numeric_a, chr(numeric_a))

# string to numeric conversion - longer strings
print('Memory view of string:')
memory_representation = bytes(s3, 'utf-8')

for ascii_value in memory_representation:
    print(ascii_value)


print('Multiple numerals to character conversion:')
binary = bytes([97, 98, 99])
print(binary.decode())


# string indexing and slicing
s1 = 'banana'
print(len(s1))
print(s1[0], s1[-6])

s2 = 'Always look at the bright side of life'
print(s2[7:18])
print(s2[1:])
print(s2[:5])
print(s2[0:-1:3])
print(s2[0::4])

# what is a method
brian = "Always look on the bright side of life!"
x = len(brian)  # is this a method?
brian_caps = brian.capitalize()  # is this a method?
print(brian_caps)

# some string methods
print(s2.__len__())
print(s2.count('o'))
print(s2.upper())
print(s2.find('l'))
print(s2.find('look'))

# example, if we want to cut only 'look at the' :
s3 = s2[s2.find('look'):s2.find('bright')]
print(s3)

s1 = 'Spam' * 5
for i in s1:
    print(i, end="*")
print('')

pass
