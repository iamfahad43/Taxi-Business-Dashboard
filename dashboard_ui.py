import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Set Wide Layout
st.set_page_config(page_title="Taxi Dashboard", layout="wide")

# API Base URL
API_URL = "http://127.0.0.1:5000"

st.title("🚖 Taxi Business Dashboard")

# --- Fetch Data ---
def fetch_data(endpoint):
    try:
        response = requests.get(f"{API_URL}{endpoint}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f"❌ API Error: {e}")
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

# --- Earnings & Expenses ---
st.subheader("📊 Earnings & Expenses Overview")
logs_data = fetch_data("/get_logs")

if logs_data and logs_data.get("data"):
    df = pd.DataFrame(logs_data["data"], columns=["ID", "Date", "Earnings (€)", "Expenses (€)", "Fuel Cost (€)", "Mileage (km)"])
    df.drop(columns=["ID"], inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])

    # Line Chart: Earnings vs Expenses
    fig1 = px.line(df, x="Date", y=["Earnings (€)", "Expenses (€)"], markers=True, title="📈 Earnings vs Expenses Trend")
    st.plotly_chart(fig1, use_container_width=True)

    # Bar Chart: Profit Breakdown
    df["Profit (€)"] = df["Earnings (€)"] - df["Expenses (€)"]
    fig2 = px.bar(df, x="Date", y="Profit (€)", color="Profit (€)", text="Profit (€)", title="💰 Profit Breakdown")
    st.plotly_chart(fig2, use_container_width=True)

    # Show Data Table
    st.subheader("📜 Data Logs")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("⚠️ No data found. Please check API or database.")

logs_data = fetch_data("/get_logs")
st.write("Raw API Response:", logs_data)  # Debugging output

if logs_data and logs_data.get("data"):
    df = pd.DataFrame(logs_data["data"])
    st.write("Processed DataFrame:", df)  # Debugging output


# Refresh Button
if st.button("🔄 Refresh Data"):
    st.rerun()
