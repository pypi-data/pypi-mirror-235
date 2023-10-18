# contextcache

[![CI](https://github.com/Peter554/contextcache/actions/workflows/ci.yml/badge.svg)](https://github.com/Peter554/contextcache/actions/workflows/ci.yml)

Cache a python function only in certain contexts.

## Usage

Here's an example:

```py
# example.py
import contextvars

import contextcache

# Define a private ContextVar to store the cached values. Don't touch this ContextVar!
_double_cache = contextvars.ContextVar("double_cache", default=None)


# Use the `enable_caching` decorator to enable context caching for `double`.
@contextcache.enable_caching(_double_cache)
def double(n: int) -> int:
    print(f"doubling {n}")
    return n * 2


# Without caching.
double(1)
double(1)

# With caching.
with contextcache.use_caching(double):
    double(2)
    double(2)

```

Here's the output:

```sh
python example.py
```

```
doubling 1
doubling 1
doubling 2

```
