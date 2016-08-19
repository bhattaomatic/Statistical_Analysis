#!/usr/bin/python
"""
Working GMSK modulation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

def gaussian_pulse_shaping_filter(BT,sps,T):
	T = 0.05
	sps = 18
	Ts = T/sps
	t = np.arange(-2*T,2*T,Ts)
	B = BT/T
	alpha = (2*np.pi*B)/np.sqrt(np.log(2))
	gauss = (1/(2*T))*(0.5*special.erfc((alpha*(2*t-(T/2)))/np.sqrt(2)) - 0.5*special.erfc((alpha*(2*t+(T/2)))/np.sqrt(2)))
	K = (np.pi/2)/np.sum(gauss)
	y = K * gauss
	return y

BT = 0.3
T = 3.692e-6
sps = 36
Ts = T/sps
t = np.arange(-2*T,2*T,Ts)
z = gaussian_pulse_shaping_filter(BT,sps,T)

#plt.plot(z)
#plt.show()
