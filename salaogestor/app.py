from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# --- Database connection ---
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )


# --- Flask-Login setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"  # redirect to login if not authenticated

# --- User model for Flask-Login ---


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='employee')


@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, email, password_hash, role FROM users WHERE id = %s;", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return User(*user)
    return None

# --- Routes ---


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, email, password_hash, role FROM users WHERE email = %s;", (email,))
    user_data = cur.fetchone()
    cur.close()
    conn.close()

    if user_data and check_password_hash(user_data[2], senha):
        user = User(*user_data)
        login_user(user)
        flash(f"Bem-vindo, {user.email} ({user.role})!", "success")
        return redirect(url_for("dashboard"))
    else:
        flash("Email ou senha incorretos.", "error")
        return redirect(url_for("index"))


@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.role == "admin":
        return f"<h1>Área do Administrador</h1><p>Bem-vindo, {current_user.email}</p><a href='/logout'>Sair</a>"
    else:
        return f"<h1>Área do Funcionário</h1><p>Bem-vindo, {current_user.email}</p><a href='/logout'>Sair</a>"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "info")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        role = request.form.get("role", "employee")

        if not email or not senha:
            flash("Preencha todos os campos.")
            return redirect(url_for("register"))

        senha_hash = generate_password_hash(senha)
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users (email, password_hash, role) VALUES (%s, %s, %s);",
                (email, senha_hash, role)
            )
            conn.commit()
            flash("Cadastro realizado com sucesso!")
        except psycopg2.errors.UniqueViolation:
            flash("Este email já está cadastrado.")
        finally:
            cur.close()
            conn.close()

        return redirect(url_for("index"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
