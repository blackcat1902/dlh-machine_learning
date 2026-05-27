#!/usr/bin/env python3
""" insert a new document """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document and returns the _id """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id