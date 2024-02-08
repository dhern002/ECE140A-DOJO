# DROP TABLE items;
-- Create the users table
CREATE TABLE IF NOT EXISTS users (
                       user_id INT AUTO_INCREMENT PRIMARY KEY,
                       username VARCHAR(50) NOT NULL,
                       password VARCHAR(100) NOT NULL,
                       name VARCHAR(100) NOT NULL,
                       date_of_birth DATE NOT NULL,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the items table
CREATE TABLE IF NOT EXISTS items (
                       item_id INT AUTO_INCREMENT PRIMARY KEY,
                       item_name VARCHAR(100) NOT NULL,
                       description TEXT,
                       price DECIMAL(10, 2) NOT NULL,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the orders table
CREATE TABLE IF NOT EXISTS orders (
                        order_id INT AUTO_INCREMENT PRIMARY KEY,
                        user_id INT NOT NULL,
                        item_id INT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(user_id),
                        FOREIGN KEY (item_id) REFERENCES items(item_id),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT users.name AS name, items.item_name
FROM users
         INNER JOIN orders ON users.user_id = orders.user_id
         INNER JOIN items ON orders.item_id = items.item_id;


SELECT users.name AS name,
       SUM(items.price) AS total_spent
FROM users
         LEFT JOIN orders ON users.user_id = orders.user_id
         LEFT JOIN items ON orders.item_id = items.item_id
GROUP BY users.user_id, users.name;


SELECT
    users.name AS user_name,
    items.item_name,
    CASE
        WHEN TIMESTAMPDIFF(YEAR, users.date_of_birth, CURDATE()) >= 30 THEN 'Older Person'
        ELSE 'Younger Person'
        END AS age_group
FROM
    users
        LEFT JOIN orders ON users.user_id = orders.user_id
        LEFT JOIN items ON orders.item_id = items.item_id
ORDER BY age_group;

SELECT
    CASE
        WHEN TIMESTAMPDIFF(YEAR, users.date_of_birth, CURDATE()) >= 30 THEN 'Older Person'
        ELSE 'Younger Person'
        END AS age_group,
    SUM(items.price) AS total_spent
FROM
    users
        LEFT JOIN orders ON users.user_id = orders.user_id
        LEFT JOIN items ON orders.item_id = items.item_id
GROUP BY age_group;


# -- Insert into the users table
# INSERT INTO users (username, password, name, date_of_birth)
# VALUES
#     ('john_doe', 'password123', 'John Doe', '1990-05-15'),
#     ('jane_smith', 'securepass', 'Jane Smith', '1985-08-22'),
#     ('bob_jones', 'pass123word', 'Bob Jones', '1995-03-10'),
#     ('alice_green', 'green123', 'Alice Green', '1988-12-03'),
#     ('charlie_brown', 'brownie456', 'Charlie Brown', '1992-06-28'),
#     ('emily_white', 'whitepass', 'Emily White', '1987-02-14'),
#     ('david_miller', 'millerpass', 'David Miller', '1993-09-20'),
#     ('susan_black', 'blackie789', 'Susan Black', '1998-11-05'),
#     ('michael_hill', 'hillpass', 'Michael Hill', '1984-04-18'),
#     ('olivia_gray', 'gray456', 'Olivia Gray', '1996-07-25');
#
# -- Insert into the items table
# INSERT INTO items (item_name, description, price)
# VALUES
#     ('Laptop', 'High-performance laptop with 16GB RAM', 999.99),
#     ('Smartphone', 'Latest model with dual cameras', 599.99),
#     ('Headphones', 'Noise-canceling wireless headphones', 149.99),
#     ('Tablet', '10-inch display with fast processor', 299.99),
#     ('Camera', 'DSLR camera with 24MP sensor', 799.99),
#     ('Smartwatch', 'Fitness tracking and smart notifications', 129.99),
#     ('Printer', 'Wireless color printer with scanner', 199.99),
#     ('Gaming Console', 'Next-gen gaming console with 4K support', 499.99),
#     ('Bluetooth Speaker', 'Portable speaker with deep bass', 79.99),
#     ('External Hard Drive', '2TB storage for backups', 129.99);
#
# -- Insert into the orders table
# INSERT INTO orders (user_id, item_id)
# VALUES
#     (1, 2), (2, 1), (3, 3), (4, 4), (5, 5),
#     (6, 6), (7, 7), (8, 8), (9, 9), (10, 10);

-- Insert more random orders into the orders table
INSERT INTO orders (user_id, item_id)
VALUES
    (1, 5), (2, 8), (3, 2), (4, 6), (5, 1),
    (6, 10), (7, 3), (8, 9), (9, 4), (10, 7),
    (1, 1), (2, 9), (3, 7), (4, 3), (5, 6),
    (6, 2), (7, 10), (8, 4), (9, 8), (10, 5);

#
# INSERT INTO items (name, description, price) VALUES
# ('Laptop', 'A high-performance laptop.', 1200.00),
# ('Smartphone', 'An advanced smartphone.', 800.00),
# ('Tablet', 'A versatile tablet.', 600.00);

# CREATE TABLE IF NOT EXISTS notes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     note VARCHAR(1000) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
#
# INSERT INTO notes (note) VALUE ('Hi there!')
