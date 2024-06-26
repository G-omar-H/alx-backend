#!/usr/bin/env python3
"""
0-basic_cache.py
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system:

    Must use self.cache_data - dictionary from the parent class BaseCaching
    This caching system doesn't have limit
    def put(self, key, item):
        Must assign to the dictionary self.
            cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.
            cache_data, return None.


    Args:
        BasicCaching (Class): parent class
    """

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.
            cache_data, return None.

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
