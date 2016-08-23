#!/usr/bin/env python

"""
Author: Abhishek Bhatta

This is the final file for Ambiguity function simulation using different types of transmit signals.

The transmit signals here are 
1. Sine wave with no modulation.
2. Barker Code with BPSK modulation.
3. GSM Training Sequence with GMSK modulation.

Check for different values of reflected path in case of a specific direct path signal.
There is some anomalies.

"""

import numpy as np
import time
import my_signal_ambiguity as my_sig
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


print __doc__				# Printing out the details of this program at the beginning of the execution.

m = my_sig.mysignal()	# creating an instance of the class my_signal.

# MATCHED FILTERING

# Variable Declarations
fc = 100						# Frequency of operation.
wc = 2 * np.pi * fc			# Angular frequency.
phi = 0						# Phase of the transmitted signal.
ut = np.exp(1j*wc*phi)		# Complex envelope of the signal.
td = 0.1					# Direct path signal.
tr = np.arange(0,1,0.1)		# The reflected path signal.
#tr = [0.1, 0.3, 0.5, 0.75, 1, 1.2, 1.4, 1.6, 2]	# The reflected path signal.
#tr = [0.6, 1.6]	# The reflected path signal Causes trouble when td = 0.1.
#tr = [0.5, 1.5, 2.5, 3.5]	# The reflected path signal Causes trouble when td = 0.0.


####################################### TX signal with sine wave (no modulation) #######################################

# Specific variables for sinusoidal transmit signal
T = 0.0001						# total duration for the signal to be transmitted.
B = 3/T
fs = 2*B
doppler_shift = np.linspace( -fs, fs, fs/100)	# Doppler Shift of the signal
t = np.linspace(0,T,fs/100)		# time variable to sample the tx signal.
t_mf = np.linspace(-T,T,int((2 * len(t))-1))
Tx_signal = m.tx_signal(ut, wc, t, phi)			# Transmitted Signal.
matched = m.tx_signal(ut, wc, (T-t), phi)		# Matched Filter to the transmitted signal.
mafi = np.conj(matched)		# Complex conjugated output of the matched filter.

abs_out_real = np.zeros(shape=(len(doppler_shift),len(t_mf)))		# Ambiguity Function output


fig, ax = plt.subplots()#(subplot_kw=dict(projection='3d'))
plt.ion()				# Initializes interactive mode for plot.
for i in range(len(tr)):
	for nu in range(len(doppler_shift)):
		utd = np.exp(1j*2*np.pi*doppler_shift[nu]*(t-td))		# Doppler shifted Envolope of direct path signal
		utr = np.exp(1j*2*np.pi*doppler_shift[nu]*(t-tr[i]))	# Doppler shifted Envolope of reflected path signal.
		Rx_signal = m.tx_signal(utd, wc, (t-td), phi) + m.tx_signal(utr, wc, (t-tr[i]), phi)							# Received signal with doppler shift
		output = np.convolve(mafi, Rx_signal)				# Convolution output
		abs_out_real[nu] = np.abs(np.real(output))
		# Zero Doppler cut
#		dop = np.exp(1j*2*np.pi*0*t)
#		Rx_zero_dop = Tx_signal * dop
#		zero_dop_cut = np.convolve(mafi, Rx_zero_dop)
#		zero_dop =+ np.abs(np.real(zero_dop_cut))
		# Zero Time cut
#		zero_time_cut = np.sinc(2*np.pi*doppler_shift[nu] * T/10)
#		zero_time.append(zero_time_cut)

	X, Y = np.meshgrid(t_mf, doppler_shift)
	surf = plt.contour(X, Y, np.multiply(abs_out_real,1/np.max(abs_out_real)), cmap='jet', hold='on')
#	surf = ax.plot_surface(X, Y, abs_out_real, cmap='jet', rstride=10, cstride=10, linewidth=0, antialiased=False, shade=False)
#	surf = plt.imshow(abs_out_real)
	plt.title('Sine wave without modulation td, tr', fontsize=30)
	plt.xlabel('Time', fontsize=20)
	plt.ylabel('Doppler Shift', fontsize=20)
#	ax.set_zlabel('Amplitude', fontsize=20)
	plt.ylim([-15000, 15000])	# Set the Y axis limit (for contour). 
