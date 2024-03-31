#!/usr/bin/env python3
"""Index Range Module"""

from typing import Tuple, List
import csv
import math


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple Pagination
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        rnge = index_range(page, page_size)
        result = []
        dataset = self.dataset()
        try:
            for i in range(rnge[0], rnge[1]):
                result.append(dataset[i])
                return result
        except Exception:
            pass
        return []
