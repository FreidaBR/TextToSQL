from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "ecommerce.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Drop existing tables (optional)
cursor.execute("DROP TABLE IF EXISTS OrderItems")
cursor.execute("DROP TABLE IF EXISTS Orders")
cursor.execute("DROP TABLE IF EXISTS Products")
cursor.execute("DROP TABLE IF EXISTS Customers")

# Customers Table
cursor.execute("""
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    city TEXT
)
""")

# Products Table
cursor.execute("""
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL
)
""")

# Orders Table
cursor.execute("""
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date DATE,
    total_amount REAL,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
)
""")

# Order Items Table
cursor.execute("""
CREATE TABLE OrderItems (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
""")

conn.commit()
conn.close()

print("Database created successfully!")