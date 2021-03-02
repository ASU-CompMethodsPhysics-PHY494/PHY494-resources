# sine series implementations

def sin_recursive(x, N=100):
    """Calculate sin(x) for N iterations.

    Arguments
    ---------
    x : float
        argument of sin(x)
    N : int
        number of iterations
    Returns
    -------
    func_value
    """
    # special case 0
    if x == 0:
        return 0.0, 1

    sumN = an = x  # n=1

    for n in range(2, N+1):
        qn = -x*x/((2*n - 1) * (2*n - 2))
        an *= qn
        sumN += an

    return sumN


import math

def sin_explicit(x, N=100):
    """Calculate sin(x) to precision eps... BADLY"""
    if x == 0:
        return 0., 1
    an = x
    sumN = 0.
    for n in range(1, N+1):
        an = (-1)**(n-1) * x**(2*n-1) / math.factorial(2*n-1)
        sumN += an

    return sumN
