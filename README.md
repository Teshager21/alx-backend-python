# 🎯 ALX Backend - Python Generators Exercises 🚀

This repository contains a series of exercises focused on using Python generators for efficient data processing with a MySQL database.

## Exercises Overview

### 1. Stream Users One by One
- **Function:** `stream_users()`
- **Description:** A generator that fetches rows one by one from the `user_data` table.
- **Key Concept:** Yielding individual rows to avoid loading all data at once.
  
---

### 2. Stream Users in Batches
- **Functions:** `stream_users_in_batches(batch_size)` and `batch_processing(batch_size)`
- **Description:** Fetches users in batches, then processes each batch to filter users over age 25.
- **Key Concept:** Batch fetching combined with generator-based filtering using list comprehensions.
  
---

### 3. Lazy Pagination
- **Functions:** `paginate_users(page_size, offset)` and `lazy_paginate(page_size)`
- **Description:** Implements pagination by lazily loading pages of user data on demand using a generator.
- **Key Concept:** Efficiently fetching paginated data using offset and limit, yielding one page at a time.
  
---

### 4. Memory-Efficient Average Age Calculation
- **Functions:** `stream_user_ages()` and `calculate_average_age()`
- **Description:** Streams user ages one by one, then calculates the average age without loading the entire dataset into memory.
- **Key Concept:** Using generators for memory-efficient aggregate calculations without SQL aggregate functions.

---

## Setup

1. Clone this repo.
2. Install dependencies:
   ```bash
   pip install mysql-connector-python python-dotenv

---

## Create a .env file with your database credentials:
```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=ALX_prodev
```

---

## Ensure your MySQL database and user_data table are set up accordingly.

### Usage

Each exercise script can be run individually. For example:


```bash
python 0-stream_users.py
python 1-stream_users_batches.py
python 2-lazy_pagination.py
python 3-average_age.py
```
