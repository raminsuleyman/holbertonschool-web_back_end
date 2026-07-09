#!/usr/bin/env python3
"""Module that contains a typed element_length function."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples (element, length of element)."""
    return [(i, len(i)) for i in lst]
