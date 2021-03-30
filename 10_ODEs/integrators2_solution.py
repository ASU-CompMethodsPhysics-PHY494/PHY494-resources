# integrators for lesson 10 ODEs
# Copyright (c) 2016-2021 Oliver Beckstein.
# License: BSD-3 clause

# Integrating Newton's Equations of Motions in 2D... nD
# (very similar to integrators.py but includes a few more numpy
# tricks to make higher dimensional positions/velocities work)

import numpy as np
import numpy.linalg

import matplotlib.pyplot as plt

#------------------------------------------------------------
# force and potential energy functions
#
# All force functions need to accept as argument the position x
# and return the force.
#
# Each function always takes the position x (n-d array)
# and any additional parameters needed to specify the force law.
# The **kwargs parameter swallows any other un-used keyword
# arguments and allows us to use the same framework with different
# force laws.
#
# The functions can take lists/arrays of n-dimensional vectors
# and will produce equivalent arrays of force vectors or
# n-dim arrays containing energies


# central forces

def unitvector(r):
    """Return |r|, r/|r|.

    Parameters
    ----------
    r : array
      Can be a single position vector (d-dim, i.e. d cartesian coordinates) or
      N x d, i.e. N positions in d-dim space.

    Returns
    -------
    rr : array
       lengths of all the vectors as a Nx1 array
    rhat : array
       unit vectors in a Nxd array
    """
    rr = numpy.linalg.norm(r, axis=-1, keepdims=True)
    rhat = r/rr
    return rr, rhat


# constant of gravity when usinh AU for length, solar mass for
# mass, and years for time
G_gravity = 4*np.pi**2
M_sun = 1.0
M_earth = 3.003467e-6

def F_gravity(r, m=M_earth, M=M_sun, **kwargs):
    rr, rhat = unitvector(r)
    return -G_gravity*m*M/rr**2 * rhat

def U_gravity(r, m=M_earth, M=M_sun, **kwargs):
    rr, rhat = unitvector(r)
    return np.ravel( -G_gravity*m*M/rr )

def F_harmonic(r, k=1, **kwargs):
    """Harmonic force"""
    return -k*r

def U_harmonic(r, k=1, **kwargs):
    """Harmonic potential  U(x) = 1/2 k x**2"""
    rr, rhat = unitvector(r)
    return np.ravel( 0.5*k*rr**2 )

def F_power(r, k=1, p=6, **kwargs):
    """Force for k/p x^p potential."""
    rr, rhat = unitvector(r)
    return -k * rr**(p-1) * rhat

def U_power(r, k=1, p=6, **kwargs):
    """Even-power potential U(x) = k/p x**p"""
    rr, rhat = unitvector(r)
    return np.ravel( k/p * r**p )

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
    k1 = f(t, y)
    k2 = f(t + 0.5*h, y + 0.5*h*k1)
    return y + h*k2

def rk4(y, f, t, h):
    """Runge-Kutta RK4"""
    k1 = f(t, y)
    k2 = f(t + 0.5*h, y + 0.5*h*k1)
    k3 = f(t + 0.5*h, y + 0.5*h*k2)
    k4 = f(t + h, y + h*k3)
    return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

def velocity_verlet(y, f, t, h):
    """Velocity Verlet

    Low-performance implementation because the force is calculated
    twice; should remember the second force calculation and use as
    input for the next step.

    For comparing different algorithms it is ok to use this
    implementation for convenience. For production level code you
    should use a better implementation that saves the second force
    evaluation.

    """
    # half step velocity
    F = f(t, y)
    y[1] += 0.5*h * F[1]
    # full step position
    y[0] += h*y[1]
    # full step velocity (updated positions!)
    # NOTE: this force evaluation should be used for the next iteration!!!
    F = f(t+h, y)
    y[1] += 0.5*h * F[1]

    return y

#------------------------------------------------------------
# analysis

