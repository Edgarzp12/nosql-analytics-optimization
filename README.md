# NoSQL Analytics Optimization: MongoDB vs Redis

## Overview

This project evaluates the performance of two NoSQL technologies—MongoDB and Redis—for analytical workloads. It focuses on how different data storage strategies impact query latency and efficiency when performing aggregations on transactional data.

The goal is to simulate a real-world scenario where fast query responses are critical, such as dashboards or reporting systems.

---

## Objectives

* Compare MongoDB and Redis for analytical queries
* Implement data ingestion pipelines for both systems
* Evaluate performance across common aggregation use cases
* Understand trade-offs between flexibility and speed

---

## Technologies

* Python
* MongoDB (document-oriented database)
* Redis (in-memory data store)
* Docker

---

## Project Structure

```
.
├── data/                  # Raw dataset
├── docker/                # Docker configuration
├── src/
│   ├── ingestion/         # Data loading scripts
│   │   ├── load_mongo.py
│   │   └── load_redis.py
│   ├── queries/
│   │   ├── mongo/         # MongoDB queries
│   │   └── redis/         # Redis queries
│   └── config.py          # Database configuration
├── requirements.txt
└── README.md
```

---

## Data Description

The dataset consists of transactional records with attributes such as:

* Brand
* Category
* Date (monthly aggregation)
* Sales or transaction counts

---

## Methodology

### 1. Data Ingestion

* Data is loaded into MongoDB as structured documents
* The same data is transformed and stored in Redis using optimized key-value structures

### 2. Query Design

Equivalent analytical queries were implemented in both systems:

* Aggregation by brand
* Aggregation by category
* Aggregation by month

### 3. Performance Evaluation

Each query is executed in both databases to compare execution time and efficiency.

---

## Results (To Be Completed)

| Query Type | MongoDB (s) | Redis (s) |
| ---------- | ----------- | --------- |
| Brand      | TBD         | TBD       |
| Category   | TBD         | TBD       |
| Month      | TBD         | TBD       |

---

## Key Insights

* Redis is expected to outperform MongoDB in repeated analytical queries due to its in-memory architecture
* MongoDB provides greater flexibility for complex queries and dynamic schemas
* Choosing the right database depends on the specific use case (real-time vs flexible analytics)

---

## How to Run

### 1. Start services

```bash
docker-compose up
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Load data

```bash
python src/ingestion/load_mongo.py
python src/ingestion/load_redis.py
```

### 4. Run queries

```bash
python src/queries/mongo/query_mongo_brand.py
python src/queries/redis/query_redis_brand.py
```

---

## Future Improvements

* Add automated benchmarking and logging
* Visualize performance comparisons
* Extend dataset size for scalability testing
* Integrate with a BI tool for real-time dashboards

---

## Author

Edgar Antonio Zeledón Pérez
