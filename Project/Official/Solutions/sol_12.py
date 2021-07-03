import random
import numpy
from scipy import stats
import matplotlib
import matplotlib.pyplot
import matplotlib.pylab as pl


def f1(a):
    for i in range(1, a):
        if a % i == 0:
            b = i
    return (b, a / b)


def f2(L1, L2, L3):
    L = []

    for i in L1:
        if i in L2 or i in L3:
            L.append(i)
    for i in L2:
        if i in L3:
            L.append(i)
    return (L)


def f3(n):
    if n == 1:
        return (1)
    elif n == 2:
        return (4)
    else:
        return 2 * f3(n - 1) - 3 * f3(n - 2)


def f4t(L):
    d = {}
    for i in range(10):
        d[i] = []
    for i in L:
        d[int(str(i)[0])].append(i)
    return d


class c5(object):
    def __init__(self, Nb, s):
        assert type(Nb) == int and type(s) == bool and Nb > 1 and Nb < 8, \
            "This is not manat Falafel"
        self.Nb = Nb
        self.s = s

    def __str__(self):
        # free text
        pass

    def __add__(self, other):
        return c1(self.Nb + other.Nb, self.s or other.s)


def f6(N):
    random.seed(1)
    sum = 0
    for i in range(N):
        nOf6 = 0
        for j in range(10):
            k = random.choice([1, 2, 3, 4, 5, 6])
            if k == 2:
                nOf6 += 1
        if nOf6 == 2:
            sum += 1
    return (sum / N)


def f7a(L):
    random.seed(2)
    return random.sample(L, 3)


L = [(3, 4, 3, 5), (3, 2, 6, 9), (2, 2, 1, 1), (1, 2, 3, 4), (2, 1, 2, 1), (1, 1, 1, 1), (3, 3, 3, 3), (1, 3, 1, 3),
     (23, 3, 2, 1), (3, 4, 5, 6), (2, 1, 1, 2), (3, 2, 4, 5), (4, 3, 43, 4), \
     (12, 12, 12, 12), (0, 3, 1, 4), (4, 3, 7, 2)]
La = f7a(L)


def f7b(L1, L2):
    def distance(v1, v2):
        return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2 + (v1[2] - v2[2]) ** 2 + (v1[3] - v2[3]) ** 2) ** (1 / 2)

    L = [[], [], []]
    for v in L1:
        min = distance(v, L2[0])
        a = 0
        if min > distance(v, L2[1]):
            a = 1
            min = distance(v, L2[1])
        if min > distance(v, L2[2]):
            a = 2
        L[a].append(v)
    return (L)


Lb = f7b(L, La)


def f7c(L):
    Lavarage = []
    for i in range(3):
        v0, v1, v2, v3 = 0, 0, 0, 0
        for j in L[i]:
            v0 += j[0] / len(L[i])
            v1 += j[1] / len(L[i])
            v2 += j[2] / len(L[i])
            v3 += j[3] / len(L[i])
        vavarage = (v0, v1, v2, v3)
        Lavarage.append(vavarage)
    return (Lavarage)


Lc = f7c(Lb)
print(Lc)


def f7d(L):
    Lnew = f7b(L, f7a(L))
    Lavarage = f7c(Lnew)
    Lnew = f7b(L, Lavarage)
    Lavarage_new = f7c(Lnew)

    while Lavarage != Lavarage_new:
        Lavarage = Lavarage_new
        Lnew = f7b(L, Lavarage)
        Lavarage_new = f7c(Lnew)

    return (Lnew)


print(f7d(L))


def f8(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return (arr)


def f9(y, x):
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    return slope

# כיול של נתנאל

def Scale(L):
    L = pl.array(L)
    mean = float(pl.mean(L))
    l = L-mean
    sd = L.std()
    l = l/sd
    return l