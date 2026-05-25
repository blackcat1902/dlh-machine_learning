#!/usr/bin/env python3
""" list all documents """


def list_all(mongo_collection):
    "a Python function that lists all documents in a collection"
    return list(mongo_collection.find())