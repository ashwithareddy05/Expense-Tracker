# 💰 Expense Tracker

An **Expense Tracker Web App** built with **Flask (Python), SQLite, HTML, CSS, and Chart.js**.
This app helps users track their daily expenses, categorize them, and visualize spending with interactive charts.
It also includes a **user authentication system** for secure login and registration.

---

## ✨ Features

### 🔑 User Authentication

* Secure registration & login with password hashing
* Each user manages their own expenses

### 📝 Expense Management

* Add new expenses with amount, category, description, and date
* Delete expenses easily

### 📊 Data Visualization

* Interactive monthly **pie charts** showing expenses by category
* Grand total and monthly totals

### 🏠 UI/UX

* Simple and clean design
* Responsive layout with Chart.js integration

---

## 🚀 Tech Stack

* **Backend**: Python, Flask
* **Database**: SQLite3
* **Frontend**: HTML5, CSS3, Chart.js
* **Authentication**: Flask-Login, Werkzeug (password hashing)

---

## 📂 Project Structure

```
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
```

---

## ⚡ Installation & Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/expense_tracker.git
   cd expense_tracker
   ```

2. **Create & activate virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

5. **Open in browser**

   ```
   http://127.0.0.1:5000
   ```

---

## 📌 Future Improvements

* Export expenses to Excel/CSV
* Add income tracking
* Budget alerts (overspending warnings)
* Dark mode UI

---

💡 *Feel free to fork this repo, improve the project, and submit pull requests!* 🚀

