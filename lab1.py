import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2, ifft2, fftshift
from scipy.signal import convolve2d

from Functions import *
from gaussfft import gaussfft
from fftwave import fftwave


# Either write your code in a file like this or use a Jupyter notebook.
#
# A good idea is to use switches, so that you can turn things on and off
# depending on what you are working on. It should be fairly easy for a TA
# to go through all parts of your code though.

if __name__ == '__main__':
    p,q = 5, 0
    Fhat = np.zeros((128, 128))
    Fhat[p,q] = 1
    # showgrey(Fhat)

    F = ifft2(Fhat)
    Fabsmax = np.max(np.abs(F))
    showgrey(np.real(F), True, 64, -Fabsmax, Fabsmax)
    showgrey(np.imag(F), True, 64, -Fabsmax, Fabsmax)
    showgrey(np.abs(F), True, 64, -Fabsmax, Fabsmax)
    showgrey(np.angle(F), True, 64, -np.pi, np.pi)