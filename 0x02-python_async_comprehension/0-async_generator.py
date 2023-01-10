#!/usr/bin/env python3
"""Async Generator """
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """asynchronously wait 1 second
    yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
