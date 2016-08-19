#!/usr/bin/env python

"""
Author: Abhishek Bhatta

This is a basic matched filter implementation in which the received signal is
exactly the same as the transmitted signal. The calculated values are divided
in two parts because the slope of the graph changes.

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
t2 = np.arange(0,2*T-0.01,0.01)
phi = 0
gh = 1
ut = gh*np.exp(1j*wc*phi)
#plt.plot(gh)
#plt.show()
Tx_signal = np.real(ut*np.exp(1j*wc*t+phi))
#plt.plot(Tx_signal)
#plt.show()
Rx_signal = Tx_signal
#plt.plot(Rx_signal)
#plt.show()
matched = gh*(ut*np.exp(1j*wc*(T-t) + phi))
mafi = np.conj(matched)
#plt.plot(mafi)
#plt.show()
output = np.convolve(Rx_signal, mafi)
abs_out_real = np.abs(np.real(output))
plt.plot(abs_out_real, label = 'Simulated', linewidth =2)
#plt.plot(np.abs(output), label= 'td = %s and tr = %s' %(td,tr))
#plt.show()
calc1 = 50*np.real(np.exp(1j*wc*(T-t))*(t))
calc2 = 50*np.real(np.exp(1j*wc*(t))*(T-t))

plt.plot(t*100,abs(calc1), label='Calculated Part 1', linewidth =2)

plt.plot(t1*100,abs(calc2), label= 'Calculated part 2', linewidth =2)
plt.title('Matched Filter Simple Case', fontsize=30)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Amplitude', fontsize=20)
plt.legend()
plt.show()


#plt.plot(matched)
#plt.plot(Tx_signal)
#plt.show()







