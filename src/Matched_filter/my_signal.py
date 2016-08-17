import numpy as np


class mysignal(object):
	"""
Author: Abhishek Bhatta
	
This contains description of all the transmit signals generated to calculate the matched filter and ambiguity function.
	
	"""
	# Defining Various Functions
	def __init__(self):
#		print mysignal.__doc__
		print "Starting the function"

	def pause(self):
		programPause = raw_input("Press the <ENTER> key to continue...")

	def tx_signal(self,complex_env, angular_freq, time, phase):
		Tx_signal = np.real(complex_env*np.exp(1j*angular_freq*time+phase))		# Transmitted signal.
		return Tx_signal

	def barker_tx_signal(self,barker, angular_freq, t, phase):
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
				bit = np.sin(angular_freq*t+p1);
			else:
				bit = np.sin(angular_freq*t+p2);
		
			BPSK = np.append(BPSK, bit);
		
			time = np.append(time, t)
		return BPSK
