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
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='employee')

    def __init__(self, id, email, password_hash, role):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.role = role


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
        User(*user)
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
        return redirect(url_for("agenda"))
    else:
        flash("Email ou senha incorretos.", "error")
        return redirect(url_for("index"))


@app.route("/agenda")
def agenda():
    return render_template("agenda-salao.html")


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

@app.route("/reset_simples", methods=["GET", "POST"])
def reset_simples():
    # chave de troca de senha
    CHAVE_MESTRA = "admin123" 

    if request.method == "POST":
        email = request.form.get("email")
        nova_senha = request.form.get("nova_senha")
        chave_digitada = request.form.get("chave_seguranca")

        # 1. Verifica se a chave de segurança está correta
        if chave_digitada != CHAVE_MESTRA:
            flash("Chave de segurança incorreta! Peça ao administrador.", "error")
            return redirect(url_for("reset_simples"))

        # 2. Verifica se preencheu tudo
        if not email or not nova_senha:
            flash("Preencha todos os campos.")
            return redirect(url_for("reset_simples"))

        # 3. Atualiza a senha no banco
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Primeiro verificamos se o email existe
        cur.execute("SELECT id FROM users WHERE email = %s;", (email,))
        if not cur.fetchone():
            flash("E-mail não encontrado.", "error")
            cur.close()
            conn.close()
            return redirect(url_for("reset_simples"))

        # Se existe, atualizamos
        senha_hash = generate_password_hash(nova_senha)
        cur.execute("UPDATE users SET password_hash = %s WHERE email = %s;", (senha_hash, email))
        conn.commit()
        cur.close()
        conn.close()

        flash("Senha alterada com sucesso! Faça login.", "success")
        return redirect(url_for("index"))

    return render_template("reset_simples.html")


if __name__ == "__main__":
    app.run(debug=True)
