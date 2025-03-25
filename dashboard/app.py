from flask import Flask, request, jsonify
from flask_cors import CORS
import db_helper

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (useful for frontend later)

@app.route("/")
def home():
    return jsonify({"message": "Taxi Business Dashboard API is running!"})

@app.route("/add_log", methods=["POST"])
def add_log():
    data = request.json
    date = data.get("date")
    earnings = data.get("earnings")
    expenses = data.get("expenses")
    fuel_cost = data.get("fuel_cost")
    mileage = data.get("mileage")

    if not all([date, earnings, expenses, fuel_cost, mileage]):
        return jsonify({"error": "Missing required fields"}), 400

    result = db_helper.insert_taxi_log(date, earnings, expenses, fuel_cost, mileage)
    return jsonify(result)

@app.route("/get_logs", methods=["GET"])
def get_logs():
    logs = db_helper.get_all_logs()
    return jsonify({"data": logs})

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
    app.run(debug=True)
