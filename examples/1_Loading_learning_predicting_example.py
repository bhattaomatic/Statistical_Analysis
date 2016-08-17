#!/usr/bin/env python

from sklearn import datasets
import numpy as np
from sklearn import svm

# Loading an example dataset
iris = datasets.load_iris()

print iris.data.shape
print iris.target.shape
print np.unique(iris.target)


# Learning and predicting
clf = svm.LinearSVC()
clf.fit(iris.data, iris.target)	# learn from data

clf.predict([[5.0, 3.6, 1.3, 0.25]])

print clf.coef_
