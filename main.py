import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def run():
    plt.figure()
    # values not interpolated
    x = np.linspace(0, 20, 100)
    y = np.random.randint(0, 100, 100)
    plt.plot(x, y)

    # values interpolated
    f = interp1d(x, y, kind='nearest') # linear, nearest, cubic
    new_x = np.linspace(0, 20, 5)
    new_y = f(new_x)

    plt.plot(new_x, new_y, c='red')

    plt.title('my data')
    plt.show()


run()
