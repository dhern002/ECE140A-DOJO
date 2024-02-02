CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, description, price) VALUES
('Laptop', 'A high-performance laptop.', 1200.00),
('Smartphone', 'An advanced smartphone.', 800.00),
('Tablet', 'A versatile tablet.', 600.00);
