#!/usr/bin/env python3
"""Pagination function"""


def index_range(page, page_size):
    """Return the start and end indices for a page"""
    if not page or not page_size:
        return (0, 0)
    return (((page - 1) * page_size), (page * page_size))
