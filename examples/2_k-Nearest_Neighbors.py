#!/usr/bin/env python

from sklearn import datasets
import numpy as np
from sklearn import neighbors

# Loading an example dataset
iris = datasets.load_iris()

# Create and fit a nearest-neighbor classifier
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target)

print knn.predict([[0.1, 0.2, 0.3, 0.4]])

perm = np.random.permutation(iris.target.size)
iris.data = iris.data[perm]
iris.target = iris.target[perm]

knn.fit(iris.data[:100], iris.target[:100])

print knn.score(iris.data[100:], iris.target[100:])
