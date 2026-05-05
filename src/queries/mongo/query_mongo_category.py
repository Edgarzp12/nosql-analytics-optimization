"""
Query in MongoDB:
Gets the category with the highest sales (highest number of documents).
"""
import time

start = time.time()
from pymongo import MongoClient
from config import MONGO_HOST, MONGO_PORT

# 1. Connection to Mongo
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client["ecommerce"]
collection = db["orders"]

# 2. Aggregation pipeline
#    - Group by category
#    - Count how many sales there are per category
#    - Sort from highest to lowest
#    - Return only the first (the best-selling)
pipeline = [
    { "$group": { "_id": "$category_code", "count": { "$sum": 1 } }},
    { "$sort": { "count": -1 }},
    { "$limit": 1 }
]

# 3. Execute query
res = list(collection.aggregate(pipeline))

# 4. Print result in a friendly format
if res:
    category = res[0]["_id"]
    cantidad = res[0]["count"]
    print(f"The best-selling category was '{category}' with {cantidad} sales.")
else:
    print("No results found.")

# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")