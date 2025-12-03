#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """Arg:
        mongo_collection (collection obj):
            collection from which to get documents

        Return:
            (list) documents as a list
    """
    return list(mongo_collection.find())
