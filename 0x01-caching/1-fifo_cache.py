#!/usr/bin/env python3
"""Fifo caching module"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching Clasd"""
    def __init__(self):
        """initialize the class"""
        self.__ol = []
        super().__init__()

    def put(self, key, item):
        """Add item to the cache until max
        then discard in fifo"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.__ol:
                self.__ol.append(key)
            if len(self.__ol) > BaseCaching.MAX_ITEMS:
                tbpop = self.__ol.pop(0)
                self.cache_data.pop(tbpop)
                print(f"Discard: {tbpop}")

    def get(self, key):
        """Retrieve cached item"""
        if key is not None:
            try:
                return self.cache_data[key]
            except KeyError:
                pass
        return None
