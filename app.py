import os
import sqlite3
from flask import Flask, render_template, request, redirect, session, g

app = Flask(__name__)
app.secret_key = 'a_very_secret_key_12345'
DATABASE = "telephone.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    db = get_db()
    cursor = db.execute("SELECT * FROM directory")
    rows = cursor.fetchall()
    return render_template('index.html', rows=rows)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        db = get_db()
        db.execute("INSERT INTO directory (name, phone_number, address) VALUES (?, ?, ?)", (name, phone_number, address))
        db.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        db = get_db()
        cursor = db.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        
        if user and user['password'] == password:
            session['user'] = username
            return redirect('/add')
        else:
            return 'Invalid credentials'
    return render_template('login.html')

