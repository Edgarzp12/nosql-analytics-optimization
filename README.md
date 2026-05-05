# NoSQL Analytics Optimization: MongoDB vs Redis

## Overview

This project compares MongoDB and Redis for analytical workloads using a large-scale e-commerce dataset (~2M+ records). It evaluates how each system performs when executing aggregation queries on transactional data.

## Key Features

* Data ingestion pipelines for MongoDB and Redis
* Data cleaning and normalization process
* Analytical queries on:

  * Top-selling category
  * Brand with highest revenue
  * Month with most sales
  * Execution time benchmarking

## Tech Stack

* Python
* MongoDB
* Redis
* Docker

## Dataset

E-commerce purchase history dataset with ~2.6M records, reduced to ~2.0M after cleaning. 

## Methodology

1. Load cleaned data into MongoDB (document model)
2. Load transformed data into Redis (key-value model)
3. Execute equivalent queries in both systems
4. Measure execution time for each query

## Results

| Query               | MongoDB  | Redis   |
| ------------------- | -------- | ------- |
| Top Category        | ~5.9 sec | ~11 min |
| Top Brand (Revenue) | ~5.8 sec | ~12 min |
| Top Month           | ~3.7 sec | ~12 min |

## Key Insights

* MongoDB outperforms Redis by up to **100x+** in analytical queries
* Redis is inefficient for aggregation-heavy workloads due to lack of query engine
* MongoDB’s aggregation pipeline and indexing enable scalable analytics
* Data cleaning was critical to obtain valid results

## How to Run

```bash
docker-compose up
pip install -r requirements.txt
```

Load data:

```bash
python src/ingestion/load_mongo.py
python src/ingestion/load_redis.py
```

Run queries:

```bash
python src/queries/mongo/query_mongo_brand.py
python src/queries/redis/query_redis_brand.py
```

## Conclusion

MongoDB is significantly more suitable for large-scale analytical queries, while Redis is better suited for caching and fast key-value access.

## Limitations
- Redis queries are executed client-side (Python), not natively
- No parallelization implemented

## Author

Edgar Antonio Zeledón Pérez
