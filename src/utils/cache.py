# src/utils/cache.py
import os
from joblib import Memory
from functools import wraps
import logging

from src.utils.logger import setup_logging

DEV_MODE = os.environ.get("PYTHON_ENV") == "development"
memory = Memory(".cache", verbose=1) if DEV_MODE else None

setup_logging()


def dev_cache(func):
    """Cache function results during development"""
    if not DEV_MODE:
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key based on function name and args
        cache_func = memory.cache(func)
        return cache_func(*args, **kwargs)

    return wrapper
