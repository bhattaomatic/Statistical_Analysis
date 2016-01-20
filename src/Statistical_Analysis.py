#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as sp
from sh import cd

class Statistical_Analysis:

# Functions

	def gauss_fit_2(self, s, bin1):
		"""Gaussian distribution fitting, using norm.fit(). Parameters taken are input data and the number of bins needed to plot"""
		mean, std = sp.norm.fit(s)		# Distribution fitting
		count, bins, ignored = plt.hist(s, bin1, normed=True)	# Extracting the parameters from the histogram
		pdf_fitted = sp.norm.pdf(bins, loc=mean, scale=std)
		print " "
		print "Gaussian Distribution Extraction"
		print "Extracted mean is :", mean
		print "Extracted standard deviation is :",std
		print " "
		plt.plot(bins, pdf_fitted, linewidth=2, color='k', label='Gaussian')
		plt.title("Gaussian Distribution Estimation")
		plt.show()
		return pdf_fitted
	
	def rayl_fit_2(self, s, bin1):
		"""Rayleigh distribution fitting, using rayleigh.fit(). Parameters taken are input data and the number of bins needed to plot"""
		mean, std = sp.rayleigh.fit(s)		# Distribution fitting
		count, bins, ignored = plt.hist(s, bin1, normed=True)	# Extracting the parameters from the histogram
		pdf_fitted = sp.rayleigh.pdf(bins, loc=mean, scale=std)
		print " "
		print "Rayleigh Distribution Extraction"
		print "Extracted mean is :", mean
		print "Extracted mode is :", std
		print " "
		plt.plot(bins, pdf_fitted, linewidth=2, color='r', label='Rayleigh')
		plt.title("Rayleigh Distribution Extraction")
		plt.show()
		return pdf_fitted

	def curve_fitting(self, d, bin1, name, no):
		"""Find the best fit curve for the given dataset and save it in the location given in savefig"""
		for i in range(0,no):
			s = d[:,i]
			dist_names = ['rayleigh', 'norm', 'lognorm', 'gamma']# , 'rice']
			colors = ['b', 'g', 'r', 'y', 'm']
			for dist_name,col in zip(dist_names,colors):
				dist = getattr(sp, dist_name)
				param = dist.fit(s)
				count, bins, ignored = plt.hist(s, bin1, normed=True)	# Extracting the parameters from the histogram
				pdf_fitted = dist.pdf(bins, *param[:-2], loc=param[-2], scale=param[-1])
				plt.plot(bins, pdf_fitted, linewidth=2, color=col , label=dist_name)
				plt.title('Distribution Fitting %s' %name, fontsize=25)
				plt.xlabel("Filter tap values", fontsize=20)
				plt.ylabel("Probability Distribution", fontsize=20)
				plt.legend(fontsize = 'xx-large')
				plt.savefig('/home/abhishek/Results/comparison_all_sets/Curve fitting/plots/hist_%s_index_%d' %(name,i))
	#		plt.show()
			plt.close()


	def fitted_data(self, d, bin1, name, no):
		""" Find the parameters of the best fit curve and save the values in a file."""
		f = open('/home/abhishek/Results/comparison_all_sets/Curve fitting/data/%s' %(name), 'w')	
		for i in range(0,no):
			s = d[:,i]
			dist_names = ['rayleigh', 'norm', 'lognorm', 'gamma']
			colors = ['b', 'g', 'r', 'y', 'm']
			f.write('INDEX %d \n' %i)
			for dist_name,col in zip(dist_names,colors):
				dist = getattr(sp, dist_name)
				param = dist.fit(s)
				count, bins, ignored = plt.hist(s, bin1, normed=True)	# Extracting the parameters from the histogram
				f.write(" Params %s \nIgnored %s \n" %(param, ignored))
			f.write('\n \n \n')
	
		f.close()
	
	def fitting_parameter_plot(self, d, bin1, name, no):
		"""Find the shape, scale and location parameters of a file"""
		for i in range(0,no):
			s = d[:,i]
			dist_names = ['rayleigh', 'norm', 'lognorm', 'gamma']
			colors = ['b', 'g', 'r', 'y', 'm']
			for dist_name,col in zip(dist_names,colors):
				dist = getattr(sp, dist_name)
				shape[i], location[i], scale[i] = dist.fit(s)
		return shape, location, scale
	
	
	
	

	def hist_save(self, d, bin1, name, no):
		""" save the plotted figures to a particular folder given in the savefig command """
		for i in range(0,no):
			s = d[:,i]
			plt.hist(s, bin1, normed=True, color='c')	# Extracting the parameters from the histogram
			plt.title('Probability Distribution Fnction of %s' %name, fontsize=20)
			plt.xlabel("Filter tap values", fontsize=20)
			plt.ylabel("Probability Distribution", fontsize=20)
#			plt.xlim(0,0.10)
			plt.ylim(0,100)
#			plt.legend(fontsize = 'xx-large')
			plt.savefig('/home/abhishek/Results/comparison_all_sets/Curve fitting/test/set_1/hist_%s_index_%d' %(name,i))
			plt.close()
#			plt.show()

# End of the functions


