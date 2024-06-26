#!/usr/bin/env python3
"""
1-fifo_cache.py
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system:

    You must use self.cache_data - dictionary from the parent class BaseCaching
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item value fo
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than BaseCachin
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and following
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
