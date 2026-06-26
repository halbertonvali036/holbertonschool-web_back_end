#!/usr/bin/env python3
"""Module that contains the make_multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""

    def multiplier_func(value: float) -> float:
        """Multiply value by multiplier."""
        return value * multiplier

    return multiplier_func
