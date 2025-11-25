#!/usr/bin/env python3
"""Calculates and returns the floor of a float

    Variables and expected return
    are validated via type annotation.
"""


def floor(n: float) -> int:
    """Args:
            n (float): argument to find floor of

        Returns:
            (int) The floor of float 'n'
    """
    return int(n // 1)
