# hicuda
Simplest possible pybind11 + CUDA + PyPI example:

```
pip install hicuda
```

```py
import hicuda
hicuda.cuda() # "Hello, CUDA!"
```

# WARNING
This only works with a version of Python that matches that of the built `.so` file.

After installing, use `pip show hicuda` and `cd` into the `Location` listed, then `cd hicuda`, `ls` will show you the `.so` file which has a prefix `hellobinding.cpython-3XX`. The `3XX` must match the Python you try to import the `hicuda` package from. On PyPI currently it's 3.11 as of version `0.0.2`.
