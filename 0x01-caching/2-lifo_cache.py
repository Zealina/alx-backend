#!/usr/bin/env python3
"""Fifo caching module"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching Clasd"""
    def __init__(self):
        """initialize the class"""
        self.__ol = []
        super().__init__()

    def put(self, key, item):
        """Add item to the cache until max
        then discard in fifo"""
        if key is None or item is None:
            return
        if key in self.__ol:
            self.__ol.remove(key)
        self.__ol.append(key)
        if len(self.__ol) > BaseCaching.MAX_ITEMS:
            tbpop = self.__ol.pop(-2)
            del self.cache_data[tbpop]
            print(f"DISCARD: {tbpop}")
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve cached item"""
        if key is not None:
            return self.cache_data.get(key)
