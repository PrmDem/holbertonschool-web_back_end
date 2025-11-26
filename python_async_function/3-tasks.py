#!/usr/bin/env python3
"""This module creates and returns an asyncio.Task
    using the 'wait_random' module"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates an asynchronous 'wait_random' task

    Args:
        max_delay (int): passed to wait_random, delay duration

    Return:
        (asyncio.Task) the created 'wait_random' task object
    """
    return asyncio.create_task(wait_random(max_delay))
