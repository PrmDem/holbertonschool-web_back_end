#!/usr/bin/env python3
"""Searches and filters schools by topic taught"""


def schools_by_topic(mongo_collection, topic):
    """Lists schools teaching a specific topic

    Args:
        mongo_collection (collection object):
            mongoDB collection of documents to look into

        topic (str): school subject, search parameter

    Return:
        (list) Schools where the topic is taught
        """
    return mongo_collection.find({"topics": topic})
