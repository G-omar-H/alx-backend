#!/usr/bin/env python3
"""
3-lru_cache.py
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system:

    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self): but don't forget
        to call the parent init: super().__init__()
    def put(self, key, item):
        Must assign to the dictionary self.cache_data
            the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
            you must discard the least recently used item (LRU algorithm)
            you must print DISCARD: with the key discarded
                and following by a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in
        self.cache_data, return None.

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """
        initializer
        """
        self.lru = None
        self.cache_list = list()
        self.ageDict = dict()
        super().__init__()

    def set_age(self):
        """
        track the age of each cache
        """
        for key in self.cache_data.keys():
            if key not in self.ageDict.keys():
                self.ageDict[key] = 0

    def set_lru(self):
        """
        define the lest recentely used cache
        """
        a, b = next(iter(self.ageDict.items()))
        for key, value in self.ageDict.items():
            if b > value:
                a = key
                b = value
        self.lru = a

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
            is higher that BaseCaching.MAX_ITEMS:

        must discard the least recently used item (LRU algorithm)
        must print DISCARD: with the key discarded and following by a new
        """
        if key is None or item is None:
            return
        self.set_age()
        if len(
                self.cache_data) == self.MAX_ITEMS and key not in self.cache_data.keys():
            self.set_lru()
            print(f"DISCARD: {self.lru}")
            del self.cache_data[self.lru]
            del self.ageDict[self.lru]
        self.cache_data[key] = item
        self.ageDict[key] = 0
        print(f"                               {self.ageDict}")

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in
        self.cache_data, return None.

        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.ageDict[key]: self.ageDict[key] = + 1
        return self.cache_data[key]
