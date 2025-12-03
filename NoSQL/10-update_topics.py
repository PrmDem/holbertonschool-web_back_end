#!/usr/bin/env python3
"""Based on the name of a school document,
    adds topics that can be studied there."""


def update_topics(mongo_collection, name, topics):
    """Adds topics to school documents

    Args:
        mongo_collection (collection object):
            mongoDB collection of documents to update
        name (str): name of a school
        topics (list[str]): list of topics studied

    Return:
        updated collection object
    """
    query_filter = {'name': name}
    update_operation = {'$set': {'topics': topics}}
    return mongo_collection.update_many(query_filter, update_operation)
