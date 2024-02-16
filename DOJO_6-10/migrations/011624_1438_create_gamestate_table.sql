CREATE TABLE IF NOT EXISTS gamestate (
    game_id INT NOT NULL,
    user_id INT NOT NULL,
    guesses INT,
    guessed_letters VARCHAR(30),
    state enum('in_progress', 'won', 'lost'),
    FOREIGN KEY (game_id) REFERENCES game(id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);