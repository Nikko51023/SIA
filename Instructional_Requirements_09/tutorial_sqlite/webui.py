from flask import Flask, render_template, request, redirect # type: ignore
import sqlite3

app = Flask(__name__)

DATABASE = 'gym_database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    equipment = conn.execute('SELECT * FROM gym_equipment').fetchall()
    conn.close()
    return render_template('index.html', equipment=equipment)

@app.route('/add_equipment', methods=['POST'])
def add_equipment():
    name = request.form.get('name')
    category = request.form.get('category')
    year_acquired = request.form.get('year_acquired')

    conn = get_db_connection()
    conn.execute('INSERT INTO gym_equipment (name, category, year_acquired) VALUES (?, ?, ?)', (name, category, year_acquired))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)