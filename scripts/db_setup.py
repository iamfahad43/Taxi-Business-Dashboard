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

if __name__ == "__main__":
    create_database()
