#!/usr/bin/env python3
"""Displays info about logs

    Given a MongoDB collection of logs,
    counts documents for each method and
    displays the information."""
from pymongo import MongoClient


# Ensures module doesn't run on import
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_col = client.logs.nginx    # Our logs collection
    amount = logs_col.count_documents({})   # Total of documents in nginx
    get_status = logs_col.count_documents({"method": "GET", "path": "/status"})

    # Dictionary tying each method to its total count
    method = {
        "GET": logs_col.count_documents({"method": "GET"}),
        "POST": logs_col.count_documents({"method": "POST"}),
        "PUT": logs_col.count_documents({"method": "PUT"}),
        "PATCH": logs_col.count_documents({"method": "PATCH"}),
        "DELETE": logs_col.count_documents({"method": "DELETE"})
        }

    print(f"{amount} logs\nMethods:")
    # Iterates over 'method' to print all five lines
    for key, val in method.items():
        print(f"\tmethod {key}: {val}")
    print(f"{get_status} status check")
