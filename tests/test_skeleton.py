# -*- coding: utf-8 -*-

import pytest
from berlin_gelaendemodelle_downloader.skeleton import fib

__author__ = "Sebastian Jaeger"
__copyright__ = "Sebastian Jaeger"
__license__ = "apache"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
