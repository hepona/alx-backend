#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page, page_size) -> tuple:
    """return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters."""
    start = page_size * (page - 1)
    end = start + page_size
    tup = (start, end)
    return tup
