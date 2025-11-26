#!/user/bin/env python3
"""This module uses the 'wait_random' module to create
an async routine that spawns 'wait_random' a certain
amount of time within a specified 'max_delay'.

The module returns the list of delays as floats,
in ascending order.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """invokes wait_random and spawns it n times

    Args:
        n (int): how many times wait_random should be spawned
        max_delay (int): passed to wait_random, delay duration

    Return:
        List[float]: delays in ascending order
    """
    coro = [asyncio.create_task(wait_random(max_delay)) for idx in range(n)]
    listDelays: List[float] = [
        await coro for coro in asyncio.as_completed(coro)
        ]

    return listDelays
