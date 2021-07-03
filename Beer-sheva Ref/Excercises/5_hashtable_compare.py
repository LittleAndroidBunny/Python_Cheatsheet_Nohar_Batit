import string
from random import randrange as rr
from random import choice as rchoice
from time import perf_counter as count
import Hashtable_2

STRING_SIZE = 3000
NUM_OF_STRINGS = 10000


def string_generator(size=rr(10, STRING_SIZE), chars=string.ascii_letters + string.digits):
    """returns a random  string of length size, comprised of specific chars
    :param size: size of string, defaults to random size up to 3000
    :param chars: legetimate characters, defaults to digits and letters
    :returns: a string
    """
    return ''.join(rchoice(chars) for _ in range(size))


def list_lookup(ls, picked_strings):
    t = 0
    for st in picked_strings:
        dt  = count()
        #ls.index(str)
        st in ls
        dt = count() - dt
        t += dt
    return t/len(picked_strings)


def hash_lookup(hashtable, picked_strings):
    t = 0
    for st in picked_strings:
        dt = count()
        hashtable.find(st)
        dt = count() - dt
        t += dt
    return t/len(picked_strings)


# create data set
ls = [string_generator(size=rr(10, STRING_SIZE)) for i in range(NUM_OF_STRINGS)]
# why can't I use the default argument of string_generator?

# pick 10 strings
picked_strings = [ls[rr(0, NUM_OF_STRINGS - 1)] for i in range(10)]

non_existent_string = picked_strings[0]+'!!!'


# lookup via list
list_lookup_time = list_lookup(ls, picked_strings)
print('******************************************')
print('mean time to find existing string in list', list_lookup_time)

# look for non existent string in list
dt = count()
non_existent_string in ls
dt = count() - dt
print('******************************************')
print('time to look for non existent string in list', dt)


# create a hashtable
hash_t = Hashtable_2.Hashtable(int(4 * NUM_OF_STRINGS / 3))
for i in range(NUM_OF_STRINGS):
    hash_t.insert(ls[i])

# lookup via hashtable
hash_lookup_time = hash_lookup(hash_t, picked_strings)
print('******************************************')
print('mean time to find existing string in hashtable', hash_lookup_time)

# look for non existent string in hashtable
dt = count()
hash_t.find(non_existent_string)
dt = count() - dt
print('******************************************')
print('time to look for non existent string in hashtable', dt)
