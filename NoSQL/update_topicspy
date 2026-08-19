#!/usr/bin/env python3
"""
Update topics of a school document.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all school documents matching the given name.

    Args:
        mongo_collection: The pymongo collection object.
        name: The school name.
        topics: List of topics.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
