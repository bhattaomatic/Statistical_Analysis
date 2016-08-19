#!/usr/bin/env python
"""

Author: Abhishek Bhatta
This code shows the matched filter output in the presence of direct path and
multiple reflected paths.

here 
td = direct path
tr = reflected path

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
#plt.plot(gh)
#plt.show()
to = 0

td = 1
tr1 = 10.7
tr2 = 14.14
Tx_signal = np.real(ut*np.exp(1j*wc*(t+phi)))
#plt.plot(Tx_signal)
#plt.show()

Rx_signal = np.real(ut*np.exp(1j*wc*(t-td)))
Rx_signal1 = np.real(ut*np.exp(1j*wc*(t-td))) + np.real(ut*np.exp(1j*wc*(t-tr1)))
Rx_signal2 = np.real(ut*np.exp(1j*wc*(t-td))) + np.real(ut*np.exp(1j*wc*(t-tr1))) + np.real(ut*np.exp(1j*wc*(t-tr2)))
#plt.plot(Rx_signal)
#plt.show()

matched = gh*(ut*np.exp(1j*wc*(T-t) + phi))
mafi = np.conj(matched)
#plt.plot(mafi)
#plt.show()

output = np.convolve(Rx_signal, mafi)
output1 = np.convolve(Rx_signal1, mafi)
output2 = np.convolve(Rx_signal2, mafi)
#plt.plot(np.abs(output))
#plt.plot(np.abs(output), label= 'td = %s and tr = %s' %(td,tr))
#plt.show()
K = 100
Ku = (K/2)*np.exp(-1j*wc*(to+td+tr1+tr2))

calc1 = Ku*(np.real(np.exp(1j*wc*(T-(t-to-td)))*(t-to)))
calc2 = Ku*(np.real(np.exp(1j*wc*(t-to-td))*(T-t+to)))

calc3 = Ku*(np.real(np.exp(1j*wc*(T-(t-to-td)))*(t-to)) + np.real(np.exp(1j*wc*(T-(t-to-tr1)))*(t-to)))
calc4 = Ku*(np.real(np.exp(1j*wc*(t-to-td))*(T-t+to)) + np.real(np.exp(1j*wc*(t-to-tr1))*(T-t+to)))

calc5 = Ku*(np.real(np.exp(1j*wc*(T-(t-to-td)))*(t-to)) + np.real(np.exp(1j*wc*(T-(t-to-tr1)))*(t-to)) + np.real(np.exp(1j*wc*(T-(t-to-tr2)))*(t-to)))
calc6 = Ku*(np.real(np.exp(1j*wc*(t-to-td))*(T-t+to)) + np.real(np.exp(1j*wc*(t-to-tr1))*(T-t+to)) + np.real(np.exp(1j*wc*(t-to-tr2))*(T-t+to)))


fig = plt.figure(1)
fig.suptitle('Matched filter for different reflected path', fontsize=35)
ax1 = fig.add_subplot(311)
ax1.plot(np.abs(np.real(output)), label='simulated td=%s' %td, linewidth=2, color='r')
ax1.plot(t*100,abs(calc1), label='calculated part 1 td=%s' %td, linewidth=2, color='b')
ax1.plot(t1*100,abs(calc2), label='calculated part 2 td=%s' %td, linewidth=2, color='b')
#ax1.set_ylim([0,1400])
plt.legend()


ax2 = fig.add_subplot(312)
ax2.plot(np.abs(np.real(output1)), label='simulated td=%s, tr1=%s' %(td,tr1), linewidth=2, color='r')
ax2.plot(t*100,abs(calc3), label='calculated part 1 td=%s, tr1=%s' %(td,tr1), linewidth=2, color='b')
ax2.plot(t1*100,abs(calc4), label='calculated part 2 td=%s, tr1=%s' %(td,tr1), linewidth=2, color='b')
#ax2.set_ylim([0,1400])
plt.legend()
plt.ylabel('Amplitude of Matched filter output', fontsize=30)

ax3 = fig.add_subplot(313)
ax3.plot(np.abs(np.real(output2)), label='simulated td=%s, tr1=%s, tr2=%s' %(td,tr1,tr2), linewidth=2, color='r')
ax3.plot(t*100,abs(calc5), label='calculated part 1 td=%s, tr1=%s, tr2=%s' %(td,tr1,tr2), linewidth=2, color='b')
ax3.plot(t1*100,abs(calc6), label='calculated part 2 td=%s, tr1=%s tr2=%s' %(td,tr1,tr2), linewidth=2, color='b')
#ax3.set_ylim([0,1400])
plt.legend()

plt.xlabel('Time', fontsize=30)

plt.show()




