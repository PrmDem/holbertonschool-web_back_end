#!/usr/bin/env python3
"""Creates a Callable object that multiplies a number
    by the float 'multiplier' passed as argument to this module

    Variables and expected return
    are validated via type annotation.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Args:
           multiplier (float): number by which to multiply
                arguments used in the Callable function

        Returns:
            Callable[[float], float] A function that multiplies
                a number argument by multiplier
    """
    def multi(val: float) -> float:
        """Multiplies the float argument by itself

        Args:
            val (float): number to multiply

        Returns:
            The result of the multiplication (float)
        """
        return (val * multiplier)
    return multi
