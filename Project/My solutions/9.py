#######################
###   Nohar_Batit   ###
###    315572941    ###
#######################
import random
import numpy as np
from scipy import stats
import matplotlib.pyplot as mpl

random.seed(1)


### Q1 ###:
def probability_calc(n, N):  ### n-times of the same result ,N-times series
    print("Actual probability of " + str(n * "0") + " is :", 0.5 ** n)
    Success = 0
    for i in range(N):
        c = 0
        for q in range(n):
            a = random.randint(0, 1)
            if a == 0:
                c += 1
            if c == n:
                Success += 1
    print("Estimated is :", Success / N)


### Q2 ###:
# This function checks if from the 12 throws of coin we get the same side of the coin
# print then start the coin toss function for the Estimated Probability
def coin_flip(n2, k2, N2):
    total = 0
    for j in range(N2):
        heads = 0
        for i in range(n2):
            num_flips = 0
            win = 0
            while win == 0:
                turn = np.random.uniform(0, 1)
                num_flips += 1
                if turn <= k2:
                    if num_flips % 2 != 0:
                        heads += 1
                    win += 1
        total += float(heads) / float(n2)
    return total / N2


k = 7
n = 12
x = 10000


def coin_toss1(n, k):
    a = [0, 1]
    counter = 0
    for i in range(n):
        random.choice(a)
        if random.choice(a) == 1:
            counter += 1
    if counter >= k:
        return 1
    else:
        return 0


def coin1(n, range1, k):
    x = 0
    for i in range(range1):
        x += coin_toss1(n, k)
    print(f"The Estimated Probability of only getting the same side of the coin is: {x / range1}")


### Q3 ###:
def coin_toss2(n, k):
    counter = 0
    for i in range(n):
        if random.randint(1, 100) < 67:
            counter += 1
    if counter > k:
        return 1
    else:
        return 0


def coin2(n, range1, k):
    x = 0
    for i in range(range1):
        x += coin_toss2(n, k)
    print(f"The Estimated Probability of only getting the same side of the coin is: {x / range1}")


coin2(n, x, k)


### Q4 ###:

def statistics(l):  # as requested methods, function
    print(np.mean(l))
    print(np.median(l))
    print(stats.mode(l))
    print(np.std(l))

### Q5 ###:
def random_list(x, y):
    L = []  # getting random list
    for i in range(20):
        L.append(random.randint(x, y))
    return L


### Q6 ###:
def print_random_list(x, y):  # This function calls the previous function 10000 times, save result in a list and
    # print its Histogram
    L = []
    for i in range(10000):
        L.append(random_list(x, y))
    mpl.hist(L, 10, None, False)
    mpl.ylabel()
    mpl.xlabel()
    mpl.show()
    return L


### Q7 ###:
def calc_percentage(L):  # This function gets results from randoms_average function and saves it into a list
    c = 0
    for i in L:
        if abs(mean - i) <= 2 * std:
            c += 1
    print(c / len(L))


### Q8 ###:
def hook(x):  # in this question we will find the Scatter graph for the result of the lists x,y
    # we will create a diagram
    return slope * x + intercept


### Q9 ###:
def socks_random_washing_machine(N):
    # here we have 100 socks in 2 different colors, The function will approximate the probability for the same socks
    white_socks = np.array(np.tile(1, 30))
    blue_socks = np.array(np.tile(2, 70))
    flatten_list = [m for n in [white_socks, blue_socks] for m in n]
    random.shuffle(flatten_list)
    counter = 0
    for i in range(N):
        x = random.sample(flatten_list, 2)
        if x[0] == x[1]:
            counter += 1
    return f'{(counter / N) * 100}%'


if __name__ == '__main__':
    probability_calc(12, 100000)
    statistics([1, 3, 5345, 5, 66, 7, 8, 43])
    L = random_list(1, 20)
    std = np.std(L)
    print("std is :", std)
    mean = np.mean(L)
    print("mean is :", mean)
    Force = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Deformation = [3, 4.5, 6, 7.5, 9, 10.5, 13, 14, 15]
    slope, intercept, r, p, std_err = stats.linregress(Force, Deformation)
    my_model = list(map(hook, Force))
    mpl.scatter(Force, Deformation)
    mpl.plot(Force, my_model)
    mpl.show()
    print(socks_random_washing_machine(1000))
    P = 0.6  # Can be used for fair coin too
    q = 7
    print(coin_flip(12, P, 100000))  # This function prints us the Estimated probability of getting same side with
    # the cheating coin