#	plt.ylim([200, 400])	# Set the Y axis limit (for imshow).
	plt.draw()			# Draws the graph in the current figure, useful in interactive mode.
	plt.show()
#	m.pause()			# Waits for <ENTER> key press to continue if activated disable time.sleep().
	time.sleep(0.5)		# Waits for 0.5 second before continuing.
	plt.clf()			# This clears the previous plot in the figure, comment this to see all plots.
plt.ioff()				# Intreactive mode off.



####################################### TX signal with Barker Code (BPSK modulation) #######################################

# Specific variables when Barker code is used as transmit signal with BPSK modulation.
Time = 0.01
T_barker = 1
B_barker = 3/Time
fs_barker = 2*B_barker
ut_barker = 1
td_barker = 0.01
tr_barker = np.arange(0,0.1,0.01)		# The reflected path signal.
doppler_shift_barker = np.linspace( -fs_barker, fs_barker, fs_barker/100)	# Doppler Shift of the signal
t_barker = np.linspace(0,T_barker,fs_barker/10)		# time variable to sample the signal at proper instance.
barker = [1,1,1,1,1,0,0,1,1,0,1,0,1]
t_mf_barker = np.linspace(-T_barker,T_barker,int((26 * len(t_barker))-1))

BPSK_transmit = m.barker_tx_signal(barker, wc, t_barker, phi, ut_barker)
matched_BPSK = np.flipud(BPSK_transmit)

abs_out_real_barker = np.zeros(shape=(len(doppler_shift_barker),len(t_mf_barker)))		# Ambiguity Function output
#fig = plt.figure()
#ax1 = fig.add_subplot(211)
#ax1.plot(barker_code,'r', label='Barker Code')
#plt.legend()
#ax2 = fig.add_subplot(212)
#ax2.plot(BPSK_transmit, 'g', label='BPSK')
#plt.legend()
#plt.show()

fig1, ax1 = plt.subplots()#(subplot_kw=dict(projection='3d'))
plt.ion()				# Initializes interactive mode for plot.
for i in range(len(tr_barker)):
	for nus in range(len(doppler_shift_barker)):
		utd = np.exp(1j*2*np.pi*doppler_shift_barker[nus]*(t_barker-td_barker))		# Doppler shifted Envolope of direct path signal
		BPSK_receive_td = m.barker_tx_signal(barker, wc, (t_barker-td_barker), phi, utd)
		utr = np.exp(1j*2*np.pi*doppler_shift_barker[nus]*(t_barker-tr_barker[i]))	# Doppler shifted Envolope of reflected path signal.
		BPSK_receive_tr = m.barker_tx_signal(barker, wc, (t_barker-tr_barker[i]), phi, utr) # Received signal with just one reflected path.
		BPSK_receive = BPSK_receive_td + BPSK_receive_tr	# Rx signal with direct path and one reflected path.
		output = np.convolve(matched_BPSK, BPSK_receive)	# Output of the matched filter
		abs_out_real_barker[nus] = np.abs(np.real(output))			# Taking absolute of the real part of the matched filter output.
		# Zero Doppler cut
#		dop = np.exp(1j*2*np.pi*0*t)
#		Rx_zero_dop = Tx_signal * dop
#		zero_dop_cut = np.convolve(mafi, Rx_zero_dop)
#		zero_dop =+ np.abs(np.real(zero_dop_cut))
		# Zero Time cut
#		zero_time_cut = np.sinc(2*np.pi*doppler_shift[nu] * T/10)
#		zero_time.append(zero_time_cut)
# Plotting
	X1, Y1 = np.meshgrid(t_mf_barker, doppler_shift_barker)
	surf = plt.contour(X1, Y1, np.multiply(abs_out_real_barker,1/np.max(abs_out_real_barker)), cmap='jet')
#	surf = ax1.plot_surface(X1, Y1, abs_out_real, cmap='jet', rstride=10, cstride=10, linewidth=0, antialiased=False, shade=False)
#	surf = plt.imshow(abs_out_real)
	plt.title('Barker Code 13 with td and tr', fontsize=25)
	plt.xlabel('Time', fontsize=20)
	plt.ylabel('Doppler Shift', fontsize=20)
#	ax.set_zlabel('Amplitude', fontsize=20)
	plt.xlim([-0.1, 0.1])	# Set the Y axis limit (for contour). 
