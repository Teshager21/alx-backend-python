# 🎯 ALX Backend - Advanced Python Exercises 🚀  
**Focus Areas:** Generators • Decorators • Context Managers • Async Programming

## 📚 Objective

To deepen backend Python expertise by implementing advanced techniques like generators, decorators, context managers, and asynchronous programming. These patterns are essential for writing efficient, readable, and maintainable code — particularly for scalable data processing, resource management, and concurrent execution.

---

## 🧠 Key Concepts Covered

- **Generators** – Creating memory-efficient iterators for streaming large datasets  
- **Decorators** – Enhancing or modifying function behavior, such as logging, caching, retries, and transaction handling  
- **Context Managers** – Managing setup and teardown logic for resources like database connections  
- **Asynchronous Programming** – Running concurrent database operations using `async/await`, `aiosqlite`, and `asyncio.gather()`

---

## 🗂️ Exercises Overview

### ✅ Generators

#### 1. Stream Users One by One
- **Function:** `stream_users()`
- **Description:** Yields rows one at a time from the `user_data` table.
- **Concept:** Memory-efficient iteration over database results.

#### 2. Stream Users in Batches
- **Function:** `stream_users_in_batches(batch_size)`
- **Description:** Fetches and yields batches of users for batch processing.
- **Concept:** Balanced trade-off between memory and performance.

#### 3. Lazy Pagination
- **Function:** `lazy_paginate(page_size)`
- **Description:** Yields paginated data lazily from the database.
- **Concept:** Efficient pagination using generators.

#### 4. Memory-Efficient Average Age Calculation
- **Function:** `calculate_average_age()`
- **Description:** Streams user ages and computes the average without loading all data at once.
- **Concept:** Streaming aggregation with generators.

---

### ✅ Decorators

#### 5. SQL Query Logging
- **Decorator:** `@log_queries`
- **Description:** Logs SQL queries before execution for observability.

#### 6. Connection Management
- **Decorator:** `@with_db_connection`
- **Description:** Automatically opens and closes the database connection.

#### 7. Transaction Handling
- **Decorator:** `@transactional`
- **Description:** Wraps DB operations with commit/rollback support.

#### 8. Retry on Failure
- **Decorator:** `@retry_on_failure(retries=3, delay=2)`
- **Description:** Retries DB operations on transient errors.

#### 9. Query Caching
- **Decorator:** `@cache_query`
- **Description:** Caches query results to reduce redundant DB hits.

---

### ✅ Context Managers

#### 10. Class-Based Connection Manager
- **Class:** `DatabaseConnection`
- **Description:** Manages `__enter__` and `__exit__` for SQLite connection lifecycle.

#### 11. Query Execution Context
- **Class:** `ExecuteQuery`
- **Description:** Takes a parameterized SQL query and returns the result in a managed context.

---

### ✅ Asynchronous Programming

#### 12. Async Fetching with `aiosqlite`
- **Functions:** `async_fetch_users()` & `async_fetch_older_users()`
- **Description:** Uses `asyncio.gather()` to fetch users concurrently.
- **Concept:** Asynchronous I/O for non-blocking DB operations.

---

## ⚙️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx-backend-python-advanced.git
   cd alx-backend-python-advanced
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your MySQL credentials:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=ALX_prodev
   ```

---

## 🧪 Usage

Each script can be run individually, e.g.:

```bash
python 0-stream_users.py
python 4-log_queries.py
python 8-async_fetch.py
```

---

## 📌 Notes

- SQLite is used for some advanced tasks (decorators, context managers, async).
- MySQL is used for streaming and generator exercises.
- Make sure corresponding tables exist and are seeded appropriately before testing.

---

Let me know if you’d like a `requirements.txt` or `.env.example` added!