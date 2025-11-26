#!/usr/bin/env python3
"""Using the imported async_generator function,
    this module collects the ten yielded floats
    in a list.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """No arguments.

    Return:
        (List[float]) the floats yielded by async_generator
    """
    return [fl async for fl in async_generator()]
