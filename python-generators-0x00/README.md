# User Data Seeder

This Python script seeds a MySQL database with user data from a CSV file. It generates unique `user_id`s for each record if not present in the CSV.

## Features

- Creates MySQL database and table if not existing.
- Reads user data from CSV (`name`, `email`, `age`).
- Generates UUIDs for `user_id` as primary key.
- Inserts or updates records using upsert.

## Requirements

- Python 3.x
- `mysql-connector-python`
- `python-dotenv`

## Setup

1. Install dependencies:

   ```bash
   pip install mysql-connector-python python-dotenv

   ```
---
## 2. Create a .env file with your DB credentials:

```bash
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=your_password
```
---

## 3. Place your CSV file (without user_id column) in the data/ folder.

```bash
    python 0/seed.py
 ```
 This will create the database, table, and populate it with data from your CSV.
