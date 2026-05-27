#!/usr/bin/env python3
def top_students(mongo_collection):
    """
    Returns all students sorted by average score (descending),
    with 'averageScore' included in each document.
    """

    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
