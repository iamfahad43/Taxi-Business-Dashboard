# Taxi Business Dashboard

## 🚖 Overview
The Taxi Business Dashboard is a comprehensive tool designed for taxi drivers and fleet managers to track and analyze daily operations efficiently. It helps in monitoring earnings, expenses, fuel costs, and mileage while providing valuable insights to maximize profitability.

## 🛠 Tech Stack
- **Backend:** Python, Flask, SQL
- **Frontend:** Streamlit
- **Database:** SQLite/PostgreSQL
- **Data Visualization:** Power BI / Tableau

## ✨ Features
✅ Tracks daily earnings, expenses, fuel costs, and mileage  
✅ Provides insights into profitable routes & peak hours  
✅ Predicts monthly revenue & fuel efficiency trends  
✅ Generates automated reports & notifications  

## 📂 Project Structure
```
Taxi-Business-Dashboard/
│-- app/                     # Main application logic
│   │-- config/              # Configuration files
│   │-- dashboard/           # Streamlit/Flask dashboard
│   │   │-- __pycache__/     # Compiled Python files (ignored)
│   │   │-- templates/       # HTML templates (if applicable)
│   │   └-- app.py           # Main dashboard script
│   │-- db_helper.py         # Database helper functions
│-- data/                    # Stores raw and processed data
│-- db/                      # Database storage
│   └-- taxi_data.db         # SQLite database file
│-- reports/                 # Generated reports (PDF/Excel)
│-- scripts/                 # Utility and setup scripts
│   └-- db_setup.py          # Database setup script
│-- vnv/                     # Virtual environment (excluded from GitHub)
│-- config.py                # Configuration settings
│-- dashboard_ui.py          # UI for the dashboard
│-- main.py                  # Main entry point of the application
│-- README.md                # Project documentation
│-- requirements.txt         # Dependencies
```

## 🚀 Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/iamfahad43/Taxi-Business-Dashboard.git
   cd Taxi-Business-Dashboard
   ```
2. **Create and Activate Virtual Environment**
   ```sh
   python -m venv vnv
   source vnv/bin/activate  # Mac/Linux
   vnv\Scripts\activate  # Windows
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Dashboard**
   ```sh
   streamlit run dashboard/app.py
   ```

5. **Run the Dashboard Alternative**
   ```sh
   python dashboard/app.py (in one terminal) and  streamlit run dashboard_ui.py (in second terminal)
   ```


## 📊 Usage
- Enter daily earnings, fuel costs, and mileage in the interface
- View real-time insights on revenue, peak hours, and fuel efficiency
- Generate automated reports for performance tracking

## 🔧 Future Enhancements
- Implement machine learning models for trend predictions
- Add user authentication for multiple drivers
- Expand analytics with more visualizations

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!

## 📜 License
This project is licensed under the MIT License.