def kinetic_energy(v, m=1):
    """Kinetic energy 1/2 m v**2"""
    # v = [[v(0)x, v(0)y], [...], ...]
    return 0.5*m*np.sum(v**2, axis=-1)

def energy_conservation(t, y, U, **kwargs):
    """Energy drift (Tuckerman Eq 3.14.1)"""
    m = kwargs.get('m', 1)
    x, v = y[:, 0], y[:, 1]
    KE = kinetic_energy(v, m=m)
    PE = U(x, **kwargs)
    E = KE + PE

    machine_precision = 1e-15
    if np.isclose(E[0], 0, atol=machine_precision, rtol=machine_precision):
        # if E[0] == 0 then replace with machine precision (and expect bad results)
        E[0] = machine_precision
    return np.mean(np.abs(E/E[0] - 1))

def energy_precision(energy, machine_precision=1e-15):
    """log10 of relative energy conservation"""
    if np.isclose(energy[0], 0, atol=machine_precision, rtol=machine_precision):
        # if E[0] == 0 then replace with machine precision (and expect bad results)
        E = energy.copy()
        E[0] = machine_precision
    else:
        # don't modify input energies
        E = energy
    DeltaE = np.abs(E/E[0] - 1)
    # filter any zeros
    # (avoid log of zero by replacing 0 with machine precision 1e-15)
    zeros = np.isclose(DeltaE, 0, atol=machine_precision, rtol=machine_precision)
    DeltaE[zeros] = machine_precision
    return np.log10(DeltaE)

def analyze_energies(t, y, U, step=1, **kwargs):
    m = kwargs.get('m', 1)
    x, v = y[:, 0], y[:, 1]
    KE = kinetic_energy(v, m=m)
    PE = U(x, **kwargs)
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
    ax.set_ylabel("log(relative error energy)")

    #return ax.figure


#------------------------------------------------------------
# ODE integration


def integrate_newton_2d(x0=np.array([0, 0]), v0=np.array([0, 1]), t_max=100, h=0.001, mass=1,
                        force=F_harmonic, integrator=euler,
                        **kwargs):
    """Integrate Newton's equations of motions in 2D.

    Note that all problem parameters must be set consistently in the
    force function.

    The force function and the integrator must be able to work with
    n-dimensional position and velocity vectors.

    Arguments
    ---------
    x0 : array
       initial position
    v0 : array
       initial velocity
    t_max : float
       time to integrate out to
    h : float (default 0.001)
       integration time step
    mass : float (default 1)
       mass of the particle
    force : function `f(x, **kwargs)`
       function that returns the force when particle is
       at position `x`; kwargs can be used to customize, e.g.,
       `k=1` for F_harmonic or `k=1, p=6` for F_power.
    integrator : function `I(y, f, t, h)`
       function that takes the ODE standard form vectors y and f
       together with the current time and the step `h` and returns
       y at time t+h.
    **kwargs : keyword arguments
       Other kwargs that are passed to the `force()` function (`mass`
       is added to the kwargs).

    Returns
    -------
    Tuple ``(t, y)`` with times and the ODE standard form vector.
    `y[:, 0]` is position and `y[:, 1]` velocity. Note that position
    and velocity are 2- or 3D arrays.

    """
    # code can be easily generalized to 3D
    dim = len(x0)
    assert len(v0) == dim

    Nsteps = int(t_max/h)
    t_range = h * np.arange(Nsteps)
    y_values = np.zeros((len(t_range), 2, dim))

    # initial conditions
    y_values[0, 0, :] = x0
    y_values[0, 1, :] = v0

    # build a gradient function with "our" force
    def f(t, y):
        """ODE force vector (currently only for velocity-independent forces)"""
        return np.array([y[1], force(y[0], **kwargs)/mass])


    for i, t in enumerate(t_range[:-1]):
        y_values[i+1, :] = integrator(y_values[i].copy(), f, t, h)

    return t_range, y_values
