#!/usr/bin/env python3
"""This module is an asynchronous coroutine
    that waits a random amount of time (up to 10sec)
    then returns that amount
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Args:
        max_delay (int): maximum delay before
            function executes/returns a value

        Return:
            float: wait time before return
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
