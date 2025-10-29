import psycopg2
import os
import allure

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "secret"),
        database=os.getenv("DB_NAME", "testdb")
    )

@allure.step("Create table 'users' if not exists")
def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@allure.step("Insert user '{name}' with age {age}")
def insert_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s);", (name, age))
    conn.commit()
    cur.close()
    conn.close()

@allure.step("Update user with id={id} to name='{name}', age={age}")
def update_user(id, name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s;", (name, age, id))
    conn.commit()
    cur.close()
    conn.close()

@allure.step("Delete user with id={id}")
def delete_user(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s;", (id,))
    conn.commit()
    cur.close()
    conn.close()

@allure.step("Get all users from database")
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
