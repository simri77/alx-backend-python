#!/usr/bin/env python3
"""Async Comprehensions"""

from typing import List
import random
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
     return the 10 random numbers
    """
    retun[i async for i in async_generator()]
