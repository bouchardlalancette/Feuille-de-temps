from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Création de la table pour les heures de travail
    c.execute('''
        CREATE TABLE IF NOT EXISTS work_time (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT NOT NULL,
            week_end_date TEXT NOT NULL,
            sunday_hours REAL,
            monday_hours REAL,
            tuesday_hours REAL,
            wednesday_hours REAL,
            thursday_hours REAL,
            friday_hours REAL,
            saturday_hours REAL
        )
    ''')
    # Créer la table employees si elle n'existe pas
    c.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT,
            hourly_rate REAL,
            department TEXT,
            start_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Appel de la fonction d'initialisation de la base de données
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fdt')
def fdt():
    return render_template('fdt.html')

@app.route('/log', methods=['POST'])
def log_time():
    print(request.form.keys())  # Imprimer les clés de formulaire pour le débogage
    employee_name = request.form['employee_name']
    week_end_date = request.form['week_end_date']
    sunday_hours = request.form['sunday_hours']
    monday_hours = request.form['monday_hours']
    tuesday_hours = request.form['tuesday_hours']
    wednesday_hours = request.form['wednesday_hours']
    thursday_hours = request.form['thursday_hours']
    friday_hours = request.form['friday_hours']
    saturday_hours = request.form['saturday_hours']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO work_time (
            employee_name, week_end_date, sunday_hours, monday_hours, tuesday_hours,
            wednesday_hours, thursday_hours, friday_hours, saturday_hours
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (employee_name, week_end_date, sunday_hours, monday_hours, tuesday_hours, wednesday_hours, thursday_hours, friday_hours, saturday_hours))
    conn.commit()
    conn.close()
    return "Heures enregistrées!"

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        hourly_rate = request.form['hourly_rate']
        department = request.form['department']
        start_date = request.form['start_date']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO employees (name, position, hourly_rate, department, start_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, position, hourly_rate, department, start_date))
        conn.commit()
        conn.close()
        return "Employé ajouté!"
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)
