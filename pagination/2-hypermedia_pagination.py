#!/usr/bin/env python3
"""
This module uses pagination to retrieve information
from a .csv file.
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Defines indexes of elements to display on a page

    Args:
        page (int): page number
        page_size (int): number of elements in one page

    Return:
        res (tuple): start and end indexes of elements
                in a list, to display those within range
    """
    start: int = page_size * (page - 1)  # as p1 starts at idx 0, p2 at 15...
    end: int = page * page_size   # number of times we saw that amount of items
    return (start, end)


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
        """Gets contents from csv file

        Args:
            page (int, default 1): page number, must be > 0
            page_size (int, default 10): number of items per page, must be > 0

        Return:
            (List[List]) a list of rows within range of the request
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_file = self.dataset()
        data_length = len(data_file)
        # Get the total number of pages needed by the file
        pages_total = math.ceil(data_length / page_size)

        # Returns empty list if page out of bounds
        if page > pages_total:
            return []

        # Get indexes from index_range
        start, end = index_range(page, page_size)
        # Slices dataset as requested
        return data_file[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Gets content from csv file and various info

        Args:
            page (int, default 1): page number, must be > 0
            page_size (int, default 10): number of items per page, must be > 0

        Return:
            (Dict[str, object]): values for page_size (int), page (int),
            data (List[List]), next_page (int), prev_page (int),
            and total_pages (int)
        """
        data_file: List[List] = self.dataset()
        data_length: int = len(data_file)
        pages_total: int = math.ceil(data_length / page_size)
        page_data = self.get_page(page, page_size)

        # Gets int or None if out of range
        if (page + 1) <= pages_total:
            next = page + 1
        else:
            next = None

        # Gets int or None if out of range
        if (page - 1) != 0:
            prev = page - 1
        else:
            prev = None

        hyper_data = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next,
            'prev_page': prev,
            'total_pages': pages_total
        }

        return hyper_data
