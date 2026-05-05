"""
Query in Redis:
Sums revenue by brand and determines which generated the most money.
"""
import time

start = time.time()
import redis
from config import REDIS_HOST, REDIS_PORT

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

brands = {}

# Get all keys with format "transaction:*"
for key in r.scan_iter("transaction:*"):

    data = r.hgetall(key)

    brand = data.get("brand")
    price = data.get("price")

    # Validation
    if not brand or brand == "unknown":
        continue

    try:
        price = float(price)
    except (TypeError, ValueError):
        continue

    # Acumulate revenue by brand
    brands[brand] = brands.get(brand, 0.0) + price

# Results
if brands:
    brand_top = max(brands, key=brands.get)
    ingresos = round(brands[brand_top], 2)
    print(f"The brand with the highest revenue was '{brand_top}' with ${ingresos}.")
else:
    print("No brands found.")


# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")