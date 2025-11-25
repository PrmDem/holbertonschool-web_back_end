#!/usr/bin/env python3
"""Calculates the sum of floats
    present in a list passed as argument

    Variables and expected return
    are validated via type annotation.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Args:
            input_list (List[float]): contains only floats to
                    calculate the sum of

        Returns:
            (float) The sum of all floats from the list
    """
    return sum(input_list)
