"""
Query in Redis:
Counts all categories and determines which appears most frequently.
"""
import time

start = time.time()
import redis
from config import REDIS_HOST, REDIS_PORT

# 1. Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

categories = {}

# 2. Iterate over all transactions in Redis
for key in r.scan_iter("transaction:*"):

    data = r.hgetall(key)

    category = data.get("category_code")

    # Ignore "unknown" values
    if not category or category.lower() == "unknown":
        continue

    categories[category] = categories.get(category, 0) + 1

# 3. Find the category with the most sales
if categories:
    category_top = max(categories, key=categories.get)
    total = categories[category_top]
    print(f"The most sold category was '{category_top}' with {total} sales.")
else:
    print("No categories found.")

# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")