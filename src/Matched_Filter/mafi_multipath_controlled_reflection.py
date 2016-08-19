#!/usr/bin/env python
"""
Author: Abhishek Bhatta
This code shows the matched filter output with only the direct path delay 
which changes with simulation time. Also it shows the calculated values 
and their similarities to the simulated values.

here td = direct path
"""
import numpy as np
import matplotlib.pyplot as plt


print __doc__
# General Case of Matched Filtering
fc = 1/np.pi
wc = 2 * np.pi * fc
T = 10
t = np.arange(0,T,0.01)
t1 = np.arange(T,2*T,0.01)
phi = 0
gh = 1
ut = gh*np.exp(1j*wc*phi)
to = 0

td = [0.01, 1, 1.1]

Tx_signal = np.real(ut*np.exp(1j*wc*(t+phi)))

matched = gh*(ut*np.exp(1j*wc*(T-t) + phi))
mafi = np.conj(matched)
color = ['b', 'g', 'r']

for i, col in zip(range(0,len(td)),color):
	Rx_signal = np.real(ut*np.exp(1j*wc*(t-td[i])))
	output = np.convolve(Rx_signal, mafi)
	K = 100
	Ku = (K/2)*np.exp(-1j*wc*(to+td[i]))
	calc1 = Ku*(np.real(np.exp(1j*wc*(T-(t-to-td[i])))*(t-to)))
	calc2 = Ku*(np.real(np.exp(1j*wc*(t-to-td[i]))*(T-t+to)))
	fig = plt.figure(1)
	fig.suptitle('Matched filter', fontsize=35)
	ax = fig.add_subplot(211)
	ax.plot(np.abs(np.real(output)), label='simulated td=%s' %td[i], linewidth=2, color=col)
	plt.title("Simulated", fontsize=25)
#	plt.xlabel('Time', fontsize=30)
	plt.legend()
#	fig.suptitle('Matched filter Calculated', fontsize=35)
	ax1 = fig.add_subplot(212)
	ax1.plot(t*100,abs(calc1), label='calculated part 1 td=%s' %td[i], linewidth=2, color= col)
#	ax1.plot(t1*100,abs(calc2), label='calculated part 2 td=%s' %td[i], linewidth=2)
	ax1.plot(t1*100,abs(calc2), linewidth=2)
	plt.title("Calculated", fontsize=25)
	plt.xlabel('Time', fontsize=30)
	plt.legend()
plt.show()




