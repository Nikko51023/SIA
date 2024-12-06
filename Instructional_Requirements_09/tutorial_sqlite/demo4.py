import sqlite3

connection = sqlite3.connect('gym_database.db')

connection.execute('''CREATE TABLE IF NOT EXISTS gym_employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    role TEXT
    )''')

# Insert data into the table
employee_data = [
    ('Jacob', 25, 'Trainer'),
    ('Jake', 30, 'Receptionist'),
    ('Russel', 35, 'Manager'),
    ('Jared', 40, 'Maintenance'),
    ('Jay', 45, 'Nutritionist'),
    ('Augustu', 38, 'Trainer'),
]

# connection.executemany('INSERT INTO gym_employees (name, age, role) VALUES (?, ?, ?)', employee_data)

# query data from the table
result = connection.execute('SELECT * FROM gym_employees ORDER BY age DESC')
data = result.fetchall()

# display the data
for row in data:
    print(f'Name: {row[1]}')
    print(f'Age: {row[2]}')
    print(f'Role: {row[3]}')
    print('')

# Write the data to the file
connection.commit()

# Close the database connection
connection.close()