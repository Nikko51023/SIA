import sqlite3

connection = sqlite3.connect('gym_database.db')

connection.execute('''CREATE TABLE IF NOT EXISTS gym_members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
    )''')

connection.execute('''CREATE TABLE IF NOT EXISTS fitness_programs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT,
    member_id INTEGER,
    FOREIGN KEY (member_id) REFERENCES gym_members(id)
    )''')

member_data = [
    ('Harper', 22),
    ('Benjamin', 36),
    ('Amos', 30),
    ('Zoe', 28),
    ('Henry', 33),
]

program_data = [
    ('Weight Loss', 1),
    ('Strength Training', 2),
    ('Cardio', 3),
    ('Flexibility', 4),
    ('Bodybuilding', 5),
]

connection.executemany('INSERT INTO gym_members (name, age) VALUES (?, ?)', member_data)
connection.executemany('INSERT INTO fitness_programs (program_name, member_id) VALUES (?, ?)', program_data)

results = connection.execute('''
    SELECT gym_members.name, fitness_programs.program_name
    FROM gym_members
    INNER JOIN fitness_programs ON gym_members.id = fitness_programs.member_id
''')

connection.commit()

print("Gym Members and their Fitness Programs:")
for row in results.fetchall():
    print(f"Member: {row[0]}, Program: {row[1]}")

connection.close()