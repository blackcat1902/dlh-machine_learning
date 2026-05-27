#!/usr/bin/env python3

"""top students """

def top_students(mongo_collection):
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$scores"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
