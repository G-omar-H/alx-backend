#!/usr/bin/env python3
"""
4-mru_cache.py
"""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Initialize MRUCache
        """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.mru_keys.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.mru_keys.pop(-2)
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

    def get(self, key):
        """
        Get an item from cache by key
        """
        if key and key in self.cache_data:
            self.mru_keys.remove(key)
            self.mru_keys.append(key)
            return self.cache_data[key]
        return None
