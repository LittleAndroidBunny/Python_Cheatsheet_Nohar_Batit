import time
import random
import string


## comments
#Q1|Q2
# Clause A:                 |
# times:  4+2*(x-1)/eps     |  # 5 + 4*log2(n) + log2(1/epsilon)
#                           |
# Clause B:                 |
# space:  x/eps             |  #  cube
#                           |
# Clause C:                 |
# complexity: O(n^2)        |  # O(log(n))

dict_4 = {}
list_4 = []

# Q1 -  exhaustive algorithm
def exhaustive_sqrt(cube, eps):
    ans = 1
    while (ans + eps) ** 2 < cube:
        ans = ans + eps

    if (ans + eps) ** 2 >= cube:
        return ans

# Q2 - bisection algorithm
def bisection_search(cube, epsilon):
    high = cube
    low = 1
    ans = (cube + 1) / 2

    while abs(ans ** 2 - cube) > epsilon:
        if ans ** 2 > cube:
            high = ans
            ans = (low + ans) / 2
        else:
            low = ans
            ans = (high + ans) / 2

    return ans


# Q3 - Calling the function from get list, see # **3.
def get_dict():
    j = 1
    for i in range(ord('a'), ord('z') + 1):
        dict_4[chr(i)] = j
        j += 1  # O(n)


def get_list(string):  # Calling the function from menu, sending it a string
    if not string.islower():  # Checking valid input
        string = input("Please follow instruction:")
        return get_list(string)
    else:
        get_dict()  # Initialize the dictionary
        for i in range(len(string)):
            list_4.append(dict_4[string[i]])
        x = merge_sorted(list_4)  # Assigning the value
        return [key for val in x for key, value in dict_4.items() if val == value]  #Return the list by letters [O(n)]

def merge_sorted(val):  # Merge sorted algorithm
    if len(val) < 2:
        return val  # Extreme case
    else:
        result = []
        mid = int(len(val) / 2)
        y = merge_sorted(val[:mid])
        z = merge_sorted(val[mid:])
        i = 0
        j = 0
        while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
        result += y[i:]
        result += z[j:]
        return result  #Total O(n(log(n))


#Q5
def insertion_sort(n):  # Function that gets a list and sort it by insertion algorithm
    for index in range(1, len(n)):
        current_value = n[index]
        position = index
        while position > 0 and n[position - 1] > current_value:
            n[position] = n[position - 1]
            position = position - 1
        n[position] = current_value
    return n

if __name__ == '__main__':

    print('Q3:')
    t0 = time.time()
    p = (exhaustive_sqrt(10000, 0.001))
    t1 = time.time()
    print(f'Exhaustive answer is: {p} Time since Epoch: {t1 - t0}')

    t2 = time.time()
    B = (bisection_search(10000, 0.001))
    t3 = time.time()
    print(f'Bisection answer is: {B} Time since Epoch: {t3 - t2}')

    T0 = time.process_time()
    EXHAUSTIVE = exhaustive_sqrt(120000, 0.001)
    T1 = time.process_time()
    time1 = T1 - T0

    T2 = time.process_time()
    BISECTION = (bisection_search(120000, 0.001))
    T3 = time.process_time()
    time2 = T3 - T2

    print('Exhaustive algorithm result:', EXHAUSTIVE, 'Process time: ', time1)
    print('Bisection algorithm result is:', BISECTION, 'Process time: ', time2)

    print('Q4:')
    letters = string.ascii_lowercase
    st = (''.join(random.choice(letters) for i in range(10)))
    print(f'The random string: {st}')
    print(f'The sorted string: {get_list(st)}')

    print('Q5:')
    L = random.sample(range(1, 50), 7)
    print(f'The random list: {L}')
    print(f'The sorted list: {insertion_sort(L)}')