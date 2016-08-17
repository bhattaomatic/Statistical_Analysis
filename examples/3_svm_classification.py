#!/usr/bin/env python

from sklearn import datasets
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt

# Loading an example dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

svc = svm.SVC(kernel='linear', degree=3)
svc.fit(iris.data, iris.target)

perm = np.random.permutation(iris.target.size)
iris.data = iris.data[perm]
iris.target = iris.target[perm]

svc.fit(iris.data[:100], iris.target[:100])

print svc.score(iris.data[100:], iris.target[100:])
#print svc.coef_

plt.scatter(X[:,0], X[:,1], c=Y, cmap=plt.cm.Paired)
plt.show()

