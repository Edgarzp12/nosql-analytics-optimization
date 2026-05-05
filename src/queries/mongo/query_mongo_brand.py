"""
Query in MongoDB:
Gets the brand with the highest revenue (total price sum).
"""
import time

start = time.time()
from pymongo import MongoClient
from config import MONGO_HOST, MONGO_PORT

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client["ecommerce"]
collection = db["orders"]

# Pipeline:
# 1. Filtrate valid brands (brand != None)
# 2. Group by brand and sum the price (revenue)
# 3. Sort from highest to lowest revenue
# 4. Limitate to 1 brand
pipeline = [
    { "$match": { "brand": { "$ne": None } } },
    { "$group": { "_id": "$brand", "revenue": { "$sum": "$price" } }},
    { "$sort": { "revenue": -1 }},
    { "$limit": 1 }
]

res = list(collection.aggregate(pipeline))

if res:
    marca = res[0]["_id"]
    ingresos = round(res[0]["revenue"], 2)
    print(f"The brand with the highest revenue was '{marca}' with ${ingresos}.")
else:
    print("No brands found.")

# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")
