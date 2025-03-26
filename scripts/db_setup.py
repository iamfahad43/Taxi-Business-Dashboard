import sqlite3

# Create database and tables
def create_database():
    conn = sqlite3.connect("db/taxi_data.db")
    cursor = conn.cursor()

    # Table for daily earnings, expenses, fuel, and mileage
    cursor.execute('''CREATE TABLE IF NOT EXISTS taxi_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        earnings REAL NOT NULL,
                        expenses REAL NOT NULL,
                        fuel_cost REAL NOT NULL,
                        mileage REAL NOT NULL
                     )''')

    conn.commit()
    conn.close()
    print("Database and table created successfully.")


# Seting up a function that takes user input from the UI
def setup_database():
    conn = sqlite3.connect("db/taxi_data.db")
    cursor = conn.cursor()

    # Create a table for user-entered taxi data if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS taxi_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        earnings REAL NOT NULL,
        fuel_expense REAL NOT NULL,
        other_expense REAL NOT NULL,
        distance_km REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup completed.")
