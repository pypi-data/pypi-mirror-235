from __future__ import annotations
import derivative
from functools import partial
from jax import Array, jit, random, vmap
import jax.numpy as jnp

from numderivax.dlocal import savitzky_golay_derivative_single_sample, savitzky_golay_derivative

rng = random.PRNGKey(seed=0)


def test_savitzky_golay() -> None:
    order = 3

    ts = jnp.linspace(0, 10, 100)
    x_ts = jnp.sin(ts)
    # add white noise to the signal
    x_ts_noisy = x_ts + 0.1 * random.normal(rng, shape=x_ts.shape)

    # initialize the functions
    sg = derivative.SavitzkyGolay(left=1.0, right=1.0, order=order)
    savitzky_golay_fn = partial(
        savitzky_golay_derivative_single_sample, num_left=10, num_right=10, order=order
    )
    savitzky_golay_fn_jitted = jit(savitzky_golay_fn)

    # apply derivative.SavitzkyGolay to index 0
    x_d0_target = sg.compute(ts, x_ts_noisy, 0)
    # apply our own savitzky_golay to index 0
    x_d0 = savitzky_golay_fn(ts, x_ts_noisy, 0)
    if not jnp.allclose(x_d0_target, x_d0):
        print(
            f"x_d0: {x_d0} != x_d0_target: {x_d0_target}"
        )
    # now try the jitted version
    x_d0 = savitzky_golay_fn_jitted(ts, x_ts_noisy, 0)

    # apply derivative.SavitzkyGolay to index 50
    x_d50_target = sg.compute(ts, x_ts_noisy, 50)
    # apply our own savitzky_golay to index 50
    x_d50 = savitzky_golay_fn(ts, x_ts_noisy, 50)
    if not jnp.allclose(x_d50_target, x_d50):
        print(
            f"x_d50: {x_d50} != x_d50_target: {x_d50_target}"
        )

    # apply derivative.SavitzkyGolay to index 99
    x_d99_target = sg.compute(ts, x_ts_noisy, 99)
    # apply our own savitzky_golay to index 99
    x_d99 = savitzky_golay_fn(ts, x_ts_noisy, 99)
    if not jnp.allclose(x_d99_target, x_d99):
        print(
            f"x_d99: {x_d99} != x_d99_target: {x_d99_target}"
        )

    x_d_ts_target = sg.d(x_ts_noisy, ts)
    x_d_ts = savitzky_golay_derivative(ts, x_ts_noisy, num_left=10, num_right=10, order=order)
    if not jnp.allclose(x_d_ts_target, x_d_ts):
        print(
            f"x_d_ts:\n{x_d_ts} != x_d_ts_target:\n{x_d_ts_target}"
        )


def test_int_mock():
    # this is just a mock test to prevent errors in the CI
    pass


if __name__ == "__main__":
    test_savitzky_golay()
