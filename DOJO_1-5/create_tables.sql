CREATE TABLE IF NOT EXISTS game (
    id INT AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(6) NOT NULL,
    created_by int NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS game_completions (
    game_id INT NOT NULL,
    user_id INT NOT NULL,
    guesses INT NOT NULL,
    FOREIGN KEY (game_id) REFERENCES game(id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);