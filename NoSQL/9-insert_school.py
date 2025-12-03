#!/usr/bin/env python3
"""Using kwargs, inserts new document
    in the collection 'school'
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a kwarg as new document

    Args:
        mongo_collection (collection object):
            mongoDB collection to insert into
        kwargs (str): typically a school name,
            with an optional address

    Return:
        (str) the id of the new document"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
