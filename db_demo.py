from __future__ import annotations

from sqlalchemy import text

from database import engine, init_db

def run_sql(query: str):
    """Run a raw SQL query on the same DB used by `database.py`.
    
    Example:
    rows = run_sql("SELECT * FROM appointments")
    print(rows)
    """
    
    #init_db()  # ensures the appointments table exists
    with engine.begin() as conn:
        result = conn.execute(text(query))
        return result.fetchall() if result.returns_rows else result.rowcount
    

#query = """SELECT * FROM appointments;"""
query = """INSERT INTO appointments (patient_name, reason, start_time, canceled, created_at) VALUES ('John Doe', 'Checkup', '2026-01-24 14:30:00', 0, datetime('now'));"""
print(run_sql(query))