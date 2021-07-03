# 1
import random
import numpy
import matplotlib.pyplot as plt
from scipy import stats


def rollCoin():
    return random.choice([1, 0])


# random.seed(1)


def runSim(n, numTrials):
    goal = n * "0"
    txt = goal
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollCoin())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=',
          round(1 / (2 ** len(goal)), 8))
    estProbability = round(total / numTrials, 8)
    print('Estimated Probability of', txt, '=',
          round(estProbability, 8))


# runSim(12,100000)

# 2
def kTrees(k, n, N):
    goal = 0
    for i in range(N):
        kexp = 0
        for j in range(n):
            if rollCoin() == 0:
                kexp += 1
        if kexp == k:
            goal += 1

    print('Estimated Probability of k trees from n rolls', '=', goal / N)


# 3

def kTreesBiased(k, n, N):
    goal = 0
    for i in range(N):
        kexp = 0
        for j in range(n):
            if rollBiasedCoin() == 0:
                kexp += 1
        if kexp == k:
            goal += 1

    print('Estimated Probability of k trees from n rolls of biased coin', '=', goal / N)


def rollBiasedCoin():
    return random.choice([0, 0, 1])


# kTreesBiased(3,3,100)
# 4
def stat(L):
    mean = numpy.mean(L)
    median = numpy.median(L)
    mode = stats.mode(L)
    std = numpy.std(L)
    return mean, median, mode, std


# print(stat([2,4,23,66,23,23]))
# 5,6

import matplotlib.pyplot as plt


def avarageOfRandomList(x, y):
    l = numpy.random.uniform(x, y, 20)
    return (numpy.mean(l))


def Histo():
    L = []
    for i in range(10000):
        L.append(avarageOfRandomList(0, 10))
    plt.hist(L, 100)
    plt.show()
    return (L)


# 7
L = Histo()
mean = numpy.mean(L)
std = numpy.std(L)
# creating a list l for values in L restricted to the 4 sigma domain
l = []
for i in L:
    if (i > mean - 2 * std and i < mean + 2 * std) or i == mean - 2 * std or i == mean + 2 * std:
        l.append(i)
print("percent of L in 4 sigma domain is", str(100 * len(l) / len(L)))

# 8

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [3, 4.5, 6, 7.5, 9, 10.5, 13, 14, 15]
slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print("The experimental spring constant is", (1 / slope) * 1000, "N/m")


# 9
def pair(N):
    basket = [0] * 70 + [1] * 30
    goal = 0
    for i in range(N):
        sample = random.sample(basket, 2)

        if sample == [0, 0] or sample == [1, 1]:
            goal += 1
    print("The estimated probability for a pair of socks is", goal / N)


pair(30)


#look at the comments in the file sol_9b pdf computer