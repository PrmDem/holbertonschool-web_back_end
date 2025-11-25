#!/usr/bin/env python3
from typing import List, Union

"""Calculates the sum of float and int
    present in a list passed as argument

    Variables and expected return
    are validated via type annotation.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Args:
            mxd_lst (list of int and float): contains ints and floats
            to calculate the sum of

        Returns:
            (float) The sum of all ints and floats from the list
    """
    return sum(mxd_lst)
