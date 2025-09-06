from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from flask_login import (
    LoginManager, UserMixin, login_user, logout_user,
    login_required, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# -------------------------------
# Updated DB path
DB_NAME = "database.db"  # moved outside venv, same folder as app.py
# -------------------------------

# --- DB Helpers ---
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

# --- User model ---
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    conn.close()
    if user:
        return User(user["id"], user["username"], user["password"])
    return None

# --- Routes ---
@app.route('/')
def home_redirect():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/dashboard')
@login_required
def index():
    conn = get_db_connection()
    expenses = conn.execute(
        "SELECT * FROM expenses WHERE user_id=? ORDER BY date DESC", (current_user.id,)
    ).fetchall()

    total = sum([exp["amount"] for exp in expenses]) if expenses else 0

    rows = conn.execute(
        """
        SELECT strftime('%Y-%m', date) AS month, category, SUM(amount) AS total
        FROM expenses
        WHERE user_id=?
        GROUP BY month, category
        ORDER BY month DESC
        """,
        (current_user.id,)
    ).fetchall()

    conn.close()

    monthly_expenses = {}
    for r in rows:
        m, cat, tot = r["month"], r["category"], r["total"]
        if m not in monthly_expenses:
            monthly_expenses[m] = {"labels": [], "values": [], "total": 0}
        monthly_expenses[m]["labels"].append(cat)
        monthly_expenses[m]["values"].append(tot)
        monthly_expenses[m]["total"] += tot

    return render_template(
        'index.html',
        expenses=expenses,
        total=total,
        monthly_expenses=monthly_expenses
    )

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO expenses (amount, category, description, date, user_id) VALUES (?, ?, ?, ?, ?)",
            (amount, category, description, date, current_user.id)
        )
        conn.commit()
        conn.close()
        flash("Expense added ✅", "success")
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/delete/<int:id>')
@login_required
def delete_expense(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id=? AND user_id=?", (id, current_user.id))
    conn.commit()
    conn.close()
    flash("Expense deleted ❌", "info")
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        if not username or not password:
            flash("Username and password are required!", "danger")
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            flash("Registration successful ✅ Please log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("⚠️ Username already taken.", "danger")
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user["password"], password):
            login_user(User(user["id"], user["username"], user["password"]))
            flash("Login successful 🎉", "success")
            return redirect(url_for('index'))
        else:
            flash("❌ Invalid credentials", "danger")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out ✅", "info")
    return redirect(url_for('login'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
