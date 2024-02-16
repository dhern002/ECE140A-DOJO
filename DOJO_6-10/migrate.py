import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables


def get_db_connection():
    return mysql.connector.connect(
        host="localhost", # because we are inside docker compose, we can use the service name as the host name
        user="root",
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )


# Path to the migrations folder
migrations_folder = 'migrations'


def apply_migration(file_path):
    """
    Apply a single migration file using the given database connection.
    """
    print(f"Applying migration: {file_path}")
    with open(file_path, 'r') as file:
        migration_sql = file.read()
        try:
            cursor.execute(migration_sql)
            cnx.commit()
            print(f"Successfully applied {file_path}")
        except mysql.connector.Error as err:
            print(f"Failed to apply {file_path}: {err}")

def apply_migrations(directory):
    """
    Apply all migration files in the specified directory, in alphabetical order.
    """
    # Get a list of .sql files in the specified directory
    files = [f for f in os.listdir(directory) if f.endswith('.sql')]
    # Sort the files alphabetically
    files.sort()

    for file in files:
        file_path = os.path.join(directory, file)
        apply_migration(file_path)


if __name__ == "__main__":
    # Connect to the database
    try:
        cnx = get_db_connection()
        cursor = cnx.cursor()
        apply_migrations(migrations_folder)
    except mysql.connector.Error as err:
        print(f"Failed to connect to database: {err}")
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()
