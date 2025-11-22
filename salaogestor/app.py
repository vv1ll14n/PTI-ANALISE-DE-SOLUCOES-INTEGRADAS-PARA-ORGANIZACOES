from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from functools import wraps
from datetime import date, datetime, timedelta
import psycopg2
import os

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'admin':
            flash("Você não tem permissão para acessar esta página.", "error")
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

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
        return User(*user)  # ✅ RETORNA o objeto User
    return None

# --- Routes ---

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")
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
        return redirect(url_for("agenda_salao"))
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

# --- Rotas para Clientes ---

@app.route("/clientes")
@login_required
def listar_clientes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, email, telefone, endereco, data_cadastro FROM clientes ORDER BY nome;")
    clientes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes/novo", methods=["GET", "POST"])
@login_required
@admin_required
def novo_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")

        if not nome:
            flash("O nome do cliente é obrigatório.", "error")
            return redirect(url_for("novo_cliente"))

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO clientes (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s);",
                (nome, email, telefone, endereco)
            )
            conn.commit()
            flash("Cliente cadastrado com sucesso!", "success")
            return redirect(url_for("listar_clientes"))
        except psycopg2.errors.UniqueViolation:
            flash("Este email já está cadastrado para outro cliente.", "error")
        finally:
            cur.close()
            conn.close()

    return render_template("form_cliente.html", cliente=None) # Passa None para indicar que é um novo cliente

