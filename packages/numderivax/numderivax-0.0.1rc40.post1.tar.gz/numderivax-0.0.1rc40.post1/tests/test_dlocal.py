from __future__ import annotations
import derivative
from jax import Array, jit, random, vmap
import jax.numpy as jnp

from numderivax.dlocal import savitzky_golay

rng = random.PRNGKey(seed=0)


def test_savitzky_golay() -> None:
    toff_left = 1.0
    toff_right = 1.0
    order = 3

    ts = jnp.linspace(0, 10, 100)
    x_ts = jnp.sin(ts)
    # add white noise to the signal
    x_ts_noisy = x_ts + 0.1 * random.normal(rng, shape=x_ts.shape)

    # initialize the derivative.SavitzkyGolay
    sg = derivative.SavitzkyGolay(left=toff_left, right=toff_right, order=order)

    # apply derivative.SavitzkyGolay to index 0
    x_d0_target = sg.compute(ts, x_ts_noisy, 0)
    # apply our own savitzky_golay to index 0
    x_d0 = savitzky_golay(0, ts, x_ts_noisy, toff_left, toff_right, order)
    assert jnp.allclose(x_d0_target, x_d0), "x_d_ts_target[0] != x_d0"

    # x_d_ts_target = sg.d(x_ts_noisy, ts)


def test_int_mock():
    # this is just a mock test to prevent errors in the CI
    pass


if __name__ == "__main__":
    test_savitzky_golay()
