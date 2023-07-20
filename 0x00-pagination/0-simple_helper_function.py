#!/usr/bin/env python3
""" Calculate the start and end indexes for a given page and page size."""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): _description_
        page_size (int): No of items per page

    Returns:
        tuple: _description_
    """
    start_index = (page - 1) * page_size
    end_index = page_size
    return (start_index, end_index)