@app.route("/clientes/editar/<int:cliente_id>", methods=["GET", "POST"])
@login_required
@admin_required
def editar_cliente(cliente_id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")

        if not nome:
            flash("O nome do cliente é obrigatório.", "error")
            return redirect(url_for("editar_cliente", cliente_id=cliente_id))

        try:
            cur.execute(
                "UPDATE clientes SET nome = %s, email = %s, telefone = %s, endereco = %s WHERE id = %s;",
                (nome, email, telefone, endereco, cliente_id)
            )
            conn.commit()
            flash("Cliente atualizado com sucesso!", "success")
            return redirect(url_for("listar_clientes"))
        except psycopg2.errors.UniqueViolation:
            flash("Este email já está cadastrado para outro cliente.", "error")
        finally:
            cur.close()
            conn.close()
    else: # GET request
        cur.execute(
            "SELECT id, nome, email, telefone, endereco FROM clientes WHERE id = %s;", (cliente_id,)
        )
        cliente = cur.fetchone()
        cur.close()
        conn.close()

        if cliente is None:
            flash("Cliente não encontrado.", "error")
            return redirect(url_for("listar_clientes"))

        return render_template("form_cliente.html", cliente=cliente)

@app.route("/clientes/excluir/<int:cliente_id>", methods=["POST"])
@login_required
@admin_required
def excluir_cliente(cliente_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM clientes WHERE id = %s;", (cliente_id,))
        conn.commit()
        flash("Cliente excluído com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao excluir cliente: {e}", "error")
    finally:
        cur.close()
        conn.close()
    return redirect(url_for("listar_clientes"))

# --- Rotas para Agendamento ---

@app.route("/agenda-salao")
@login_required
def agenda_salao():
    conn = get_db_connection()
    cur = conn.cursor()

    # --- OFFSET DA SEMANA (0 = semana atual, 1 = próxima, -1 = anterior) ---
    try:
        offset = int(request.args.get("offset", 0))
    except ValueError:
        offset = 0

    hoje = date.today()
    # segunda-feira da semana atual
    inicio_semana_atual = hoje - timedelta(days=hoje.weekday())
    # aplica o offset em semanas
    inicio_semana = inicio_semana_atual + timedelta(weeks=offset)
    fim_semana = inicio_semana + timedelta(days=4)  # segunda a sexta

    # Buscar dados do profissional (nome, foto)
    cur.execute("""
        SELECT nome, foto_url
        FROM profissionais
        WHERE email = %s;
    """, (current_user.email,))
    profissional = cur.fetchone()  # (nome, foto_url) ou None

    # Buscar agendamentos para a semana escolhida
    if current_user.role == "admin":
        cur.execute("""
            SELECT a.id, c.nome AS cliente, a.servico, a.profissional,
                   a.data, a.hora, a.status
            FROM agendamentos a
            JOIN clientes c ON a.cliente_id = c.id
            WHERE a.data BETWEEN %s AND %s
            ORDER BY a.data, a.hora;
        """, (inicio_semana, fim_semana))
    else:
        cur.execute("""
            SELECT a.id, c.nome AS cliente, a.servico, a.profissional,
                   a.data, a.hora, a.status
            FROM agendamentos a
            JOIN clientes c ON a.cliente_id = c.id
            WHERE a.profissional = %s
              AND a.data BETWEEN %s AND %s
            ORDER BY a.data, a.hora;
        """, (current_user.email, inicio_semana, fim_semana))

    agendamentos = cur.fetchall()
    cur.close()
    conn.close()

         # --- contagens para a "Lista de espera" ---
    total_agendados = len(agendamentos)
    total_finalizados = sum(1 for ag in agendamentos if ag[6] == 'finalizado')

    # --- monta grid ---
    horarios = ["09:00","09:30","10:00","10:30","11:00","11:30",
                "14:00","14:30","15:00","15:30","16:00","16:30"]
    dias_semana = ["segunda","terça","quarta","quinta","sexta"]
    grid = {h: {dia: None for dia in dias_semana} for h in horarios}

    for ag in agendamentos:
        ag_data = ag[4]                     # data
        ag_hora = ag[5].strftime("%H:%M")   # hora -> "HH:MM"
        dow = ag_data.weekday()             # 0 = segunda

        if dow < 5 and ag_hora in grid:
            dia = dias_semana[dow]
            grid[ag_hora][dia] = {
                "cliente": ag[1],           # nome do cliente
                "servico": ag[2]            # serviço
            }
        
    # horários disponíveis = total de slots - ocupados
    total_slots = len(horarios) * len(dias_semana)
    total_ocupados = sum(
        1
        for h in horarios
        for d in dias_semana
        if grid[h][d] is not None
    )
    total_disponiveis = total_slots - total_ocupados

    # Texto do intervalo da semana para mostrar no topo
    semana_label = f"{inicio_semana.strftime('%d/%m/%Y')} a {fim_semana.strftime('%d/%m/%Y')}"

    return render_template(
        "agenda-salao.html",
        grid=grid,
        profissional=profissional,
        offset=offset,
        semana_label=semana_label,
        total_agendados=total_agendados,
        total_finalizados=total_finalizados,
        total_disponiveis=total_disponiveis,
    )

@app.route("/agendamentos/novo", methods=["GET", "POST"])
@login_required
def novo_agendamento():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        cliente_id = request.form.get("cliente_id")
        servico = request.form.get("servico")
        data = request.form.get("data")
        hora = request.form.get("hora")

        if not cliente_id or not servico or not data or not hora:
            flash("Preencha todos os campos do agendamento.", "error")
            return redirect(url_for("novo_agendamento"))

        try:
            cur.execute("""
                INSERT INTO agendamentos (cliente_id, servico, profissional, data, hora, status)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (cliente_id, servico, current_user.email, data, hora, 'pendente'))
            conn.commit()
            flash("Agendamento criado com sucesso!", "success")
            return redirect(url_for("agenda_salao"))
        except Exception as e:
            conn.rollback()
            flash(f"Erro ao criar agendamento: {e}", "error")
        finally:
            cur.close()
            conn.close()

        return redirect(url_for("agenda_salao"))

    # GET: mostrar formulário
    cur.execute("SELECT id, nome FROM clientes ORDER BY nome;")
    clientes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("novo_agendamento.html", clientes=clientes)

if __name__ == "__main__":
    app.run(debug=True)
