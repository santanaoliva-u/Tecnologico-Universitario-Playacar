# app/database.py

import sqlite3

def create_db():
    conn = sqlite3.connect('profiles.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            photo TEXT,
            email TEXT,
            phone TEXT,
            birth_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_profile(profile):
    conn = sqlite3.connect('profiles.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO profiles (name, photo, email, phone, birth_date) 
        VALUES (?, ?, ?, ?, ?)
    ''', (profile['name'], profile['photo'], profile['email'], profile['phone'], profile['birth_date']))
    conn.commit()
    conn.close()
