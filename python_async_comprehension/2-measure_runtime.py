#!/usr/bin/env python3
"""Module for measuring runtime."""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run four async comprehensions in parallel and measure runtime."""
    start = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for i in range(4)])

    end = time.perf_counter()
    return end - start
