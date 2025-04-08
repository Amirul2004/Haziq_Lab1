import functools
import os
import re
import struct
import threading
import warnings
from tempfile import NamedTemporaryFile

import numpy as np
from numpy import testing
from numpy.testing import (
    TestCase,
    assert_,
    assert_allclose,
    assert_almost_equal,
    assert_array_almost_equal,
    assert_array_almost_equal_nulp,
    assert_array_equal,
    assert_array_less,
    assert_equal,
    assert_no_warnings,
    assert_warns,
)
from numpy.typing import ArrayLike

from ..data._fetchers import _fetch
from ._warnings import expected_warnings

SKIP_RE = ...

skipif = ...
xfail = ...
parametrize = ...
raises = ...
fixture = ...

# true if python is running in 32bit mode
# Calculate the size of a void * pointer in bits
# https://docs.python.org/3/library/struct.html
arch32 = ...

_error_on_warnings = ...

def assert_less(a, b, msg=None): ...
def assert_greater(a, b, msg=None): ...
def doctest_skip_parser(func): ...
def roundtrip(image, plugin, suffix): ...
def color_check(plugin, fmt="png"): ...
def mono_check(plugin, fmt="png"): ...
def setup_test(): ...
def teardown_test(): ...
def fetch(data_filename): ...
def test_parallel(num_threads: int = 2, warnings_matching: ArrayLike | None = None): ...
