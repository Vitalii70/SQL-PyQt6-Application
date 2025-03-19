"""
Module for performing core database operations.

This module contains the essential functionality for interacting with the database, including creating, reading, updating, and deleting (CRUD) data. It provides methods for executing SQL queries and managing database connections.
"""

import sqlite3
import hashlib
import os

def create_table(name_of_table, columns_data):
    # Connect zu DB
    try:
        conn = sqlite3.connect(f"C:\\reps\\SQL-PyQt6-Application\\app\\database\\created_databases\\{name_of_table}.db")
        cursor = conn.cursor()
    except Exception as e:
        print(f"Database connection error: {e}")
        return

    # list für Zukunfte Tabelle
    column_definitions = []
    for column in columns_data:
        if isinstance(column["name"], str):
            column_name = column["name"]
        else:
            column_name = column["name"].text()
        column_type = column["type"]
        column_pk = column["PRIMARY KEY"]
        column_nn = column["NOT NULL"]

        # Fügen name und type in column_parts
        column_parts = [column_name, column_type]

        # Fügen die andere Attributen hinzu
        if column_pk:
            column_parts.append("PRIMARY KEY")
        if column_nn:
            column_parts.append("NOT NULL")

        # Machen die Teilen in einer Str
        column_definitions.append(" ".join(column_parts))

    # Machen SQL-Request für Erstellt Tabelle
    sql_query = f"""
        CREATE TABLE IF NOT EXISTS {name_of_table} (
            {", ".join(column_definitions)}
        )
    """
    print(f"SQL Query: {sql_query}") # Für console

    # SQL-Request
    try:
        cursor.execute(sql_query)
        conn.commit()
        print(f"Table '{name_of_table}' created successfully.")
    except Exception as e:
        print(f"Error executing SQL: {e}")
    finally:
        conn.close()


def control_data(name, password_he):
    """Checking the correctness of the password and name"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "..", "database/data_users.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except Exception as e:
        print(f"Database connection error: {e}")
        return

    hash_object = hashlib.sha256()
    hash_object.update(str(password_he).encode('utf-8'))
    hashed_password = hash_object.hexdigest()

    query = "SELECT * FROM datausers WHERE name = ? AND password_hash = ?"
    cursor.execute(query, (name, hashed_password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return True  # if date from user is correct
    else:
        return False

def create_new_account(username, password):
    """Create a new user in db"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "..", "database/data_users.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        hash_object = hashlib.sha256()
        hash_object.update(password.encode('utf-8'))
        password_hash = hash_object.hexdigest()

        cursor.execute("INSERT INTO datausers (name, password_hash) VALUES (?, ?)",
                       (username, password_hash))

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Database connection error: {e}")
        return
