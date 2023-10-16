from functools import partial
from jax import config as jax_config

jax_config.update("jax_enable_x64", True)  # double precision
jax_config.update("jax_platform_name", "cpu")  # use CPU
from jax import Array, lax, vmap
from jax import numpy as jnp


def savitzky_golay_derivative(ts: Array, x_ts: Array, **kwargs) -> Array:
    """
    Compute the numerical derivative using the Savitzky-Golay filter for all samples in x_ts.
    """
    time_indices = jnp.arange(x_ts.shape[0])
    x_d_ts = vmap(
        partial(
            savitzky_golay_derivative_single_sample,
            ts,
            x_ts,
            **kwargs
        )
    )(time_indices)

    return x_d_ts


def savitzky_golay_derivative_single_sample(ts: Array, x_ts: Array, sample_idx: int, num_left: int, num_right: int, order: int) -> Array:
    """
    Compute the numerical derivative by first finding the best (least-squares) polynomial of order m < 2k+1
    using the 2k+1 points in the neighborhood [t-left, t+right]. The derivative is computed  from the coefficients
    of the polynomial. The default edge behavior is to truncate the window at the offending edge. The data does
    not need to be sampled at equal timesteps.

    This function computes the derivative for a single sample_idx.

    A simple symmetric version of the Savitzky-Galoy filter is available as scipy.signal.savgol_filter.

    Args:
        ts (Array): Time vector of shape (n, )
        x_ts (Array): Signal vector of shape (n, )
        sample_idx (int): Index of the sample to compute the derivative for.
        num_left (int): number of samples to select to the left of the sample_idx
        num_right (int): number of samples to select to the right of the sample_idx
        order (int):  Order of polynomial. Expects 0 <= order < points in window.
        **kwargs: Optional keyword arguments.

    """
    """
    Attention: this is not jittable
    # create an index window from a dimensional window
    # Find the nearest point
    i_l = jnp.argmin(jnp.abs(ts - (ts[sample_idx] - toff_left)))
    i_r = jnp.argmin(jnp.abs(ts - (ts[sample_idx] + toff_right)))
    # Construct a polynomial in t using least squares regression.
    # Index views must allow for -left to +right, inclusively.
    ii = jnp.arange(i_l, i_r + 1)
    # Times are not periodic and initial values must be corrected.
    period = ts[-1] - ts[0]
    tfit = ts[ii % len(ts)] + period * (ii // len(ts))
    xfit = x_ts[ii % len(ts)]
    
    # return jnp.sum(jnp.array([j * w[j] * jnp.power(ts[sample_idx], j - 1) for j in range(1, order + 1)]))
    """
    # Construct a polynomial in t using least squares regression.
    # Index views must allow for -left to +right, inclusively.
    idx_left = jnp.clip(sample_idx - num_left, a_min=0, a_max=ts.shape[0]-num_left-num_right-1)
    tfit = lax.dynamic_slice(ts, (idx_left,), (num_left + num_right + 1,))
    xfit = lax.dynamic_slice(x_ts, (idx_left,), (num_left + num_right + 1,))

    w = jnp.polyfit(tfit, xfit, deg=order)

    # the coefficients are in the reverse (i.e. descending) order
    # https://stackoverflow.com/questions/59004096/numpy-polyfit-vs-numpy-polynomial-polynomial-polyfit/59004097#59004097
    w = w[::-1]

    # Compute the derivative from the polyfit coefficients.
    vec_j = jnp.arange(1, order + 1)
    power_j = jnp.power(ts[sample_idx], vec_j - 1)
    x_d = jnp.sum(vec_j * w[vec_j] * power_j)

    return x_d
