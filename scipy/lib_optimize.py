import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


#  model
def f(x, a, b, c):
    return (1/2)*x**2 + (4/110)*x + np.random.randn(100)


def optimization():
    plt.figure()
    # values not fitted
    x = np.linspace(0, 5, 100)
    y = (1/2)*x**2 + (4/110)*x + np.random.randn(100)
    plt.scatter(x, y)

    # fitted values
    params, params_cov = optimize.curve_fit(f, x, y)
    plt.plot(x, f(x, params[0], params[1], params[2]), c='red')

    plt.show()

optimization()

