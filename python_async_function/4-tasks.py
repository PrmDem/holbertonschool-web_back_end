#!/usr/bin/env python3
"""Upgrades code from 'wait_n' to incorporate 'task_wait_random'.

    This new module still returns a list of the delays
    from 'wait_random', but uses a second module to create tasks.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """invokes wait_random from within task_wait_random
    spawning it 'n' amount of times

    Args:
        n (int): how many times wait_random should be spawned
        max_delay (int): passed to wait_random, delay duration

    Return:
        List[float]: delays in ascending order
    """
    coro = [(task_wait_random(max_delay)) for idx in range(n)]
    listDelays = [await coro for coro in asyncio.as_completed(coro)]

    return listDelays
