import random, pylab, numpy


# 1
def getData():
    hrList, stElevList, ageList, prevACSList, classList = [], [], [], [], []
    cardiacData = open('cardiacData.txt', 'r')
    for l in cardiacData:
        l = l.split(',')
        hrList.append(int(l[0]))
        stElevList.append(int(l[1]))
        ageList.append(int(l[2]))
        prevACSList.append(int(l[3]))
        classList.append(int(l[4]))

    def scaleAttrs(vals):
        # vals = pylab.array(vals)
        mean = sum(vals) / len(vals)
        sd = numpy.std(vals)
        for i in range(len(vals)):
            vals[i] = vals[i] - mean
            vals[i] = vals[i] / sd
        return vals

    hrList = scaleAttrs(hrList)
    stElevList = scaleAttrs(stElevList)
    ageList = scaleAttrs(ageList)
    prevACSList = scaleAttrs(prevACSList)
    return ((hrList, stElevList, ageList, prevACSList, classList))


# 2
class Patient(object):

    def __init__(self, name, features, label=None):
        # Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        dist = 0
        v1 = self.features
        v2 = other.getFeatures()
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i]) ** 2
        return dist ** (1 / 2)

    def __str__(self):
        return self.name + ':' + str(self.features) + ':' \
               + str(self.label)


# 3
def points(hrList, prevACSList, stElevList, ageList, classList):
    points = []
    for i in range(len(hrList)):
        features = pylab.array([hrList[i], prevACSList[i], \
                                stElevList[i], ageList[i]])
        pIndex = str(i)
        points.append(Patient('P' + pIndex, features, classList[i]))
    return points


# points(getData()[0],getData()[1],getData()[2],getData()[3],getData()[4])
# 4
class Cluster(object):

    def __init__(self, examples):
        """Assumes examples a non-empty list of Examples"""
        self.examples = examples
        self.centroid = self.computeCentroid()

    def update(self, examples):
        """Assume examples is a non-empty list of Examples
           Replace examples; return amount centroid has changed"""
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)

    def computeCentroid(self):
        vals = pylab.array([0.0] * self.examples[0].dimensionality())
        for e in self.examples:  # compute mean
            vals += e.getFeatures()
        centroid = Patient('centroid', vals / len(self.examples))
        return centroid

    def getCentroid(self):
        return self.centroid

    def variability(self):
        totDist = 0
        for e in self.examples:
            totDist += (e.distance(self.centroid)) ** 2
        return totDist

    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid ' \
                 + str(self.centroid.getFeatures()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]  # remove trailing comma and space


# 5
def kmeans(examples, k):
    # Get k randomly chosen initial centroids, create cluster for each
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))

    # Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        # Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])

        # Associate each example with closest centroid
        for e in examples:
            # Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            # Add e to the list of examples for appropriate cluster
            newClusters[index].append(e)

        for c in newClusters:  # Avoid having empty clusters
            if len(c) == 0:
                raise ValueError('Empty Cluster')

        # Update each cluster; check if a centroid has changed
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False

    return clusters


# 6
def dissimilarity(clusters):
    """Assumes clusters a list of clusters
       Returns a measure of the total dissimilarity of the
       clusters in the list"""
    totDist = 0
    for c in clusters:
        totDist += c.variability()
    return totDist


# 7
examples = points(getData()[0], getData()[1], getData()[2], getData()[3], getData()[4])
clusters = kmeans(examples, 4)
print(dissimilarity(clusters))


def printClustering(clustering):
    """Assumes: clustering is a sequence of clusters
       Prints information about each cluster
       Returns list of fraction of pos cases in each cluster"""
    posFracs = []
    for c in clustering:
        numPts = 0
        numPos = 0
        for p in c.members():
            numPts += 1
            if p.getLabel() == 0:
                numPos += 1
        fracPos = numPos / numPts
        posFracs.append(fracPos)
        print('Cluster of size', numPts, 'with number of negatives =',
              numPos, ". The center is", (c.getCentroid()).getFeatures())
    return pylab.array(posFracs)


printClustering(clusters)