#	plt.ylim([200, 400])	# Set the Y axis limit (for imshow).
	plt.draw()			# Draws the graph in the current figure, useful in interactive mode.
	plt.show()
#	m.pause()			# Waits for <ENTER> key press to continue if activated disable time.sleep().
	time.sleep(0.5)		# Waits for 0.5 second before continuing.
	plt.clf()			# This clears the previous plot in the figure, comment this to see all plots.

plt.ioff()				# Intreactive mode off.


####################################### TX signal with training sequence (GMSK modulation) #######################################

# GSM Training Sequence based simulations
#train_seq = [0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1]   #Training Sequence(1 of 8 available in GSM)
train_seq = [1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0]		# usually in communication system the central 16 bits of the training sequence is used.

# Needed to make the time array of same length as the upsampled training sequence.
if len(train_seq) == 16:
	T_train_seq = 1.6			# total duration for the signal to be transmitted.
elif len(train_seq) == 26:
	T_train_seq = 2.1			# total duration for the signal to be transmitted.

sps = 4
ts = T_train_seq/sps
t = np.arange(0,T_train_seq,0.01)		# time variable to sample the tx signal.
t_mf_train = np.arange(-T_train_seq, T_train_seq-0.011, 0.01)
BT = 0.3
B_train = BT/T_train_seq
fs_train = 2*B_train
ut_train = 1
GMSK_transmit = m.gsm_train_seq(train_seq,BT,sps,T_train_seq, t, wc,ts, ut_train)
doppler_shift_train = np.linspace( -fs_train, fs_train, fs_train*100)	# Doppler Shift of the signal


matched_gmsk = np.flipud(GMSK_transmit)
mafi_gmsk = np.conj(matched_gmsk)
abs_out_real_train = np.zeros(shape=(len(doppler_shift_train),len(t_mf_train)))		# Ambiguity Function output
X2, Y2 = np.meshgrid(t_mf_train, doppler_shift_train)

fig2, ax2 = plt.subplots()
plt.ion()				# Initializes interactive mode in the plot.
for i in range(0,len(tr)):
#	fig2, ax2 = plt.subplots(subplot_kw=dict(projection='3d'))
	for n in range(len(doppler_shift_train)):
		utd_train = np.exp(1j*2*np.pi*doppler_shift_train[n]*(t-td))
		utr_train = np.exp(1j*2*np.pi*doppler_shift_train[n]*(t-tr[i]))
		GMSK_receive_td = m.gsm_train_seq(train_seq,BT,sps,T_train_seq, (t-td), fc, ts, utd_train)
		GMSK_receive_tr = m.gsm_train_seq(train_seq,BT,sps,T_train_seq, (t-tr[i]), wc, ts, utr_train) # Received signal with just one reflected path.
		GMSK_receive = GMSK_receive_tr + GMSK_receive_td	# Rx signal with direct path and one reflected path.
		output = np.convolve(mafi_gmsk, GMSK_receive)	# Output of the matched filter
		abs_out_real_train[n] = np.abs(np.real(output))			# Taking absolute of the real part of the matched filter output.
# Plotting
	surf = plt.contourf(X2, Y2, np.multiply(abs_out_real_train,1/np.max(abs_out_real_train)), linewidth =1, cmap='jet')	# Plots the figure.
#	surf1 = plt.contour(X2, Y2, np.multiply(abs_out_real_train,1/np.max(abs_out_real_train)), colors='k', hold='on')
#	surf = ax2.plot_surface(X2, Y2, abs_out_real_train, cmap='jet', rstride=10, cstride=10, linewidth=0, antialiased=False, shade=False)
	plt.title('Training Sequence with td and tr', fontsize=25)
#	plt.ylim([-15000, 15000])	# Set the Y axis limit.
#	plt.legend()		# Prints the legend in the plot.
#	plt.draw()			# Draws the graph in the current figure, useful in interactive mode.
#	plt.clf()			# This clears the previous plot in the figure, comment this to see all plots.
	plt.show()			# Shows the plot.
	m.pause()				# Waits for <ENTER> key press to continue, if enabled comment the time.sleep() command.
#	time.sleep(1)		# Waits for 1 second before continuing.
#m.pause()
plt.ioff()				# Intreactive mode off.

