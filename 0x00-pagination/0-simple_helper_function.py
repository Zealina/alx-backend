#!/usr/bin/env python3
"""Index Range Module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return the index tange
    Args:
        page(int): The page number
        page_size(int): Thevsize of thebpage
    Return:
        Tuple containing the index range
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
