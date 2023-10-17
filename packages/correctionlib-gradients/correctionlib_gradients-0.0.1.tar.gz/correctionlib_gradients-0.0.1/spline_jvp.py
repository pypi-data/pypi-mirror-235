import jax
import numpy as np
from scipy.interpolate import CubicSpline


def midpoints(x):
    return 0.5*(x[1:] + x[:-1])

def make_differentiable_spline(x, y):
    spline = CubicSpline(midpoints(x), y, bc_type="clamped")
    dspline = spline.derivative(1)

    def clip(x):
        # so that extrapolation works
        return np.clip(x, spline.x[0], spline.x[-1])

    @jax.custom_jvp
    def eval_spline(x):
        return spline(clip(x))

    @eval_spline.defjvp
    def eval_spline_jvp(primals, tangents):
        x, = primals
        return eval_spline(x), dspline(clip(x)) * tangents

    return eval_spline

if __name__ == "__main__":
    x = np.array([0, 5., 10.])
    y = np.array([1., 2.])
    s = make_differentiable_spline(x, y)

    # JAX's tracing, necessary for the backward mode,
    # cannot trace through the spline's evaluation
    jax.grad(s)(1.)
