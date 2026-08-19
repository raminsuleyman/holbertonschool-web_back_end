#!/usr/bin/env python3
"""
Return schools by topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: Topic to search for.

    Returns:
        A list of matching documents.
    """
    return mongo_collection.find({"topics": topic})
