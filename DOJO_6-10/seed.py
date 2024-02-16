import mysql.connector
import os
import hashlib


def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def seed_users():
    # User data to seed
    users = [
        {'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'}
    ]

    try:
        # Connect to the MySQL database using environment variables
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('MYSQL_ROOT_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        cursor = conn.cursor()

        for user in users:
            hashed_pwd = hash_password(user['password'])
            query = ("INSERT INTO users (username, email, hashed_password) "
                     "VALUES (%s, %s, %s)")
            data = (user['username'], user['email'], hashed_pwd)

            # Execute the query
            cursor.execute(query, data)

        # Commit the transaction
        conn.commit()
        print(f"Successfully seeded {len(users)} users.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    seed_users()
