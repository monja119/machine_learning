import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy import fftpack

#  model
def f(x):
    return 4*np.sin(5*x) + 4*np.sin(2*x)


def processing():
    plt.figure()
    # default values
    x = np.linspace(0, 10, 100)
    y = f(x)
    plt.scatter(x, y)

    #   elimination de la tendance linear
    new_y = signal.detrend(y)
    plt.plot(x, new_y, c='red')

    #  transformation fourier
    fourrier = fftpack.fft(y)
    power = np.abs(fourrier)
    frequences = fftpack.fftfreq(y.size)
    plt.plot(np.abs(frequences), power, c='green')
    plt.show()


processing()
