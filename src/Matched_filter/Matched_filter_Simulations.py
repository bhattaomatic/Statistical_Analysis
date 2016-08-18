#!/usr/bin/env python

"""
Author: Abhishek Bhatta

This is the final file for matched filtering using various different types of data

Check for different values of reflected path in case of a specific direct path signal.
There is some anomalies.

"""

import numpy as np
import matplotlib.pyplot as plt
import time
import my_signal


print __doc__				# Printing out the details of this program at the beginning of the execution.

m = my_signal.mysignal()	# creating an instance of the class my_signal.

# MATCHED FILTERING

# Variable Declarations
fc = 1						# Frequency of operation.
wc = 2 * np.pi * fc			# Angular frequency.
phi = 0						# Phase of the transmitted signal.
#gh = 1						# Supposed to be rectangular function to truncate the signal Used for calculated value.
ut = np.exp(1j*wc*phi)		# Complex envelope of the signal.
td = 0.1					# Direct path signal.
tr = np.arange(0,1,0.1)		# The reflected path signal.
#tr = [0.1, 0.3, 0.5, 0.75, 1, 1.2, 1.4, 1.6, 2]	# The reflected path signal.
#tr = [0.6, 1.6]	# The reflected path signal Causes trouble when td = 0.1.
#tr = [0.5, 1.5, 2.5, 3.5]	# The reflected path signal Causes trouble when td = 0.0.

# Specific variables for sinusoidal transmit signal
T = 2						# total duration for the signal to be transmitted.
t = np.arange(0,T,0.01)		# time variable to sample the tx signal.
matched = m.tx_signal(ut, wc, (T-t), phi)		# Matched Filter to the transmitted signal.
mafi = np.conj(matched)		# Complex conjugated output of the matched filter.


plt.ion()				# Initializes interactive mode for plot.
for i in range(0,len(tr)):
	Rx_signal = m.tx_signal(ut, wc, t-td, phi) + m.tx_signal(ut, wc, t-tr[i], phi) 		# Received signal with direct path and one reflected path signal.
	output = np.convolve(Rx_signal, mafi)			# Output of the matched filter.
	abs_out_real = np.abs(np.real(output))			# Taking absolute of the real part of the matched filter output.
# Plotting
	plt.plot(np.multiply(abs_out_real,1/np.max(abs_out_real)), label = '%s' %tr[i], linewidth =1)	# Plots the matched filter output.
#	plt.ylim([0, 1.2])	# Set the Y axis limit.
	plt.title('Sine wave with td and tr', fontsize=25)
	plt.legend()		# Prints the legend in the plot.
	plt.draw()			# Draws the graph in the current figure, useful in interactive mode.
#	m.pause()			# Waits for <ENTER> key press to continue if activated disable time.sleep().
	time.sleep(1)		# Waits for 1 second before continuing.
	plt.clf()			# This clears the previous plot in the figure, comment this to see all plots.
	plt.show()			# Display the plot.

plt.ioff()				# Intreactive mode off.

# Specific variables when Barker code is used as transmit signal with BPSK modulation.
T_barker = 1						# total duration.
t_barker = np.arange(0,T_barker,0.1)		# time variable to sample the signal at proper instance.
barker = [1,1,1,1,1,0,0,1,1,0,1,0,1]

BPSK_transmit = m.barker_tx_signal(barker, wc, t_barker, phi)
matched_BPSK = np.flipud(BPSK_transmit)
BPSK_receive_td = m.barker_tx_signal(barker, wc, (t_barker-td), phi)

#fig = plt.figure()
#ax1 = fig.add_subplot(211)
#ax1.plot(barker_code,'r', label='Barker Code')
#plt.legend()
#ax2 = fig.add_subplot(212)
#ax2.plot(BPSK_transmit, 'g', label='BPSK')
#plt.legend()
#plt.show()


plt.ion()				# Initializes interactive mode in the plot.
for i in range(0,len(tr)):
	BPSK_receive_tr = m.barker_tx_signal(barker, wc, (t_barker-tr[i]), phi) # Received signal with just one reflected path.
	BPSK_receive = BPSK_receive_tr + BPSK_receive_td	# Rx signal with direct path and one reflected path.
	output = np.convolve(matched_BPSK, BPSK_receive)	# Output of the matched filter
	abs_out_real = np.abs(np.real(output))			# Taking absolute of the real part of the matched filter output.
# Plotting
	plt.plot(np.multiply(abs_out_real,1/np.max(abs_out_real)), label = '%s' %tr[i], linewidth =1)	# Plots the figure.
	plt.title('Barker Code 13 with td and tr', fontsize=25)
#	plt.ylim([0, 1.2])	# Set the Y axis limit.
	plt.legend()		# Prints the legend in the plot.
	plt.draw()			# Draws the graph in the current figure, useful in interactive mode.
#	m.pause()				# Waits for <ENTER> key press to continue, if enabled comment the time.sleep() command.
	time.sleep(1)		# Waits for 1 second before continuing.
	plt.clf()			# This clears the previous plot in the figure, comment this to see all plots.
	plt.show()			# Shows the plot.

plt.ioff()				# Intreactive mode off.
#plt.show()

# GSM Training Sequence based simulations
train_seq = [0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1];   #Training Sequence(1 of 8 available in GSM)
#train_seq = [1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0]		# usually in communication system the central 16 bits of the training sequence is used.
# Needed to make the time parameter matrix of same length.
if len(train_seq) == 16:
	T_train_seq = 1.6			# total duration for the signal to be transmitted.
elif len(train_seq) == 26:
	T_train_seq = 2.1			# total duration for the signal to be transmitted.
sps = 4
ts = T_train_seq/sps
t = np.arange(0,T_train_seq,0.01)		# time variable to sample the tx signal.
BT = 0.3
GMSK_transmit = m.gsm_train_seq(train_seq,BT,sps,T_train_seq, t, wc,ts)

GMSK_receive_td = m.gsm_train_seq(train_seq,BT,sps,T_train_seq, (t-td), fc,ts)
matched_gmsk = np.flipud(GMSK_transmit)


plt.ion()				# Initializes interactive mode in the plot.
for i in range(0,len(tr)):
	GMSK_receive_tr = m.gsm_train_seq(train_seq,BT,sps,T_train_seq, (t-tr[i]), wc,ts) # Received signal with just one reflected path.
	GMSK_receive = GMSK_receive_tr + GMSK_receive_td	# Rx signal with direct path and one reflected path.
	output = np.convolve(matched_gmsk, GMSK_receive)	# Output of the matched filter
	abs_out_real = np.abs(np.real(output))			# Taking absolute of the real part of the matched filter output.
# Plotting
	plt.plot(np.multiply(abs_out_real,1/np.max(abs_out_real)), label = '%s' %tr[i], linewidth =1)	# Plots the figure.
	plt.title('Training Sequence with td and tr', fontsize=25)
#	plt.ylim([0, 1.2])	# Set the Y axis limit.
	plt.legend()		# Prints the legend in the plot.
	plt.draw()			# Draws the graph in the current figure, useful in interactive mode.
	m.pause()				# Waits for <ENTER> key press to continue, if enabled comment the time.sleep() command.
#	time.sleep(1)		# Waits for 1 second before continuing.
	plt.clf()			# This clears the previous plot in the figure, comment this to see all plots.
	plt.show()			# Shows the plot.
#m.pause()
plt.ioff()				# Intreactive mode off.

