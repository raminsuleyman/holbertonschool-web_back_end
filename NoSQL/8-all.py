#!/usr/bin/env python3
"""
List all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Return a list of all documents in a collection.
    If the collection is empty, return an empty list.
    """
    return list(mongo_collection.find())
