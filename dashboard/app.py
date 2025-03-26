from flask import Flask, request, jsonify
from flask_cors import CORS
import db_helper
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (useful for frontend later)

# Move up one directory level from the current script's location
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Construct the correct path to the database
DB_PATH = os.path.join(BASE_DIR, "db", "taxi_data.db")


@app.route("/")
def home():
    return jsonify({"message": "Taxi Business Dashboard API is running!"})

@app.route("/get_logs", methods=["GET"])
def get_logs():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM taxi_logs ORDER BY date DESC")
    logs = cursor.fetchall()
    
    conn.close()
    
    if logs:
        return jsonify({"data": [dict(row) for row in logs]})
    return jsonify({"data": []})


@app.route("/analytics/total", methods=["GET"])
def total_earnings():
    result = db_helper.get_total_earnings()
    return jsonify(result)

@app.route("/analytics/mileage", methods=["GET"])
def avg_mileage():
    result = db_helper.get_avg_mileage()
    return jsonify(result)

@app.route("/analytics/best_worst", methods=["GET"])
def best_worst_days():
    result = db_helper.get_best_worst_days()
    return jsonify(result)






if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
