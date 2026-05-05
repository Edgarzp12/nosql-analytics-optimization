import time

start = time.time()
import pandas as pd
from pymongo import MongoClient
from config import MONGO_HOST, MONGO_PORT
import time

start = time.time()


# 1. load CSV
df = pd.read_csv("data/dataset.csv")

# 2. Data cleaning

# Replace strings "nan" by None
df = df.replace("nan", None)

# Remove rows without category
df = df[df["category_code"].notna()]

# Convert event_time to datetime
df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

df = df[df["event_time"].notna()]

# 3. Convert to dictionaries
data_dict = df.to_dict("records")

# 4. Connect to Mongo
client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client["ecommerce"]

collection = db["orders"]
collection.drop()

# 5. Insert cleaned data
result = collection.insert_many(data_dict)
print(f"Inserted {len(result.inserted_ids)} cleaned documents.")

# 6. Create indices
collection.create_index({ "category_code": 1 })
collection.create_index({ "brand": 1 })
collection.create_index({ "event_time": 1 })

print("Load + cleaning completed.")

# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")
