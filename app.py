"""A small store backend. Every query the app makes is in this file."""

import os

import psycopg


def connect():
    return psycopg.connect(os.environ["DATABASE_URL"])


def create_user(conn, name, email):
    row = conn.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (name, email)
    ).fetchone()
    return row[0]


def get_user(conn, user_id):
    return conn.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,)).fetchone()


def rename_user(conn, user_id, name):
    conn.execute("UPDATE users SET name = %s WHERE id = %s", (name, user_id))


def place_order(conn, user_id, total_cents):
    row = conn.execute(
        "INSERT INTO orders (user_id, total_cents) VALUES (%s, %s) RETURNING id", (user_id, total_cents)
    ).fetchone()
    return row[0]


def order_history(conn, user_id):
    return conn.execute(
        "SELECT o.id, o.total_cents, u.name FROM orders o JOIN users u ON u.id = o.user_id "
        "WHERE o.user_id = %s ORDER BY o.created_at",
        (user_id,),
    ).fetchall()
