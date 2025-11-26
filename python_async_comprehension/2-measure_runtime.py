#!/usr/bin/env python3
"""Measures the total runtime of 'async_comprehension'
    when it is executed in parallel 4 times.

    Runtime will be around 10 seconds, as coroutines
    are executed at the same time (in parallel),
    made to wait a second before yielding a number,
    and yield ten numbers total.
    Variations include runtime for main() and measure_runtime itself
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures and runtime for
        4 parallel executions of async_comprehension.

        Return:
            (float) total runtime
    """
    idx: int = 0
    launch = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - launch
