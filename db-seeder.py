import mysql.connector
from faker import Faker
from dotenv import load_dotenv
import random
import os

# Create a Faker instance and load the environment variables
fake = Faker()
load_dotenv()

def insert_customers(cursor, n=10000):
    for _ in range(n):
        name = fake.name()
        email = fake.email()
        city = fake.city()
        cursor.execute("INSERT INTO customers (name, email, city) VALUES (%s, %s, %s)", (name, email, city))

def insert_suppliers(cursor, n=10000):
    for _ in range(n):
        name = fake.company()
        contact_name = fake.name()
        city = fake.city()
        cursor.execute("INSERT INTO suppliers (name, contact_name, city) VALUES (%s, %s, %s)", (name, contact_name, city))

def insert_categories(cursor, n=4):
    for _ in range(n):
        name = fake.word().capitalize()
        description = fake.sentence(nb_words=6)
        cursor.execute("INSERT INTO categories (name, description) VALUES (%s, %s)", (name, description))





def insert_products(cursor, categories_count, suppliers_count, n=10000):
    for _ in range(n):
        name = fake.word().capitalize()
        price = round(random.uniform(50, 2000), 2)
        category_id = random.randint(1, categories_count)
        supplier_id = random.randint(1, suppliers_count)
        cursor.execute("INSERT INTO products (name, price, category_id, supplier_id) VALUES (%s, %s, %s, %s)", (name, price, category_id, supplier_id))

def insert_orders(cursor, customers_count, n=10000):
    statuses = ['Shipped', 'Processing', 'Delivered', 'Cancelled']  # Example statuses
    for _ in range(n):
        customer_id = random.randint(1, customers_count)  # Assuming you have at least this many customers
        order_date = fake.date_between(start_date='-2y', end_date='today').isoformat()
        status = random.choice(statuses)
        cursor.execute("INSERT INTO orders (customer_id, order_date, status) VALUES (%s, %s, %s)", (customer_id, order_date, status))


def insert_order_items(cursor, orders_count, products_count, n=10000):
    for _ in range(n):
        order_id = random.randint(1, orders_count)  # Assuming you have at least this many orders
        product_id = random.randint(1, products_count)  # Assuming you have at least this many products
        quantity = random.randint(1, 10)  # Example quantity range
        cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)", (order_id, product_id, quantity))


def seed(n=1000):


    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )

    cursor = conn.cursor()

    insert_categories(cursor, 4)
    conn.commit()
    insert_suppliers(cursor, n)
    conn.commit()
    insert_customers(cursor, n)
    conn.commit()
    insert_products(cursor, 4, n)
    conn.commit()
    insert_orders(cursor, n, n)
    conn.commit()
    insert_order_items(cursor, n, n)
    conn.commit()

    cursor.close()
    conn.close()

    print("Data insertion completed.")

if __name__ == "__main__":
    seed(1000)
    pass