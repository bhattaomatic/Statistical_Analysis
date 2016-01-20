#!/usr/bin/env python
from sh import cd
import numpy as np
import matplotlib.pyplot as plt

# Import the data
cd('../data')
test_data = np.loadtxt('chan_imp_resp_normal_abs.txt')
test_data_iq = np.loadtxt('chan_imp_resp_normal.txt')

# Plots Time Domain
fig1 = plt.figure(1,figsize=(12.88, 7))
ax1 = fig1.add_subplot(111)
ax1.plot(test_data[80:120], linewidth=5)
plt.xlabel('Filter Taps', fontsize=22)
plt.ylabel('Amplitude', fontsize=22)
plt.title('Time Domain Absolute Channel Impulse Response', fontsize=22)

fig2 = plt.figure(2,figsize=(12.88, 7))
ax2 = fig2.add_subplot(111)
plt.plot(test_data_iq[80:120,:], linewidth=5)
plt.xlabel('Filter Taps', fontsize=22)
plt.ylabel('Amplitude', fontsize=22)
plt.title('Time Domain IQ Channel Impulse Response', fontsize=22)
plt.show()

