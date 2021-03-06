import numpy as np
from scipy import special
#import matplotlib.pyplot as plt

class mysignal(object):
	"""
Author: Abhishek Bhatta
	
This contains description of all the transmit signals generated to calculate the matched filter and ambiguity function.
	
	"""
####################################### Defining Various Functions #######################################

	def __init__(self):
#		print mysignal.__doc__
		print "Starting the function"

	def pause(self):
		programPause = raw_input("Press the <ENTER> key to continue...")

####################################### TX signal with sine wave (no modulation) #######################################

	def tx_signal(self,complex_env, angular_freq, time, phase):
		Tx_signal = np.real(complex_env*np.exp(1j*angular_freq*time+phase))		# Transmitted signal.
		return Tx_signal

####################################### TX signal with Barker Code (BPSK modulation) #######################################

	def barker_tx_signal(self,barker, angular_freq, t, phase, complex_env):
		p1 = 0
		p2 = np.pi
		T = len(barker)
		time = []
		BPSK = []
		barker_code = []
		carrier_signal = []
		for i in range(0,T):
			if barker[i] == 0:
				bit = np.zeros((1,len(t)))
			else:
				bit = np.ones((1,len(t)))
			barker_code = np.append(barker_code, bit)
		#Generating the BPSK signal
			if barker[i] == 0:
				bit = complex_env*np.sin(angular_freq*t+p1);
			else:
				bit = complex_env*np.sin(angular_freq*t+p2);
		
			BPSK = np.append(BPSK, bit);
		return BPSK

####################################### TX signal with training sequence (GMSK modulation) #######################################

	def gsm_train_seq(self,train_seq,BT,sps,T, t, wc,ts, complex_env):
		train_seq_upsampled = train_seq
		gauss = self.gaussian_pulse_shaping_filter(BT,T,ts)
		for i in range(0,len(train_seq)):
			if train_seq[i] == 0:
				bit = np.zeros((1,sps))
			else:
				bit = np.ones((1,sps))
			train_seq_upsampled = np.append(train_seq_upsampled, bit)

		nrz_train_seq = np.zeros(len(train_seq_upsampled))
		for k in range(0,len(train_seq_upsampled)):
			if train_seq_upsampled[k] == 0:
				nrz_train_seq[k] = -1
			elif train_seq_upsampled[k] == 1:
				nrz_train_seq[k] = 1

		nrz_gauss = np.convolve(gauss,nrz_train_seq) #train_seq_upsampled
		nrz_int = np.cumsum(nrz_gauss);                #Integrating the signal
		nrz_gmsk = np.exp(1j*nrz_int);           #Generating the signal
		I_data = np.imag(nrz_gmsk);
		Q_data = np.real(nrz_gmsk);
		GMSK = complex_env*(np.cos(wc*t)*Q_data)-(np.sin(wc*t)*I_data)	#The signal to be transmitted
		return GMSK

####################################### Gaussing pulse shaping filter ####################################### 
	def gaussian_pulse_shaping_filter(self,BT,T,ts):
		#T = 0.05
		sps = 18
		ts = T/sps
#		t = np.arange(-T,T,ts)
		t = np.linspace(-T,T,num=27*3)
		B = BT/T
		alpha = (2*np.pi*B)/np.sqrt(np.log(2))
		gauss = (1/(2*T))*(0.5*special.erfc((alpha*(2*t-(T/2)))/np.sqrt(2)) - 0.5*special.erfc((alpha*(2*t+(T/2)))/np.sqrt(2)))
		K = (np.pi/2)/np.sum(gauss)
		y = K * gauss
		return y





