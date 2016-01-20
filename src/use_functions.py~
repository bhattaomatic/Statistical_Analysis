#!/usr/bin/env python

import numpy as np
#import matplotlib.pyplot as plt
#import scipy
#import scipy.stats as sp
from sh import cd
from Statistical_Analysis import Statistical_Analysis



cd('../data')
test_data = np.loadtxt('chan_imp_resp_normal_abs.txt')


hello = len(test_data)
test_data = np.reshape(test_data[0:hello],(hello/40,40))


face = Statistical_Analysis()
name = [ 'test_data']

for names in name:
	plotting = face.rayl_fit_2(eval(names),100)
#	plotting = face.gauss_fit_2(eval(names),100)
#	plotting = face.curve_fitting(eval(names),100, names, 1)
#	plotting = face.hist_save(eval(names),100, names, 1)
