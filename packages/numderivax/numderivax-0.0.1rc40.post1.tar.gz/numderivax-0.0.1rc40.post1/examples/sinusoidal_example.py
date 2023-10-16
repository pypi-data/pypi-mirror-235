import derivative
from jax import config as jax_config

jax_config.update("jax_enable_x64", True)  # double precision
jax_config.update("jax_platform_name", "cpu")  # use CPU
from jax import Array, random
import jax.numpy as jnp
import matplotlib.pyplot as plt

rng = random.PRNGKey(0)


def main():
    duration = 10.0
    ts = jnp.linspace(0, duration, int(duration * 200))
    xs = jnp.sin(ts)
    # add white noise to the signal
    xs_noisy = xs + 0.01 * random.normal(rng, shape=xs.shape)

    fd = derivative.FiniteDifference(k=3)
    xs_fd = fd.d(xs_noisy, ts)

    sg = derivative.SavitzkyGolay(left=0.02, right=0.02, order=3)
    xs_sg = sg.d(xs_noisy, ts)

    fig, axes = plt.subplots(ncols=2, figsize=(10, 5))

    axes[0].set_title("signal")
    axes[0].plot(ts, xs_noisy, '.', label="noisy signal")
    axes[0].plot(ts, xs, label="ground-truth signal")
    axes[0].set_xlabel("time [s]")
    axes[0].set_ylabel("signal")
    axes[0].legend()
    axes[0].grid(True)

    axes[1].set_title("derivative")
    axes[1].plot(ts, xs_fd, label="derivative finite difference")
    axes[1].plot(ts, xs_sg, label="derivative Savitzky-Golay")
    axes[1].plot(ts, jnp.cos(ts), label="ground-truth derivative")
    axes[1].set_xlabel("time [s]")
    axes[1].set_ylabel("derivative")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
