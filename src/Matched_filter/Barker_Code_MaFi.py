#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math as m

#barker_code = [1,1,1,1,1,-1,-1,1,1,-1,1,-1,1]
barker = [1,1,1,1,1,0,0,1,1,0,1,0,1]
#barker_code = [1,2,3,4,5]

T = len(barker)
fc = 2					# Frequency of operation.
wc = 2 * np.pi * fc			# Angular frequency.

sampling_time = 0.01
t = np.arange(0,1,sampling_time)		# time variable.
p1 = 0
p2 = np.pi

time = []
barker_code = []
BPSK = []
carrier_signal = []
for i in range(0,T):
	if barker[i] == 0:
		bit = np.zeros((1,len(t)))
	else:
		bit = np.ones((1,len(t)))

	barker_code = np.append(barker_code, bit)

# Generating the binary phase coded signal

#Generating the BPSK signal
	if barker[i] == 0:
		bit = np.sin(wc*t+p1);
	else:
		bit = np.sin(wc*t+p2);

	BPSK = np.append(BPSK, bit);

#Generating the carrier wave
	carrier = np.sin(wc*t);
	carrier_signal = np.append(carrier_signal, carrier)

	time = np.append(time, t)

	td = 0.1
	if barker[i] == 0:
		bit = np.zeros((1,len(t)))
	else:
		bit = np.ones((1,len(t)))

	barker_code = np.append(barker_code, bit)

# Generating the binary phase coded signal

#Generating the BPSK signal
	if barker[i] == 0:
		bit = np.sin(wc*(t-td)+p1);
	else:
		bit = np.sin(wc*(t-td)+p2);

	BPSK_td = np.append(BPSK, bit);

	tr = 0.5
	if barker[i] == 0:
		bit = np.zeros((1,len(t)))
	else:
		bit = np.ones((1,len(t)))

	barker_code = np.append(barker_code, bit)

# Generating the binary phase coded signal

#Generating the BPSK signal
	if barker[i] == 0:
		bit = np.sin(wc*(t-tr)+p1);
	else:
		bit = np.sin(wc*(t-tr)+p2);

	BPSK_tr = np.append(BPSK, bit);
	t = t + 1

"""
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(time,barker_code,'r', label='Digital Signal')
plt.legend()
ax2 = fig.add_subplot(312)
ax2.plot(time,BPSK, 'g', label='BPSK')
plt.legend()
ax3 = fig.add_subplot(313)
ax3.plot(time,carrier_signal,'b', label='Carrier Signal')
plt.legend()
plt.show()
"""

matched_filter = np.flipud(BPSK)

#print "barker ",barker_code, "\nmafi ", matched_filter

fig = plt.figure()
ax = fig.add_subplot(311)
ax1 = fig.add_subplot(312)
ax2 = fig.add_subplot(313)
output = np.convolve(BPSK, matched_filter)
ax.plot(np.multiply(np.abs(output),1/np.max(np.abs(output))), linewidth=2, label= 'mafi')

#n = len(barker_code)
#output1 = np.correlate(barker_code, barker_code, mode='full')[-2*n:]
#plt.plot(output1, linewidth=2, label= 'autocorrelation')
#plt.legend()

#plt.show()


output_td = np.convolve(BPSK_td, matched_filter)
ax1.plot(np.multiply(np.abs(output_td),1/np.max(np.abs(output_td))), linewidth=2, label= 'td=0.1')
output_tr = np.convolve(BPSK_tr, matched_filter)
ax2.plot(np.multiply(np.abs(output_tr),1/np.max(np.abs(output_tr))), linewidth=2, label= 'tr=0.5')
ax.legend()
ax1.legend()
ax2.legend()
plt.show()
