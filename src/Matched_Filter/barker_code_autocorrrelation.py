#!/usr/bin/python
"""
This is a simple code to check the autocorrelation of barker code without any modultaion.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math as m

print __doc__

barker_code = [1,1,1,1,1,-1,-1,1,1,-1,1,-1,1]
#barker_code = [1,1,1,1,1,0,0,1,1,0,1,0,1]




mafi = np.flipud(barker_code)

output = np.convolve(mafi, barker_code)

plt.title('Barker Code', fontsize=30)
plt.plot(output, linewidth=2, label='Autocorrelation')
plt.legend()
plt.show()
