#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
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
