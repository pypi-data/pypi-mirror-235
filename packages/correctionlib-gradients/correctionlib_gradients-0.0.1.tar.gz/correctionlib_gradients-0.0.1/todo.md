## Major features
- [X] make CorrectionWithGrad play well with other JAX calculations: just work as a cog in the machine
	- [X] ...including usage of `jax.jit`
- [X] vectorized evaluation
- [ ] gradients through Binning
- [ ] gradients through Formula
	- [ ] in correctionlib, expose formula AST from C++ via PyBind11
- [ ] allow `jax.jit` usage when one of the inputs is a string: can probably tell jax to treat is as constant? 

## Optimizations
- [ ] if all bin contents are constant, evaluate the spline only once at the beginning
- [ ] ...otherwise compute spline over a _neighborhood_, not the whole histogram

## Packaging and DevOps
- [X] add CI workflow that runs ruff, mypy, black
- [X] add codecov integration