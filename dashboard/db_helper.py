#This file will handle database interactions

import sqlite3
import os

# Move up one directory level from the current script's location
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Construct the correct path to the database
DB_PATH = os.path.join(BASE_DIR, "db", "taxi_data.db")

print(f"🔍 Database Path: {DB_PATH}")

def get_all_logs():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM logs")
        logs = cursor.fetchall()
        conn.close()
        return logs
    except Exception as e:
        print(f"❌ Database Error: {e}")  # Print any error
        return []

def insert_taxi_log(date, earnings, expenses, fuel_cost, mileage):
    """Insert a new taxi log entry into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO taxi_logs (date, earnings, expenses, fuel_cost, mileage)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, earnings, expenses, fuel_cost, mileage))

    conn.commit()
    conn.close()
    return {"message": "Data inserted successfully"}

def get_all_logs():
    """Retrieve all taxi logs from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM taxi_logs ORDER BY date DESC")
    logs = cursor.fetchall()

    conn.close()
    return logs

def get_total_earnings():
    """Fetch total earnings and expenses."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(earnings), SUM(expenses) FROM taxi_logs")
    result = cursor.fetchone()
    
    conn.close()
    
    total_earnings = result[0] if result[0] else 0
    total_expenses = result[1] if result[1] else 0
    return {"total_earnings": total_earnings, "total_expenses": total_expenses}


def get_avg_mileage():
    """Fetch average fuel efficiency (mileage per fuel unit)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(mileage / fuel_cost) FROM taxi_logs WHERE fuel_cost > 0")
    result = cursor.fetchone()
    
    conn.close()
    
    avg_mileage = result[0] if result[0] else 0
    return {"avg_mileage": round(avg_mileage, 2)}


def get_best_worst_days():
    """Find the best and worst earning days."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT date, earnings FROM taxi_logs ORDER BY earnings DESC LIMIT 1")
    best_day = cursor.fetchone()

    cursor.execute("SELECT date, earnings FROM taxi_logs ORDER BY earnings ASC LIMIT 1")
    worst_day = cursor.fetchone()

    conn.close()

    return {
        "best_day": {"date": best_day[0], "earnings": best_day[1]} if best_day else None,
        "worst_day": {"date": worst_day[0], "earnings": worst_day[1]} if worst_day else None
    }

def get_all_logs():
    try:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Enable dictionary-style row access
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM logs")
        logs = cursor.fetchall()
        conn.close()
        return [dict(row) for row in logs]
    except Exception as e:
        print(f"❌ Database Error: {e}")  # Print any error
        return []

# insert data into database that reciving from the UI input
def insert_taxi_data(date, earnings, fuel_expense, other_expense, distance_km):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO taxi_data (date, earnings, fuel_expense, other_expense, distance_km)
    VALUES (?, ?, ?, ?, ?)
    """, (date, earnings, fuel_expense, other_expense, distance_km))
    
    conn.commit()
    conn.close()

# to fetch data from database
def fetch_all_taxi_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM taxi_data ORDER BY date DESC")
    data = cursor.fetchall()
    
    conn.close()
    return data

