import sqlite3

connection = sqlite3.connect('gym_database.db')
connection.execute('ALTER TABLE gym_equipment ADD COLUMN location TEXT')
connection.commit
