#$@$@$@$@$@$@$@$@$ Searching algorithms @$@$@$@$@$ Searching algorithms @$@$@$@$@$@$@$@$@$@$@$#
#$@$@$@$@$@$@$@$@$ Searching algorithms @$@$@$@$@$ Searching algorithms @$@$@$@$@$@$@$@$@$@$@$#
#$@$@$@$@$@$@$@$@$ Searching algorithms @$@$@$@$@$ Searching algorithms @$@$@$@$@$@$@$@$@$@$@$#
    
    
 # def linear_search(L, e):
 #    found = False
 #    for i in range(len(L)):
 #        if e == L[i]:
 #            found = True
 #    return found

testList = [1, 3, 4, 5, 9, 18, 27]

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

x = isSubset(testSet2,testSet)
print(x)


def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
       
#$@$@$@$@$@$@$@$@$ Sorting algorithms @$@$@$@$@$ Sorting algorithms @$@$@$@$@$@$@$@$@$@$@$#
#$@$@$@$@$@$@$@$@$ Sorting algorithms @$@$@$@$@$ Sorting algorithms @$@$@$@$@$@$@$@$@$@$@$#
#$@$@$@$@$@$@$@$@$ Sorting algorithms @$@$@$@$@$ Sorting algorithms @$@$@$@$@$@$@$@$@$@$@$#
    
def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)


def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 
testList = [1,3,5,7,2,6,25,18,13]
       
print('')
print(selection_sort(testList))
print(testList)


def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
        
testList = [1,3,5,7,2,6,25,18,13]

#print('')
#print(merge_sort(testList))



###############classsessssssss######classsessssssss#####classsessssssss####classsessssssss################
###############classsessssssss######classsessssssss#####classsessssssss####classsessssssss################
###############classsessssssss######classsessssssss#####classsessssssss####classsessssssss################

#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x, origin.x)
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))
print(c)


#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects


##############
## EXAMPLE: a set of integers as class
##############
class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
#s.remove(3)  # leads to an error
print(s)
s.remove(3)



##################iiiiinnnnnhhhhhhheeeeeeeeerrrrrriiiiiiittttttaaaaaaannnnnnncccccccceeeeeeeeeee#################
##################iiiiinnnnnhhhhhhheeeeeeeeerrrrrriiiiiiittttttaaaaaaannnnnnncccccccceeeeeeeeeee#################
##################iiiiinnnnnhhhhhhheeeeeeeeerrrrrriiiiiiittttttaaaaaaannnnnnncccccccceeeeeeeeeee#################

import random

#################################
## Animal abstract data type 
#################################
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
        
print("\n---- animal tests ----")
a = Animal(4)
print(a)
print(a.get_age())
a.set_name("fluffy")
print(a)
a.set_name()
print(a)



#################################
## Inheritance example 
#################################
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
    
print("\n---- cat tests ----")
c = Cat(5)
c.set_name("fluffy")
print(c)
c.speak()
print(c.get_age())
#a.speak() # error because there is no speak method for Animal class

    
#################################
## Inheritance example
#################################
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def speak(self):
        print("hello")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

print("\n---- person tests ----")
p1 = Person("jack", 30)
p2 = Person("jill", 25)
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)


#################################
## Inheritance example
#################################
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

print("\n---- student tests ----")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
print(s1)
print(s2)
print(s1.get_name(),"says:", end=" ")
s1.speak()
print(s2.get_name(),"says:", end=" ")
s2.speak()



#################################
## Use of class variables  
#################################
class Rabbit(Animal):
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 001 instead of 1
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    def __eq__(self, other):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        # the backslash tells python I want to break up my line
        parents_same = self.parent1.rid == other.parent1.rid \
                       and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
                           and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+ self.get_rid()

print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)


################################dicccccccccccccccccttttttttttttttttttinaries@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
################################dicccccccccccccccccttttttttttttttttttinaries@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
################################dicccccccccccccccccttttttttttttttttttinaries@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#####################################
# EXAMPLE: using dictionaries
#          counting frequencies of words in song lyrics
#####################################

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
    
    
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)


def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
    
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict
        else:
            done = True
    return result
    
#print(words_often(beatles, 5))

#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

argToUse = 34
#print("")
#print('using fib')
#print(fib(argToUse))
#print("")
#print('using fib_efficient')
#print(fib_efficient(argToUse, d))

################################rrrrrrreeeeeecursiveeeeeeee@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
################################rrrrrrreeeeeecursiveeeeeeee@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
################################rrrrrrreeeeeecursiveeeeeeee@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

#print(Towers(4, 'P1', 'P2', 'P3'))

#####################################
# EXAMPLE:  fibonacci
#####################################

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
#####################################
# EXAMPLE:  testing for palindromes
#####################################
        
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

#print(isPalindrome('eve'))
#
#print(isPalindrome('Able was I, ere I saw Elba'))
#
#print(isPalindrome('Is this a palindrome'))


###########################trytrytrytrytrytrytrytrytry##########################
###########################trytrytrytrytrytrytrytrytry##########################
###########################trytrytrytrytrytrytrytrytry##########################

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("executing Finally...")
#pass 