💰 Expense Tracker
An Expense Tracker Web App built with Flask (Python), SQLite, HTML, CSS, and Chart.js. This app helps users track their daily expenses, categorize them, and visualize spending with interactive charts. It also includes a user authentication system for secure login and registration.

✨ Features
🔑 User Authentication

Register and login securely with password hashing
Each user manages their own expenses
📝 Expense Management

Add new expenses with amount, category, description, and date
Delete expenses easily
📊 Data Visualization

Interactive monthly pie charts showing expenses by category
Grand total and monthly totals
🏠 UI/UX

Simple and clean design
Responsive layout with Chart.js integration
🚀 Tech Stack
Backend: Python, Flask
Database: SQLite3
Frontend: HTML5, CSS3, Chart.js
Authentication: Flask-Login, Werkzeug (password hashing)
📂 Project Structure
expense_tracker/
│── app.py              # Main Flask app
│── requirements.txt    # Project dependencies
│── database.db         # SQLite database (auto-created)
│── static/
│   └── style.css       # Custom styles
│── templates/
│   ├── welcome.html    # Landing page
│   ├── login.html      # Login page
│   ├── register.html   # Registration page
│   ├── index.html      # Dashboard with expenses + charts
│   └── add_expense.html # Form to add expense
└── README.md
⚡ Installation & Setup
Clone this repository:

cd expense_tracker
Create & activate virtual environment:

python -m venv venv
venv\Scripts\activate   # (Windows)
source venv/bin/activate # (Mac/Linux)
Install dependencies:

pip install -r requirements.txt
Run the app:

python app.py
Open in browser:

http://127.0.0.1:5000
📌 Future Improvements
Export expenses to Excel/CSV
Add income tracking
Budget alerts (overspending warnings)
Dark mode UI
