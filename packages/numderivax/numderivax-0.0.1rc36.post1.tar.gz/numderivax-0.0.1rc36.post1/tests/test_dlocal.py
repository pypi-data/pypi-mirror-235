import derivative
from jax import Array, jit, random, vmap
import jax.numpy as jnp

from numderivax.dlocal import savitzky_golay

rng = random.PRNGKey(0)


def test_savitzky_golay() -> None:
    toff_left = 1.0
    toff_right = 1.0
    order = 3

    ts = jnp.linspace(0, 10, 100)
    x_ts = jnp.sin(ts)
    # add white noise to the signal
    x_ts_noisy = x_ts + 0.1 * random.normal(rng, shape=x_ts.shape)

    # apply derivative.SavitzkyGolay
    sg = derivative.SavitzkyGolay(left=toff_left, right=toff_right, order=order)
    x_d_ts_target = sg.d(x_ts_noisy, ts)
    print(x_d_ts_target)


if __name__ == "__main__":
    test_savitzky_golay()
