from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuarios' 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    perfil = db.Column(db.String(50), nullable=False) 
    agendamentos = db.relationship('Agendamento', back_populates='profissional')

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=False)
    agendamentos = db.relationship('Agendamento', back_populates='cliente')

class Servico(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    duracao_estimada_minutos = db.Column(db.Integer, nullable=False)

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer, primary_key=True)

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'), nullable=False)

    data_hora_inicio = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), default='agendado')

    cliente = db.relationship('Cliente', back_populates='agendamentos')
    profissional = db.relationship('Usuario', back_populates='agendamentos')
    servico = db.relationship('Servico')