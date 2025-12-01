#!/usr/bin/env python3
"""
The function 'index_range' retrieves the indexes of
elements to display on a page, depending on page
number and page size elements. Both are passed as
arguments of type 'int'.

Example:
>>> res = index_range(page=2, page_size=15)
>>> print(res)
(15, 30)
"""


def index_range(page: int, page_size: int) -> tuple:
    """Defines indexes of elements to display on a page

    Args:
        page (int): page number
        page_size (int): number of elements in one page

    Return:
        res (tuple): start and end indexes of elements
                in a list, to display those within range
    """
    start: int = page_size * (page - 1)  # as p1 starts at idx 0, p2 at 15...
    end: int = page * page_size   # number of times we saw that amount of items
    res: tuple = (start, end)
    return res
