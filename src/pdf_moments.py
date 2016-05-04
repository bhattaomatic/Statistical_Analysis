#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as st

def gaussian_dist(mean, variance):
	"""Gaussian Distribution"""
	mean1, variance1, skew, kurt = st.norm.stats(moments='mvsk')
	print 'Gaussian Distribution = ', mean1, variance1, skew, kurt
	sigma = np.sqrt(variance)
	x = np.linspace(-3-len(mean),3+len(mean),100)
	for i in range(len(sigma)):
		plt.plot(x,mlab.normpdf(x, mean[0], sigma[i]), linewidth=4, label='$\mu=0, \sigma^2 =%0.1f$' %variance[i])
	for j in range(1,len(mean)):
		plt.plot(x,mlab.normpdf(x, mean[j], sigma[1]), linewidth=4, label='$\mu=%d, \sigma^2=%0.1f$' %(mean[j], variance[1]))
	plt.title('Gaussian Distribution', fontsize=26)
	plt.xlabel('X', fontsize=22)
	plt.ylabel('Probability', fontsize=22)
	plt.legend()
	plt.show()

def rayleigh_dist(sc):
	"""Rayleigh Distribution"""
	mean, variance, skew, kurt = st.rayleigh.stats(moments='mvsk')
	x = np.linspace(0,10,100)
	print 'Rayleigh Distribution = ', mean, variance, skew, kurt
	for i in range(len(sc)):
		rv = st.rayleigh(loc=0,scale=sc[i])
		plt.plot(x,rv.pdf(x), linewidth=4, label='$\sigma=%0.1f$' %sc[i])
	plt.title('Rayleigh Distribution', fontsize=26)
	plt.xlabel('X', fontsize=22)
	plt.ylabel('Probability', fontsize=22)
	plt.legend()
	plt.show()

def gamma_dist(k, theta):
	"""Gamma Distribution with almost all combinations of $\k and \Theta$"""
	x = np.linspace(0,30,100)
	for i in range(len(theta)):
		for j in range(len(k)):
			if (theta[i] == 0.5 and k[j] ==1):
				j+=1
			else:
				mean, variance, skew, kurt = st.gamma.stats(k[i], moments='mvsk')
				print 'Gamma Distribution %f = ' %k[i] ,mean, variance, skew, kurt
				rv = st.gamma(k[j], loc=0, scale=theta[i])
				plt.plot(rv.pdf(x), linewidth=4, label='$k=%0.1f, \Theta=%0.1f $' %(k[j], theta[i]))

	plt.title('Gamma Distribution', fontsize=26)
	plt.xlabel('X', fontsize=22)
	plt.ylabel('Probability', fontsize=22)
	plt.legend()
	plt.show()

def gamma_dist2(k, theta):
	"""Gamma Distribution a specific combination of $\k and \Theta$"""
	x = np.linspace(0,30,100)
	for i in range(len(theta)):
		mean, variance, skew, kurt = st.gamma.stats(k[i], moments='mvsk')
		print 'Gamma Distribution1 %f = ' %k[i] ,mean, variance, skew, kurt
		rv = st.gamma(k[i], loc=0, scale=theta[i])
		plt.plot(rv.pdf(x), linewidth=4, label='$k=%0.1f, \Theta=%0.1f $' %(k[i], theta[i]))
	plt.title('Gamma Distribution', fontsize=26)
	plt.xlabel('X', fontsize=22)
	plt.ylabel('Probability', fontsize=22)
	plt.legend()
	plt.show()

def lognormal_dist(mean, sigma):
	"""Lognormal Distribution all combinations of mean and variance"""
	x = np.linspace(0,10,50)
	shape = sigma
	scale = np.exp(mean)
	for i in range(len(sigma)):
		for j in range(len(mean)):
			mean2, variance, skew, kurt = st.lognorm.stats(shape[i], moments='mvsk')
			print 'Log-normal Distribution %f = ' %shape[i], mean2, variance, skew, kurt
			rv = st.lognorm(shape[i], loc=mean[j], scale=scale[i])
			plt.plot(rv.pdf(x), linewidth=4, label='$\mu=%0.1f, \sigma=%0.1f $' %(mean[j], shape[i]))
	plt.title('Lognormal Distribution', fontsize=26)
	plt.xlabel('X', fontsize=22)
	plt.ylabel('Probability', fontsize=22)
	plt.legend()
	plt.show()

def lognormal_dist2(mean, sigma):
	"""Lognormal Distribution a specific combination of mean and variance"""
	x = np.linspace(0,10,100)
	shape = sigma
	scale = np.exp(mean)
	for i in range(len(sigma)):
		mean2, variance, skew, kurt = st.lognorm.stats(shape[i], moments='mvsk')
		print 'Log-normal Distribution1 %f = ' %shape[i] ,mean2, variance, skew, kurt
		rv = st.lognorm(shape[i], loc=mean[i], scale=scale[i])
		plt.plot(rv.pdf(x), linewidth=4, label='$\mu=%0.1f, \sigma=%0.1f $' %(mean[i], shape[i]))
	plt.title('Lognormal Distribution', fontsize=26)
	plt.xlabel('X', fontsize=22)
	plt.ylabel('Probability', fontsize=22)
	plt.legend()
	plt.show()


mean = [0, 1 , -2]
variance = [0.2, 0.5, 1, 5]
gaussian_dist(mean, variance)

scale = [0.5, 1, 2, 3, 4]
rayleigh_dist(scale)

shape = [0.5, 1, 2, 3, 5, 7.5, 9]
scale = [1, 2, 2, 2, 1, 1, 0.5]
gamma_dist2(shape, scale)
gamma_dist(shape, scale)

mu = [0, 0, 0, 1, 2]
sigma = [0.2, 0.5, 1, 2, 5]
lognormal_dist2(mu, sigma)
lognormal_dist(mu, sigma)
