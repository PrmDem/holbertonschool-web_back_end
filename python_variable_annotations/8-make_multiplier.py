#!/usr/bin/env python3
from typing import Callable

"""Creates a Callable object that multiplies a number
    by the float 'multiplier' passed as argument to this module

    Variables and expected return
    are validated via type annotation.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Args:
           multiplier (float): number by which to multiply
                arguments used in the Callable function

        Returns:
            (Callable) A function that multiplies a number argument
                    by multiplier
    """
    def multi(multiplier: float) -> float:
        """Multiplies the float argument by itself

        Args:
            arg (float): number to multiply

        Returns:
            The result of the multiplication
        """
        return (multiplier * multiplier)
    return multi
