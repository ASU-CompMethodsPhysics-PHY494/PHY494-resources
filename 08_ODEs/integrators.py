# integrators for lesson 08 ODEs --- student version
# Copyright (c) 2016 Oliver Beckstein.
# License: BSD-3 clause

#============================================================
# NOTE: Code is incomplete. You need to make it work
#       (see comment IMPLEMENT and replace None with
#       appropriate code)
#============================================================

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------
# forces
#
# All functions need to accept as argument the position x
# and return the force.
# Additional parameters should be added as optional keyword
# arguments.

def F_harmonic(x, k=1):
    """Harmonic force"""
    return -k*x

def U_harmonic(x, k=1):
    """Harmonic potential  U(x) = 1/2 k x**2"""
    return 0.5*k*x**2

def F_anharmonic(x, k=1, alpha=0.5):
    """Anharmonic force"""
    # IMPLEMENT

def U_anharmonic(x, k=1, alpha=0.5):
    """Anharmonic potential U(x) = 1/2 k x**2 (1 - 2/3 alpha x)"""
    return 0.5*k*x**2 * (1 - 2/3*alpha*x)

def F_power(x, k=1, p=6):
    """Force for k/p x^p potential."""
    # IMPLEMENT

def U_power(x, k=1, p=6):
    """Even-power potential U(x) = k/p x**p"""
    return k/p * x**p

#------------------------------------------------------------
# integrators
#
# The integrator takes as arguments y, f, h and returns
# y at time t+h. f is a function f(t, y) that must return
# the ODE force vector.

def euler(y, f, t, h):
    """Euler integrator.

    Returns new y at t+h.
    """
    return y + h * f(t, y)

def rk2(y, f, t, h):
    """Runge-Kutta RK2 midpoint"""
    # IMPLEMENT

def rk4(y, f, t, h):
    """Runge-Kutta RK4"""
    # IMPLEMENT

#------------------------------------------------------------
# analysis

def kinetic_energy(v, m=1):
    # IMPLEMENT
    return None

def energy_precision(energy):
    return np.log10(np.abs(energy[0]/energy - 1))

def analyze_energies(t, y, U, m=1, step=1):
    x, v = y.T
    KE = kinetic_energy(v, m=m)
    PE = U(x)
    energy = KE + PE

    times = t[::step]

    ax = plt.subplot(2, 1, 1)
    ax.plot(times, KE[::step], 'r-', label="KE")
    ax.plot(times, PE[::step], 'b-', label="PE")
    ax.plot(times, energy[::step], 'k--', label="E")
    #ax.set_xlabel("time")
    ax.set_ylabel("energy")
    ax.legend(loc="best")

    e_prec = energy_precision(energy)
    ax = plt.subplot(2, 1, 2)
    ax.plot(times, e_prec[::step])
    ax.set_xlabel("time")
    ax.set_ylabel("relative error energy")

    #return ax.figure

#------------------------------------------------------------
# ODE integration

def f_standard(t, y, force, m=1):
    """Force vector in standard ODE form (n=2)

    Arguments
    ---------
    t : float
        time
    y : array
        dependent variables in ODE standard form (2d)
    force : function
        `force(y[0])` returns force (note: will not be
        able to handle velocity dependent forces)
    m : float
        mass
    """
    return np.array([y[1], force(y[0])/m])


def integrate_newton(x0=0, v0=1, t_max=100, h=0.001, mass=1,
                     force=F_harmonic, integrator=euler):
    """Integrate Newton's equations of motions.

    Note that all problem parameters such as spring constant k must be
    set consistently in the force function.

    Arguments
    ---------
    x0 : float
       initial position
    v0 : float
       initial velocity
    t_max : float
       time to integrate out to
    h : float (default 0.001)
       integration time step
    mass : float (default 1)
       mass of the particle
    force : function `f(x)`
       function that returns the force when particle is
       at position `x`
    integrator : function `I(y, f, t, h)`
       function that takes the ODE standard form vectors y and f
       together with the current time and the step `h` and returns
       y at time t+h.

    Returns
    -------
    Tuple ``(t, y)`` with times and the ODE standard form vector.
    `y[:, 0]` is position and `y[:, 1]` velocity.

    """

    Nsteps = t_max/h
    t_range = h * np.arange(Nsteps)
    y = np.zeros((len(t_range), 2))

    # initial conditions
    y[0, :] = x0, v0

    # build a function with "our" force
    def f(t, y):
        """ODE force vector"""
        return f_standard(t, y, force, m=mass)

    for i, t in enumerate(t_range[:-1]):
        y[i+1, :] = integrator(y[i], f, t, h)

    return t_range, y
