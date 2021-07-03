#####################
###  Nohar Batit ####
####ID 315572941#####
#####################
import random
import pylab as pl
import numpy

#Question 1

# function scales for each array that it gets as val


def scaleattrs(vals):
    vals =pl.array(vals)
    mean = sum(vals) / len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals / sd


# function gets the data from file and switches it from columns to list(rows)
# and sends 4 lists to scale function

def DataExtract():
    l1, l2, l3, l4, l5 = [], [], [], [], []
    f = open('cardiacData.txt', 'r')
    for i in f:
        my_list = i.split(',')
        l1.append(int(my_list[0]))
        l2.append(int(my_list[1]))
        l3.append(int(my_list[2]))
        l4.append(int(my_list[3]))
        l5.append(int(my_list[4]))
    l1 = scaleattrs(l1)
    l2 = scaleattrs(l2)
    l3 = scaleattrs(l3)
    l4 = scaleattrs(l4)
    return [l1, l2, l3, l4, l5]

data = []  # create lists
for d in range(4):
    data.append([])

# Question 2
# Class function for finding the Euclidean distance
# and a function for finding the dimension of vectors


class Example(object):
    def __init__(self, vector, number=None):
        self.number = number
        self.vector = vector

    def get_vector(self):
        return self.vector[:]

    def get_number(self):
        return self.number

    def distance(self, v2):
        d = 0
        vec1 = self.vector
        vec2 = v2.vector
        for i in range(len(vec1)):
            d += abs(vec1[i] - vec2[i]) ** 2
        result = d ** 0.5
        return result

    def dimensionality(self):
        return len(self.vector)

    def __str__(self):
        return "P" + " : " + str(self.vector) + " : " + str(self.number)

# Question 3
# function data gets all the lists for data_getter
# and makes them into 1 list of vectors


def PatientCreator():
    all_lists = DataExtract()
    resultList = []
    for i in range(len(all_lists[0])):
        vect = pl.array([all_lists[0][i], all_lists[1][i], all_lists[2][i], all_lists[3][i]])
        resultList.append(Example(vect, all_lists[4][i]))
    return resultList

# Question 4
# class cluster contains:
# function computeCentroid which finds the center of the cluster
# function update which returns the distance between the cluster and the center
# function variability which finds the variability of the cluster
# function members run throw all the examples of clusters


class Cluster(object):
    def __init__(self, examples):
        self.examples = examples
        self.centroid = self.computeCentroid()

    def getCentroid(self):
        return self.centroid

    def computeCentroid(self):
        val = pl.array([0.0] * self.examples[0].dimensionality())
        val = pl.array([0.0] * self.examples[0].dimensionality())
        for e in self.examples:
            val += e.get_vector()
        centroid = Example(val / len(self.examples))
        return centroid

    def update(self, examples):
        Centroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return Centroid.distance(self.centroid)

    def variability(self):
        result = 0
        for e in self.examples:
            result += (e.distance(self.centroid)) ** 2
        return result

    def members(self):
        for e in self.examples:
            yield e
# Question 5
# function k_means gets a number (k) and clusters(examples)
# the function picks randomly k number of clusters from the examples
# and creates a starting list of them
# than it goes threw the starting list and creates a new list of clusters
# every element of the list is a cluster which gets the smallest near distance to the centroid


def k_means(examples, k, verbose=False):
    initialCentroids = random.sample(examples, k)
    clusters = []
    for i in initialCentroids:
        clusters.append(Cluster([i]))
    done = False
    count = 0
    while not done:
        count += 1
        newClusters = []
        for i in range(k):
            newClusters.append([])
        for e in examples:
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newClusters[index].append(e)

        for c in newClusters:
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        done = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                done = False
        if verbose:
            print('Iteration #' + str(count))
            for c in clusters:
                print(f"{c}\n")
    return clusters

# Question 6
# function dissimilarity calculates the dissimilarity for the clusters and returns it


def dissimilarity(clusters):
    dissmilarity = 0
    for c in clusters:
        dissmilarity += c.variability()
    return dissmilarity


# Question 7
# function try_kmeans finds the best result with the smallest dissimilarity

def try_kmeans(examples, numClusters, tries, verbose=False):
    best = k_means(examples, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    loop = 1
    while loop < tries:
        try:
            clusters = k_means(examples, numClusters, verbose)
        except ValueError:
            continue
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        loop += 1
    return best

# print function


def printClustering(clustering):
    lists7 = []
    for cluster in clustering:
        numPts = 0
        numNeg = 0
        for p in cluster.members():
            numPts += 1
            if p.get_number() == 0:
                numNeg += 1
        fracNeg = numNeg / numPts
        lists7.append(fracNeg)
        print('Cluster of size', numPts, 'with fraction of negative (label 0)  =',
              round(fracNeg, 4))
        print("The centroid:\n", cluster.getCentroid(), end="\n\n")
    return pl.array(lists7)

# function testClustering used to start the try k_means and printClustering functions


def testClustering(patients, numClusters, numTrials=5):
    random.seed(0)
    bestClustering = try_kmeans(patients, numClusters, numTrials)
    fr = printClustering(bestClustering)
    return fr


patients = PatientCreator()
clustering = k_means(patients, 4)
print("Dissimilarity is : {}".format(dissimilarity(clustering)))
for k in (4,):
    print('\n     Test k-means (k = ' + str(k) + ')')
    posFracs = testClustering(patients, k)

printClustering(clustering)
