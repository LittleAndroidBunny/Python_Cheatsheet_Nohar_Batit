# ######################
# ##  Nohar_Batit    ###
# ##   315572941     ###
# ######################

# ################################
import random
random.seed(1)

import pylab
import matplotlib.pyplot as plt
from scipy import stats


# Question 1
# function f1 gets a natural number and returns a tuple of the biggest divider
def f1(a):
    result = []
    if a < 0:
        return "please insert a number higher than 0"
    highest_divider = 2
    lowest_positive = 1
    if type(a / 2) is float:
        highest_divider = None
    for i in range(2, a):
        if a % i == 0:
            highest_divider = i
    for j in range(1, a+1):
        if j != 1 and a % j == 0:
            if lowest_positive < j and lowest_positive == 1:
                lowest_positive = j
    if lowest_positive == 1:
        lowest_positive = None
    result.append(highest_divider)
    result.append(lowest_positive)
    result = tuple(result)
    return result


input_1 = int(input("Enter a positive int number:\n"))
print("Question 1")
print(f1(input_1))

# b
comp1 = "O(n)"
print("The complexity of the code is:", comp1)
list1 = [1, 3, 4, 5, 9, 9]
list2 = [1, 2, 3, 4, 5, 0]
list3 = [4, 5, 6, 6, 7, -8, 9]


def f2(l1, l2, l3):
    list_new = []
    list_all = []
    for i in l1:
        if i in l2 + l3:
            list_new.append(i)
    for j in l2:
        if j in l3:
            if j not in l1:
                list_new.append(j)
    for k in list_new:
        if k not in list_all:
            list_all.append(k)
    return list_all


print(f2(list1, list2, list3))



# Question 3
# function f3 is a recursive function that gets a number bigger than 1 and finds An = 2An-1 - 3An-2
def f3(n):
    if n == 1:
        return 1
    if n == 2:
        return 4
    if n < 1:
        return "Enter an n bigger than 1"
    else:
        return 2*f3(n-1) - 3*f3(n-2)


print()
print("Question 3")
while True:
    print("Please enter an integer n biggest than 0:")
    num = int(input())
    if num > 0:
        break
print(f"The An is: (by An = 2An-1 - 3An-2)\n{f3(num)}")

# Question 4
# function f4 gets a list of numbers and returns a dictonary of numbers
# organized in keys buy the first number(from left) the keys in the dictonary are (0-9)

dictonary = {}


def find(f):
    temp = abs(f)
    if temp > 10:
        return round(find(temp / 10))
    else:
        return round(temp)


def f4(list_of_numbers):
    for i in range(10):
        dictonary[i] = []
    for number in list_of_numbers:
        temp = find(number)
        for i in range(10):
            if i == temp:
                dictonary[i].append(number)
    return dictonary


types = []
print()
print("Question 4")
print(f4([12, -121, 1, 1111, 22.2, 2.2, 1234314.1, 0, 0]))
# # showing the keys are from int type
# for k in dictonary.keys():
#     types.append(type(k))
# print(types)


# Question 5
# class c5 checks if the right amount of palafel balls(between 2-7) used and if there is a sauce or not
class c5:
    def __init__(self, Nb, s):
        self.Nb = Nb
        self.s = bool(s)
        assert (2 <= Nb <= 7), "This is not the right amount of falafel balls, min 2, max 7"
        assert (s == True) or (s == False), "s should be True or False"

    # print function prints number of balls and if there is a spicy sauce
    def __str__(self):
        if self.s:
            return f"Mana: {self.Nb} balls and has spicy sauce"
        else:
            return f"Mana: {self.Nb} balls and has no spicy sauce"

    # 5.bet
    # add function that add 2 manot falafel and checks if its possible
    # if its possible it makes the mix and checks if there was a sauce
    # if on 1 of the manot was a sauce than the mix will have a sauce
    # if neither were with the sauce the mix wont have a sauce
    def __add__(self, other):
        if self.Nb + other.Nb < 8:
            self.Nb = self.Nb + other.Nb
        else:
            return "Cant add the falafels cause too many balls"
        if self.s and other.s:
            self.s = other.s
            return f"Mana after merge: {self.Nb} balls and has spicy sauce"
        elif self.s and not other.s:
            other.s = self.s
            return f"Mana after merge: {self.Nb} balls and has spicy sauce"
        elif not self.s and other.s:
            self.s = other.s
            return f"Mana after merge: {self.Nb} balls and has spicy sauce"
        else:
            self.s = self.s
            return f"Mana after merge: {self.Nb} balls and has no spicy sauce"


man = c5(2, True)
man2 = c5(5, False)
print()
print("Question 5.alef")
print("1st", man)
print("2nd", man2)
print()
print("Question 5.bet")
print(man+man2)

def f6(N):
    counter = 0
    prob = 0
    for i in range(N):
        for j in range(10):
            dice = random.randrange(1, 7)
            round(dice)
            if dice == 6:
                counter += 1
        if counter == 2:
            prob += 1
        counter = 0
    return prob/N


print(f6(1000000))


# Question 7
# function f7a get a list of tuples and returns 3 random tuples from the list
# with using random.sample
def f7a(l):
    random.seed(2)
    r_list = random.sample(l, 3)
    return r_list


# print(f7a([(1,2,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4)]))
#Question 7.bet
def euclidean_dist(vec1, vec2):
    dist = 0
    for k in range(len(vec1)):
        dist += (vec1[k] - vec2[k]) ** 2
    return dist ** 0.5


def f7b(l1, l2):
    first_vector = []
    sec_vector = []
    third_vector = []
    for i in l1:
        min_euc = min(euclidean_dist(i, l2[0]), euclidean_dist(i, l2[1]), euclidean_dist(i, l2[2]))
        if euclidean_dist(i, l2[0]) == min_euc:
            first_vector.append(i)
        elif euclidean_dist(i, l2[1]) == min_euc:
            sec_vector.append(i)
        else:
            third_vector.append(i)
    return [first_vector, sec_vector, third_vector]


def f7c(l):
    def compute_centroid(list):
        vals = pylab.array([0] * len(list[0]))
        for vec in list:  # compute mean
            vals += vec
        return tuple(vals / len(list))

    return [compute_centroid(l[0]), compute_centroid(l[1]), compute_centroid(l[2])]


def f7d(l):
    initial_centroids = f7a(l)
    clusters = f7b(l, initial_centroids)
    new_centroids = f7c(clusters)
    while True:
        initial_centroids = new_centroids
        clusters = f7b(l, new_centroids)
        new_centroids = f7c(clusters)
        if initial_centroids == new_centroids:
            break
    return clusters

# Question 8
# function f8 gets a list and sorts it from the highest to lowest and returns it
def f8(l):
    flag = False
    while not flag:
        flag = True
        for n in range(len(l)):
            for k in range(n, 0, -1):
                if l[n] > l[k]:
                    temp = l[k]
                    l[k] = l[n]
                    l[n] = temp
                    flag = False
        if l[0] < l[1]:
            temp = l[0]
            del l[0]
            l.append(temp)
            flag = False
    return l


comp2 = "O(n**3)"
print()
print("Question 8")
print(f8([12, 4, 5, 122, 1, 13, 0]))
print("The complexity is:", comp2)


# Question 9
# the function f9 makes a linear regression
def f9(tau, alpha):
    slope, intercept, r, p, std_err = stats.linregress(tau, alpha)

    def my_func(x):
        return slope * x + intercept

    model = list(map(my_func, tau))
    plt.scatter(tau, alpha)
    plt.plot(tau, model)
    plt.show()

    return slope


print()
print("Question 9")
f9([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
