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

    @jax.custom_vjp
    def eval_spline(x):
        return spline(clip(x))

    def eval_spline_fwd(x):
        return eval_spline(x), dspline(clip(x))

    def eval_spline_bwd(res, g):
        return (res * g),

    eval_spline.defvjp(eval_spline_fwd, eval_spline_bwd)

    return eval_spline

if __name__ == "__main__":
    x = np.array([0., 5., 10.])
    y = np.array([1., 2.])
    s = make_differentiable_spline(x, y)

    # this works
    print(jax.grad(s)(1.))
    print(np.vectorize(jax.grad(s))(np.linspace(0., 10.)))

    # jax.jit does not work: `s` is not traceable
    # jax.jit(jax.grad(s))(1.)

    # jax.vmap also doesn't work because `s` is not traceable
    # print(jax.vmap(jax.grad(s))(jax.numpy.array([1., 2.])))

