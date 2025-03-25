# Streamlit web dashboard

import streamlit as st
import requests
import pandas as pd

# API Base URL
API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Taxi Business Dashboard", layout="wide")

# --- Title ---
st.title("🚖 Taxi Business Dashboard")

# --- Fetch Data from API ---
def fetch_data(endpoint):
    response = requests.get(f"{API_URL}{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# --- Metrics Section ---
col1, col2, col3 = st.columns(3)

# Get total earnings & expenses
total_data = fetch_data("/analytics/total")
if total_data:
    with col1:
        st.metric("💰 Total Earnings", f"€{total_data['total_earnings']}")
    with col2:
        st.metric("💸 Total Expenses", f"€{total_data['total_expenses']}")
    with col3:
        profit = total_data['total_earnings'] - total_data['total_expenses']
        st.metric("📈 Net Profit", f"€{profit}")

# Get average mileage
mileage_data = fetch_data("/analytics/mileage")
if mileage_data:
    st.metric("⛽ Average Mileage Efficiency", f"{mileage_data['avg_mileage']} km per unit fuel")

# Get best & worst days
days_data = fetch_data("/analytics/best_worst")
if days_data:
    st.subheader("📅 Best & Worst Earning Days")
    col4, col5 = st.columns(2)
    if days_data['best_day']:
        with col4:
            st.success(f"🔥 Best Day: {days_data['best_day']['date']} (€{days_data['best_day']['earnings']})")
    if days_data['worst_day']:
        with col5:
            st.error(f"😢 Worst Day: {days_data['worst_day']['date']} (€{days_data['worst_day']['earnings']})")

# --- Daily Logs Table ---
st.subheader("📊 Daily Earnings & Expenses Log")
logs_data = fetch_data("/get_logs")
if logs_data and logs_data['data']:
    df = pd.DataFrame(logs_data['data'], columns=["ID", "Date", "Earnings (€)", "Expenses (€)", "Fuel Cost (€)", "Mileage (km)"])
    df.drop(columns=["ID"], inplace=True)  # Remove ID column
    st.dataframe(df, use_container_width=True)

# --- Refresh Button ---
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()
