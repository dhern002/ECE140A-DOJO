import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="emin",
    password="emin",
    database="emin"
)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Fetch data for older people
cursor.execute("""
    SELECT user_id, name, date_of_birth
    FROM users
    WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) >= 30
""")
older_people_data = cursor.fetchall()

# Fetch data for younger people
cursor.execute("""
    SELECT user_id, name, date_of_birth
    FROM users
    WHERE TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) < 30
""")
younger_people_data = cursor.fetchall()

# Fetch items bought by older people
cursor.execute("""
    SELECT o.user_id, i.item_name, i.price
    FROM orders o, items i
    WHERE o.item_id = i.item_id
    AND o.user_id IN ({})
""".format(','.join(map(str, [user[0] for user in older_people_data]))))
older_people_items_data = cursor.fetchall()

# Fetch items bought by younger people
cursor.execute("""
    SELECT o.user_id, i.item_name, i.price
    FROM orders o, items i
    WHERE o.item_id = i.item_id
    AND o.user_id IN ({})
""".format(','.join(map(str, [user[0] for user in younger_people_data]))))
younger_people_items_data = cursor.fetchall()

cursor.execute("""
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
GROUP BY age_group;""")
data = cursor.fetchall()
for x in data:
    print(x[0], ": ", x[1])

# Close the cursor and connection
cursor.close()
conn.close()

# Process data in Python to calculate total spending
def calculate_total_spending(data):
    total_spent = 0
    for row in data:
        total_spent += row[2]
    return total_spent

# Calculate total spending for older and younger people
total_spent_older = calculate_total_spending(older_people_items_data)
total_spent_younger = calculate_total_spending(younger_people_items_data)

# Print the results
print("Total Spending by Older People:", total_spent_older)
print("Total Spending by Younger People:", total_spent_younger)


