#!/usr/bin/env python3
"""Loops 10 times, waiting a second each time
    before yielding a random number between 0 and 10.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """No arguments.
    Returns a number (float) between 1 and 10
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
