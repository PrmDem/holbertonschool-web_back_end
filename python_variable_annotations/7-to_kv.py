#!/usr/bin/env python3
from typing import Union, Tuple

"""Returns a tuple with the arguments as values

    Variables and expected return
    are validated via type annotation.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Args:
            k (str): a string, the first item in resulting tuple
            v (int or float): either a int or float, used to
                    calculate second item in resulting tuple

        Returns:
            (float) The sum of all ints and floats from the list
    """
    squ: float = v * v
    return (k, squ)
