import numpy as np
from scipy import special

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
		return BPSK

	# Defining the training sequence based GMSK transmit signal.
	def gsm_train_seq(self,train_seq,BT,sps,T, t, wc,ts):
		train_seq_upsampled = train_seq#[]
		t_upsampled = []
		t_gauss = np.arange(0,T,ts)		# time variable to sample the gaussian filter.
		gauss = self.gaussian_pulse_shaping_filter(BT,T,t_gauss,ts)
		for i in range(0,len(train_seq)):
			if train_seq[i] == 0:
				bit = np.zeros((1,sps))
			else:
				bit = np.ones((1,sps))
			train_seq_upsampled = np.append(train_seq_upsampled, bit)

#		nrz_train_seq = np.zeros(len(train_seq_upsampled))
#		for k in range(0,len(train_seq_upsampled)):
#			if train_seq_upsampled[k] == 0:
#				nrz_train_seq[k] = -1
#			elif train_seq_upsampled[k] == 1:
#				nrz_train_seq[k] = 1

		nrz_gauss = train_seq_upsampled#np.convolve(gauss,train_seq_upsampled)
		nrz_int = np.cumsum(nrz_gauss);                #Integrating the signal
		nrz_gmsk = np.exp(1j*nrz_int);           #Generating the signal
		I_data = np.imag(nrz_gmsk);
		Q_data = np.real(nrz_gmsk);
		GMSK = (np.cos(wc*t)*Q_data) - (np.sin(wc*t)*I_data)      #The signal to be transmitted
		return GMSK

	def gaussian_pulse_shaping_filter(self,BT,T,t,ts):
		#T = 0.05
		sps = 18
		ts = T/sps
		t = np.arange(-2*T,2*T,ts)
		B = BT/T
		alpha = (2*np.pi*B)/np.sqrt(np.log(2))
		gauss = (1/(2*T))*(0.5*special.erfc((alpha*(2*t-(T/2)))/np.sqrt(2)) - 0.5*special.erfc((alpha*(2*t+(T/2)))/np.sqrt(2)))
		K = (np.pi/2)/np.sum(gauss)
		y = K * gauss
		return y





