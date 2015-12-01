#!/usr/bin/env python

import numpy as np
#import matplotlib.pyplot as plt
#import scipy
#import scipy.stats as sp
from sh import cd
from masters_python import Masters_python



cd('/home/abhishek/Results/Day 17 Nov 2 2015 HotDay home/10')
car = np.loadtxt('chan_imp_resp_normal_abs.txt')
cd('/home/abhishek/Results/Day 17 Nov 2 2015 HotDay home/11')
car1 = np.loadtxt('chan_imp_resp_normal_abs.txt')

hello = len(car)
car = np.reshape(car[0:hello],(hello/40,40))
car1 = np.reshape(car1[0:hello],(hello/40,40))

face = Masters_python()
name = [ 'car', 'car1']

for names in name:
	plotting = face.rayl_fit_2(eval(names),100)
#	plotting = face.gauss_fit_2(eval(names),100)
#	plotting = face.curve_fitting(eval(names),100, names, 1)
#	plotting = face.hist_save(eval(names),100, names, 1)
