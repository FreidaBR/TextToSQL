import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta
from pathlib import Path
fake = Faker()


DB_PATH = Path(__file__).parent / "ecommerce.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# --------------------
# Customers
# --------------------
for _ in range(100):
    cursor.execute("""
    INSERT INTO Customers(name,email,city)
    VALUES(?,?,?)
    """, (
        fake.name(),
        fake.email(),
        fake.city()
    ))

# --------------------
# Products
# --------------------

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Sports",
    "Home"
]

for i in range(50):

    cursor.execute("""
    INSERT INTO Products(product_name,category,price)
    VALUES(?,?,?)
    """, (
        fake.word().capitalize(),
        random.choice(categories),
        round(random.uniform(10,1000),2)
    ))

# --------------------
# Orders
# --------------------

for i in range(300):

    customer = random.randint(1,100)

    random_date = datetime(2024,1,1)+timedelta(
        days=random.randint(0,365)
    )

    total = round(random.uniform(50,5000),2)

    cursor.execute("""
    INSERT INTO Orders(customer_id,order_date,total_amount)
    VALUES(?,?,?)
    """,(
        customer,
        random_date.date(),
        total
    ))

# --------------------
# Order Items
# --------------------

for i in range(700):

    cursor.execute("""
    INSERT INTO OrderItems(order_id,product_id,quantity)
    VALUES(?,?,?)
    """,(
        random.randint(1,300),
        random.randint(1,50),
        random.randint(1,5)
    ))

conn.commit()
conn.close()

print("Fake data inserted successfully!")