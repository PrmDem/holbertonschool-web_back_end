#!/usr/bin/env python3
"""Returns a tuple with the arguments as values

    Variables and expected return
    are validated via type annotation.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Args:
            k (str): a string, the first item in resulting tuple
            v (Union[int, float]): either a int or float, used to
                    calculate second item in resulting tuple

        Returns:
            (Tuple[str, float]) tuple containing both k and v squared
    """
    squ: float = v * v
    return (k, squ)
