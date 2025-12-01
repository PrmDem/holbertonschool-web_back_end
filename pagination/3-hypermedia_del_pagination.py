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
        """Gets content from csv file and various info

        Args:
            index (int, default None): index of the 1st item to display
            page_size (int, default 10): number of items per page, must be > 0

        Return:
            (Dict[str, object]): index (int), the 1st item on page;
            data (List[List]): retrieved items for the page length;
            page_size (int): number of items displayed on page;
            next_index (int): index of 1st item on the next page
        """
        dataset = self.indexed_dataset()
        data_length: int = len(dataset)
        assert index <= data_length
        next_index: int = index + page_size
        page_data: List[List] = []

        # In case of deletion
        if dataset.get(index) is None:
            # Increment to incorporate next page item(s)
            for i in range(index + 1, next_index + 1):
                page_data.append(dataset.get(i))
            next_index += 1
        else:
            # Proceed normally otherwise
            for i in range(index, next_index):
                page_data.append(dataset.get(i))

        resilient_data = {
            'index': index,
            'data': page_data,
            'page_size': len(page_data),
            'next_index': next_index
        }

        return resilient_data
