-- Drop existing tables if they exist
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS categories;

-- Create tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY auto_increment,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY auto_increment,
    name VARCHAR(100),
    contact_name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY auto_increment,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE products (
    product_id INT PRIMARY KEY auto_increment,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    category_id INT,
    supplier_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY auto_increment,
    customer_id INT,
    order_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY auto_increment,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
