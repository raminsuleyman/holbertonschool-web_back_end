#!/usr/bin/env python3
"""
Insert a new document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The document fields.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
