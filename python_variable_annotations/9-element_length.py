#!/usr/bin/env python3
from typing import List, Iterable, Sequence, Tuple

"""Annotation of parameters according to expected return:

    {'lst': typing.Iterable[typing.Sequence],
      'return': typing.List[typing.Tuple[typing.Sequence, int]]}
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Iterates through a sequence and finds length
        of each item

        Args:
            lst (iterable): typed as Sequence to support 'len';
            used to retrieve return values

        Return:
            A list of tuples, where each tuple contains
                an item of the sequence and the item's length
    """
    return [(i, len(i)) for i in lst]
