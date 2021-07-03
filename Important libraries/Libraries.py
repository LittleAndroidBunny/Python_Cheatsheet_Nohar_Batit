
###### Libraries ########

# Pylab library :
import pylab as pl
pl.std(L)
newarray = pl.array(L)



# Numpy library :
import numpy
mean = numpy.mean(L)
median = numpy.median(L)
## Mode ?!?!


# Matplotlib.pyplot
import matplotlib as plt
plt.hist(L, bins)
plt.ylabel("Headliney")
plt.xlabel("Head;inex")
plt.show()

# Scattered Points :
plt.scatter(Lx ,Ly)
plt.show


# Linear regressions code :

from scipy import stats  ### for slope

slope, intercept, r, p, std_err = stats.linregress(Lx, Ly)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, Lx))

plt.scatter(Lx ,Ly)
plt.plot(Lx ,mymodel)
plt.show()




# Time library :
import time
t1 = time.time()

# Random library :
import random
random.choice(L, k=numofsamples)
random.randint(start, stop)
random.random()  - random(float[0 - 1])
random.seed(int)
random.uniform(start, stop) - generates(random(floats))
random.sample(set, k)


