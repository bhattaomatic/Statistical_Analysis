#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as st

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)


# Gaussian Distribution
gauss_mean = [0, 1 , -2]
gauss_variance = [0.2, 1, 5]
gauss_sigma = np.sqrt(gauss_variance)
gauss_x = np.linspace(-3-len(gauss_mean),3+len(gauss_mean),100)
for i in range(len(gauss_sigma)):
	ax1.plot(gauss_x,mlab.normpdf(gauss_x, gauss_mean[0], gauss_sigma[i]), linewidth=4, label='$\mu=0, \sigma^2 =%0.1f$' %gauss_variance[i])
for j in range(1,len(gauss_mean)):
	ax1.plot(gauss_x,mlab.normpdf(gauss_x, gauss_mean[j], gauss_sigma[1]), linewidth=4, label='$\mu=%d, \sigma^2=%0.1f$' %(gauss_mean[j], gauss_variance[1]))
ax1.set_title('Gaussian Distribution', fontsize=26)
#ax1.set_xlabel('X', fontsize=22)
ax1.set_ylabel('Probability', fontsize=22)
ax1.set_yscale('log')
ax1.legend(loc='best')


# Rayleigh Distribution
rayl_scale = [0.5, 1, 2, 3, 4]
#mean, variance, skew, kurt = st.rayleigh.stats(moments='mvsk')
rayl_x = np.linspace(0,10,100)
#print mean, variance, skew, kurt
for i in range(len(rayl_scale)):
	rv = st.rayleigh(loc=0,scale=rayl_scale[i])
	ax2.plot(rayl_x,rv.pdf(rayl_x), linewidth=4, label='$\sigma=%0.1f$' %rayl_scale[i])
ax2.set_title('Rayleigh Distribution', fontsize=26)
#ax2.set_xlabel('X', fontsize=22)
ax2.set_ylabel('Probability', fontsize=22)
ax2.set_yscale('log')
ax2.legend(loc='best')


# Gamma Distribution
gamma_shape = [0.5, 1, 2, 3, 5, 7.5, 9]
gamma_scale = [1, 2, 2, 2, 1, 1, 0.5]
gamma_x = np.linspace(0,30,100)
for i in range(len(gamma_scale)):
	rv = st.gamma(gamma_shape[i], loc=0, scale=gamma_scale[i])
	ax3.plot(rv.pdf(gamma_x), linewidth=4, label='$k=%0.1f, \Theta=%0.1f $' %(gamma_shape[i], gamma_scale[i]))
ax3.set_title('Gamma Distribution', fontsize=26)
ax3.set_xlabel('X', fontsize=22)
ax3.set_ylabel('Probability', fontsize=22)
ax3.set_yscale('log')
ax3.legend(loc='best')


# Lognorm Distribution
lognorm_mean = [0, 0, 0, 1, 2]
lognorm_variance = [0.2, 0.5, 1, 2, 5]
lognorm_sigma = np.sqrt(lognorm_variance)
lognorm_x = np.linspace(0,10,100)
lognorm_shape = 1
for i in range(len(lognorm_sigma)):
	rv = st.lognorm(lognorm_shape, loc=lognorm_mean[i], scale=lognorm_sigma[i])
	ax4.plot(rv.pdf(lognorm_x), linewidth=4, label='$\mu=%0.1f, \sigma=%0.1f $' %(lognorm_mean[i], lognorm_variance[i]))
ax4.set_title('Lognormal Distribution', fontsize=26)
ax4.set_xlabel('X', fontsize=22)
ax4.set_ylabel('Probability', fontsize=22)
ax4.set_yscale('log')
ax4.legend()
plt.show()


