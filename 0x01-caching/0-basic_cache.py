#!/usr/bin/env python3
"""Caching in python"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """My Caching System"""
    def put(self, key, item):
        """Add item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve cached item"""
        if key is not None:
            try:
                return self.cache_data[key]
            except KeyError:
                pass
        return None
