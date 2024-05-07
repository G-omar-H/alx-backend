#!/usr/bin/env python3
"""
2-hypermedia_pagination.py
"""


import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    unction should return a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in a list for
    those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        page = dataset[start:end]
        return page if page else []

    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
        returns a dictionary containing the following key-value pairs:
            page_size : the length of the returned dataset page
            page : the current page number
            data : the dataset page (equivalent to return from previous task)
            next_page : number of the next page, None if no next page
            prev_page : number of the previous page, None if no previous page
            total_pages : the total number of pages in the dataset as an int

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict: _description_
        """
        data = self.get_page(page, page_size)
        total_pages = round(len(self.__dataset) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": None if page > total_pages else page + 1,
            "prev_page": None if page > 1 else page - 1,
            "total_pages": total_pages,
        }
