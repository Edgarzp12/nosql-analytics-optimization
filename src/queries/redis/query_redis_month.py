"""
Query in Redis:
Determines the month with the most sales (YYYY-MM).
"""
import time

start = time.time()
import redis
from config import REDIS_HOST, REDIS_PORT
from datetime import datetime

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

months = {}

# Get all keys with format "transaction:*"
for key in r.scan_iter("transaction:*"):

    data = r.hgetall(key)

    event_time = data.get("event_time")
    if not event_time:
        continue

    # Format ISO: "2020-08-15 05:46:01+00:00"
    try:
        date = datetime.fromisoformat(event_time)
    except ValueError:
        continue

    month = date.strftime("%Y-%m")

    months[month] = months.get(month, 0) + 1

# Results
if months:
    month_top = max(months, key=months.get)
    total = months[month_top]
    print(f"The month with the most sales was {month_top} with {total} sales.")
else:
    print("No months found.")

# Measure execution time
end = time.time()
print(f"Execution time: {end - start:.4f} seconds")
