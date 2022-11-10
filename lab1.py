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


def ex1():
    fftwave(5, 65)
    # fftwave(9, 5)
    # fftwave(17, 9)
    # fftwave(17, 121)
    # fftwave(5, 1)
    # fftwave(125, 1)

def ex2(use_log=True):
    F = np.concatenate([np.zeros((56,128)), np.ones((16,128)), np.zeros((56,128))])
    G = F.T
    H = F + 2*G
    fig = plt.figure()
    _ = fig.add_subplot(3, 3, 1)
    showgrey(F, False)
    _ = fig.add_subplot(3, 3, 2)
    showgrey(G, False)
    _ = fig.add_subplot(3, 3, 3)
    showgrey(H, False)
    Fhat = fft2(F)
    Ghat = fft2(G)
    Hhat = fft2(H)

    _ = fig.add_subplot(3, 3, 4)
    showgrey(np.log(1 + np.abs(Fhat)), False)

    _ = fig.add_subplot(3, 3, 5)
    showgrey(np.log(1 + np.abs(Ghat)), False)

    _ = fig.add_subplot(3, 3, 6)
    showgrey(np.log(1 + np.abs(Hhat)), False)

    _ = fig.add_subplot(3, 3, 7)
    shift_Fhat = fftshift(Fhat)
    if use_log:
        showgrey(np.log(1 + np.abs(shift_Fhat)), False)
    else:
        showgrey(np.abs(shift_Fhat), False)

    _ = fig.add_subplot(3, 3, 8)
    shift_Ghat = fftshift(Ghat)
    if use_log:
        showgrey(np.log(1 + np.abs(shift_Ghat)), False)
    else:
        showgrey(np.abs(shift_Ghat), False)

    _ = fig.add_subplot(3, 3, 9)
    shift_Hhat = fftshift(Hhat)
    if use_log:
        showgrey(np.log(1 + np.abs(shift_Hhat)), False)
        # showfs(Hhat, False)
    else:
        showgrey(np.abs(shift_Hhat), False)

    plt.show()

def ex3():
    F = np.concatenate([np.zeros((56, 128)), np.ones((16, 128)), np.zeros((56, 128))])
    G = F.T
    Ghat = fft2(F)
    Fhat = fft2(F)
    showgrey(F)
    showgrey(G)
    showgrey(F * G)
    showfs(fft2(F*G))
    # showfs(fft2(convolve2d((Fhat),(Ghat))))

    # fig = plt.figure()
    # fig.add_subplot(3, 3, 1)
    # showgrey(F)
    # _ = fig.add_subplot(3, 3, 2)
    # showgrey(F)
    # _ = fig.add_subplot(3, 3, 3)
    # showgrey(F * G)
    # plt.show()



def ex4():
    F = np.concatenate([np.zeros((60, 128)), np.ones((8, 128)), np.zeros((60, 128))]) * \
        np.concatenate([np.zeros((128, 48)), np.ones((128, 32)), np.zeros((128, 48))], axis=1)

    # showgrey(F)
    # showfs(fft2(F))
    alpha = [30, 60, 90]
    for angle in alpha:
        G = rot(F, angle)
        showgrey(G)
        Ghat = fft2(G)
        showfs(Ghat)
        Hhat = rot(fftshift(Ghat), -angle)
        showgrey(np.log(1 + abs(Hhat)))

if __name__ == '__main__':

    exercise = 4

    if exercise == 1:
        ex1()
    elif exercise == 2:
        # ex2()
        ex2(use_log=True)
    elif exercise == 3:
        ex3()
    elif exercise == 4:
        ex4()