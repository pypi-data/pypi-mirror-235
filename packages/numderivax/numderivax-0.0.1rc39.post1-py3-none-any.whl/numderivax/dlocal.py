from jax import Array
from jax import numpy as jnp


def savitzky_golay(ts: Array, x_ts: Array, toff_left: float, toff_right: float, order: int) -> Array:
    """ Compute the numerical derivative by first finding the best (least-squares) polynomial of order m < 2k+1
    using the 2k+1 points in the neighborhood [t-left, t+right]. The derivative is computed  from the coefficients
    of the polynomial. The default edge behavior is to truncate the window at the offending edge. The data does
    not need to be sampled at equal timesteps.

    A simple symmetric version of the Savitzky-Galoy filter is available as scipy.signal.savgol_filter.

    Args:
        ts (Array): Time vector of shape (n, )
        x_ts (Array): Signal vector of shape (n, )
        toff_left (float): Left edge of the window is t-left [s]
        toff_right (float): Right edge of the window is t+right [s]
        order (int):  Order of polynomial. Expects 0 <= order < points in window.
        **kwargs: Optional keyword arguments.

    """
    # create an index window from a dimensional window
    # Find the nearest point
    ileft = jnp.argmin(jnp.abs(ts - (ts[i] - toff_left)))
    iright = jnp.argmin(jnp.abs(ts - (ts[i] + toff_right)))

    # i_l, i_r = _nondimensional_window(t, i)

    # Construct a polynomial in t using least squares regression.
    # Index views must allow for -left to +right, inclusively.
    ii = jnp.arange(i_l, i_r + 1)

    # Construct a polynomial in t using least squares regression.
    # Index views must allow for -left to +right, inclusively.
    ii = jnp.arange(i_l, i_r + 1)
    # Times are not periodic and initial values must be corrected.
    period = ts[-1] - ts[0]
    tfit = ts[ii % len(ts)] + period * (ii // len(ts))
    xfit = x_ts[ii % len(ts)]
    # Can raise RankWarning if order exceeds points in the window.
    w = jnp.polyfit(tfit, xfit, deg=order)

    # Compute the derivative from the polyfit coefficients.
    return jnp.sum([j * w[j] * jnp.power(ts[i], j - 1) for j in range(1, order + 1)])
