#!/usr/bin/env python3
"""
0-basic_cache.py
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    caching system
    """

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key

        Args:
            key (_type_): _description_
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
