#!/usr/bin/env python3
"""This module uses previous 'wait_n' module
in a new function, to measure total exec time
for wait_n. It then returns that total divided by n.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures runtime for wait_n

    Args:
        n (int): # of times to run the function
        max_delay (int): maximum delay before returning value

    Return:
        (float) time elapsed while wait_n was running
    """
    launch = time.time()
    asyncio.create_task(wait_n(n, max_delay))
    total_time = time.time() - launch
    return (total_time / n)
