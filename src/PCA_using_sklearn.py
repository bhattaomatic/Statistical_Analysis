#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from sh import cd
import sklearn.decomposition as deco

# Import data
cd('../data')
test_data = np.loadtxt('chan_imp_resp_normal_abs.txt')

# Reshape
hello = len(test_data)
test_data = np.reshape(test_data[0:hello],(hello/40,40))

# Normalize
test_data = test_data -np.mean(test_data,0) / np.std(test_data,0)

# Stack if more than one dataset
x_data = np.vstack((test_data))
print "shape of stacked data is ",x_data.shape

# Implement PCA
n_components = 40
pca = deco.PCA(n_components) 			# n_components is the components number after reduction
x_r = pca.fit(x_data).transform(x_data)
print "Shape after %d PCA is" %n_components,x_r.shape

# Eigenvector extraction for the Principal Components
variance = pca.explained_variance_
variance_ratio = pca.explained_variance_ratio_
"""
print ('Variance ', variance)
print ('Variance Ratio', variance_ratio)
loadings = pca.components_
"""
print ('explained variance (first %d prinncipal components): %.2f'%(n_components, sum(pca.explained_variance_ratio_)))
cumulative_energy = np.cumsum(variance_ratio)	# Can be done with variance as well the ratio just gives a better visualization

# save the length of the dataset (Handy in case of multiple datasets)
data_length = len(test_data)

# 2D Scatter plot of the first two principal Components
fig1 = plt.figure(1,figsize=(12.88, 7))
ax1 = fig1.add_subplot(111)
ax1.scatter(x_r[0:data_length,0], x_r[0:data_length,1])
plt.xlabel('Principal Component 1', fontsize=20)
plt.ylabel('Principal Component 2', fontsize=20)
plt.title('Principal Component Analysis', fontsize='26')
plt.grid()

# Cumulative Energy plot
fig2 = plt.figure(2,figsize=(12.88, 7))
ax2 = fig2.add_subplot(111)
ax2.plot(cumulative_energy , 'o-', linewidth=3)
plt.xlabel('Principal Components', fontsize='20')
plt.ylabel('Cumulative Sum of Eigenvector', fontsize='20')
plt.title('Cumulative Energy', fontsize='26')
plt.grid()

# Scree plot
fig3 = plt.figure(3,figsize=(12.88, 7))
ax3 = fig3.add_subplot(111)
ax3.plot(variance_ratio, 'o-', label='Variance Ratio', linewidth=3)
plt.xlabel('Principal Components', fontsize='20')
plt.ylabel('Eigenvalues', fontsize='20')
plt.title('Scree Plot', fontsize='26')
plt.legend()
plt.grid()
plt.show()

