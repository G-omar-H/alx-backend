#!/usr/bin/env python3
"""
2-lifo_cache.py
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching and is a caching system:

    must use self.cache_data - dictionary from the parent class BaseCaching

    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item
        value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded and
            following by a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.


    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """
        initializer
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item
        value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded and
            following by a new line

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if len(self.cache_data) ==\
                BaseCaching.MAX_ITEMS\
                and key not in self.cache_data.keys():
            data = list(self.cache_data.keys())[len(self.cache_data) - 1]
            print(f"DISCARD: {data}")
            del self.cache_data[list(self.cache_data.keys())
                                [len(self.cache_data) - 1]]
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.
            cache_data, return None.
        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
