AI Financial Advisor – SpendSmart AI

An intelligent, data-driven financial assistant that helps users track expenses, analyze spending behavior, and make smarter financial decisions through actionable insights and visualizations.

Overview
Managing personal finances can be overwhelming without clear insights. This project aims to simplify financial tracking by providing clear visualization of spending patterns, intelligent suggestions to improve savings, and data-driven insights for better decision-making.

Key Features

Expense Tracking
Upload or input expense data (CSV/manual). Structured data handling ensures accuracy.
Spending Analysis
Category-wise expense breakdown. Monthly and daily trend analysis.
Smart Insights
Detects overspending patterns and suggests areas to reduce expenses.
Expense Prediction
Estimates future spending based on historical trends.
Interactive Visualizations
Provides graphs and charts for intuitive understanding.

Tech Stack

Frontend: Streamlit
Backend: Python
Data Processing: Pandas, NumPy
Visualization: Matplotlib / Seaborn
Version Control: Git, GitHub

Project Structure

ai-financial-advisor/
app.py – Main application handling UI and logic
auth.py – User authentication (login/signup/session handling)
requirements.txt – Project dependencies
README.md – Project documentation

How It Works

User uploads or inputs expense data
Data is cleaned and processed using Pandas
Spending patterns are analyzed
Insights and recommendations are generated
Results are displayed using visual dashboards

Sample Dataset

Date: 2026-03-01, Category: Food, Amount: 250
Date: 2026-03-02, Category: Transport, Amount: 100
Date: 2026-03-03, Category: Shopping, Amount: 500

Installation & Setup

Clone the repository using git clone https://github.com/your-username/ai-financial-advisor.git
Navigate to the project folder
Install dependencies using pip install -r requirements.txt
Run the application using streamlit run app.py

Example Use Case

A student uploads monthly expense data. The system analyzes spending behavior, identifies the highest spending category, shows trends over time, and suggests ways to reduce unnecessary expenses.

Future Enhancements

Advanced machine learning-based predictions
Smart alerts for unusual spending
Mobile-friendly UI
Cloud deployment
User authentication with personalized dashboards

Limitations

Works only with structured input data
Prediction model is basic and not highly accurate
No real-time bank integration
