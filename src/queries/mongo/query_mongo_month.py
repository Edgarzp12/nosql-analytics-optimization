"""
Query in MongoDB:
Determines the month with the most sales (event_time is already in datetime format).
"""
import time

start = time.time()
from pymongo import MongoClient
from config import MONGO_HOST, MONGO_PORT

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client["ecommerce"]
collection = db["orders"]

# Pipeline:
# 1. Project a new field "month" with format YYYY-MM
# 2. Group by month and sum sales
# 3. Sort descendingly
# 4. Take the first result
pipeline = [
    { "$project": { 
        "month": { "$dateToString": { "format": "%Y-%m", "date": "$event_time" }}
    }},
    { "$group": { "_id": "$month", "total": { "$sum": 1 } }},
    { "$sort": { "total": -1 }},
    { "$limit": 1 }
]

res = list(collection.aggregate(pipeline))

if res:
    month = res[0]["_id"]
    total = res[0]["total"]
    print(f"The month with the most sales was {month} with {total} sales.")
else:
    print("No months found.")

# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")
