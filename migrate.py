"""Applies migrations/*.sql that aren't recorded in schema_migrations."""

import os
import pathlib

import psycopg

with psycopg.connect(os.environ["DATABASE_URL"], autocommit=True) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS schema_migrations (version text PRIMARY KEY)")
    done = {row[0] for row in conn.execute("SELECT version FROM schema_migrations")}
    for path in sorted(pathlib.Path("migrations").glob("*.sql")):
        if path.stem not in done:
            with conn.transaction():
                conn.execute(path.read_text())
                conn.execute("INSERT INTO schema_migrations VALUES (%s)", (path.stem,))
                print(f"applied {path.stem}")
