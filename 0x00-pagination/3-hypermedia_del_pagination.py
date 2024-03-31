#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Resilient Hypermedia Pagination
        Args:
            index(int) - The firat index of the current page
            page_size(int) - The number of dicts in page
        Return:
            The Page as requested
        """
        assert index < len(self.indexed_dataset())
        dataset = self.indexed_dataset()
        result = []
        key = 0
        pg = page_size
        while key < pg:
            try:
                value = dataset.get(index + key)
                if value:
                    result.append(value)
                else:
                    pg += 1
            except Exception:
                pass
            key += 1
        nxt_idx = index + pg
        return {
                'index': index,
                'next_index': nxt_idx if nxt_idx < len(dataset) else None,
                'page_size': len(result),
                'data': result
                }
