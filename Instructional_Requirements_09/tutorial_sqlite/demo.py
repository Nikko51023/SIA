import sqlite3

connection = sqlite3.connect('gym_database.db')

connection.execute('''CREATE TABLE IF NOT EXISTS gym_equipment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    year_acquired INTEGER
    )''')

# Insert data into the table
gym_data = [
    ('Treadmill', 'Cardio', 2018),
    ('Dumbbells', 'Strength Training', 2015),
    ('Stationary Bike', 'Cardio', 2020),
    ('Bench Press', 'Strength Training', 2017),
    ('Rowing Machine', 'Cardio', 2019),
]

connection.executemany('INSERT INTO gym_equipment (name, category, year_acquired) VALUES (?, ?, ?)', gym_data)

# query data from the table
result = connection.execute('SELECT * FROM gym_equipment')
data = result.fetchall()

# display the data
for row in data:
    print(f'Name: {row[1]}')
    print(f'Category: {row[2]}')
    print(f'Year Acquired: {row[3]}')
    print('')

# Write the data to the file
connection.commit()

# Close the database connection
connection.close()