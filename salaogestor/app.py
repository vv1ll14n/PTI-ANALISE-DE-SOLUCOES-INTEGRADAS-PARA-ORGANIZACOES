from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import os

app = Flask(__name__)
app.secret_key = "secret_key_change_me"  # for flash messages

# --- PostgreSQL Connection Settings ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "salaogestor")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# --- Routes ---


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    if not email or not senha:
        flash("Por favor, preencha todos os campos.")
        return redirect(url_for("index"))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE email = %s AND password = %s;", (email, senha))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        flash("Login realizado com sucesso!")
        return "Bem-vindo ao sistema, " + email
    else:
        flash("Email ou senha incorretos.")
        return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        if not email or not senha:
            flash("Preencha todos os campos.")
            return redirect(url_for("register"))

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s);", (email, senha))
        conn.commit()
        cur.close()
        conn.close()
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for("index"))

    return "<h1>Cadastro em construção</h1>"


if __name__ == "__main__":
    app.run(debug=True)
