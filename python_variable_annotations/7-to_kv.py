#!/usr/bin/env python3
"""Module that contains a typed to_kv function."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple (k, v squared as float)."""
    return (k, float(v ** 2))
