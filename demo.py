''' A simple demonstration of using nordplotlib to generate a fun
Brownian motion plot. Code for the Brownian motion calculation is not
mine but appears in the SciPy Cookbook.
'''

import argparse
import importlib
import numpy as np
import matplotlib.pyplot as plt

from math import sqrt
from scipy.stats import norm

np.random.seed(314159)

def brownian(x0, n, dt, delta, out=None):
    '''
    Source: https://scipy-cookbook.readthedocs.io/items/BrownianMotion.html

    Generate an instance of Brownian motion (i.e. the Wiener process):

        X(t) = X(0) + N(0, delta**2 * t; 0, t)

    where N(a,b; t0, t1) is a normally distributed random variable with mean a and
    variance b.  The parameters t0 and t1 make explicit the statistical
    independence of N on different time intervals; that is, if [t0, t1) and
    [t2, t3) are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
    are independent.

    Written as an iteration scheme,

        X(t + dt) = X(t) + N(0, delta**2 * dt; t, t+dt)


    If `x0` is an array (or array-like), each value in `x0` is treated as
    an initial condition, and the value returned is a numpy array with one
    more dimension than `x0`.

    :param x0: Initial positions for the Brownian motion
    :type x0: float or np.ndarray
    :param n: Number of steps
    :type n: int
    :param dt: Constant timestep
    :type dt: float
    :param delta: Determines the "speed" of the Brownian motion. The random
        variable of the position at time t, X(t), has a normal distribution
        whose mean is the position at time t=0 and whose variance is delta**2*t.
    :type delta: float
    :param out: If `out` is not None, it specifies the array in which to
        put the result.  If `out` is None, a new :class:`numpy.ndarray`
        is created and returned.
    :type out: :class:`numpy.ndarray` or None
    :return: Brownian motion paths
    :rtype: :class:`numpy.ndarray` with shape :code:`x0.shape + (n,)`
    '''
    x0 = np.asarray(x0)

    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r = norm.rvs(size=x0.shape + (n,), scale=delta*sqrt(dt))

    # If `out` was not given, create an output array.
    if out is None:
        out = np.empty(r.shape)

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples.
    np.cumsum(r, axis=-1, out=out)

    # Add the initial condition.
    out += np.expand_dims(x0, axis=-1)

    return out

delta = 2   # The Wiener process parameter.
T = 10.0    # Total time.
N = 500     # Number of steps.
dt = T / N  # Time step size
m = 20      # Number of realizations to generate.

# Create an empty array to store the realizations.
x = np.empty((m, N+1))
# Initial values of x.
x[:,0] = 50

brownian(x[:,0], N, dt, delta, out=x[:,1:])

parser = argparse.ArgumentParser(prog='python demo.py')
parser.add_argument('variant', type=str, choices=['png', 'pdf'])
parser.add_argument('--save', type=str, default=None)
args = parser.parse_args()

module = importlib.import_module('.'.join(['nordplotlib', args.variant]))
module.install()

t = dt * np.arange(N + 1)
for k in range(m): plt.plot(t, x[k])

plt.xlabel(r'$t$', fontsize=16)
plt.ylabel(r'$x$', fontsize=16)
plt.title(r'Brownian motion $X(t + \Delta t) = X(t) + ' \
    r'\mathcal{N}(0, \delta^2 \Delta t)$')
plt.grid(True)

if args.save: plt.savefig(args.save)
else: plt.show()

# vim: set ft=python:
