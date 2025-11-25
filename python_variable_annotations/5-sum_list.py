#!/usr/bin/env python3
from typing import List

"""Calculates the sum of floats
    present in a list passed as argument

    Variables and expected return
    are validated via type annotation.
"""


def sum_list(input_list: List[float]) -> float:
    """Args:
            input_list (list of floats): contains only floats to
                    calculate the sum of

        Returns:
            (float) The sum of all floats from the list
    """
    return sum(input_list)
