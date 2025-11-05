from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False) 
    telefone = db.Column(db.String(20), nullable=True) 
    ativo = db.Column(db.Boolean, default=True, nullable=False) 
    perfil = db.Column(
        db.Enum('admin', 'recepcionista', 'profissional', name='user_profile'), 
        nullable=False
    )
    
    agendamentos_como_profissional = db.relationship('Agendamento', back_populates='profissional')

class Cliente(db.Model):

    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=True) 
    data_nascimento = db.Column(db.Date, nullable=True) 
    data_cadastro = db.Column(db.DateTime(timezone=True), server_default=func.now()) 
    agendamentos = db.relationship('Agendamento', back_populates='cliente')
    vendas_produtos = db.relationship('VendaProduto', back_populates='cliente') 


class Servico(db.Model):
    __tablename__ = 'servicos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True) 
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    duracao_estimada_minutos = db.Column(db.Integer, nullable=False)
    agendamentos = db.relationship('Agendamento', back_populates='servico') 

class Produto(db.Model):
    __tablename__ = 'produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco_venda = db.Column(db.Numeric(10, 2), nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)
    codigo_barras = db.Column(db.String(100), unique=True, nullable=True)
    vendas = db.relationship('VendaProduto', back_populates='produto')

class Agendamento(db.Model):
 
    __tablename__ = 'agendamentos'
    
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'), nullable=False)
    data_hora_inicio = db.Column(db.DateTime(timezone=True), nullable=False)
    data_hora_fim = db.Column(db.DateTime(timezone=True), nullable=False) 
    
    status = db.Column(
        db.Enum('agendado', 'concluido', 'cancelado', 'nao_compareceu', name='agendamento_status'),
        nullable=False,
        default='agendado'
    )
    
    valor_cobrado = db.Column(db.Numeric(10, 2), nullable=True) 
    
    status_pagamento = db.Column(
        db.Enum('pendente', 'pago', name='pagamento_status'),
        nullable=False,
        default='pendente'
    )
    metodo_pagamento = db.Column(db.String(50), nullable=True)
    observacoes = db.Column(db.Text, nullable=True)
    cliente = db.relationship('Cliente', back_populates='agendamentos')
    profissional = db.relationship('Usuario', back_populates='agendamentos_como_profissional')
    servico = db.relationship('Servico', back_populates='agendamentos')
    vendas_associadas = db.relationship('VendaProduto', back_populates='agendamento')

class VendaProduto(db.Model):
    __tablename__ = 'vendas_produtos'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    agendamento_id = db.Column(db.Integer, db.ForeignKey('agendamentos.id'), nullable=True) 

    quantidade = db.Column(db.Integer, nullable=False, default=1)
    valor_total_pago = db.Column(db.Numeric(10, 2), nullable=False)
    data_venda = db.Column(db.DateTime(timezone=True), server_default=func.now())
    

    produto = db.relationship('Produto', back_populates='vendas')
    cliente = db.relationship('Cliente', back_populates='vendas_produtos')
    agendamento = db.relationship('Agendamento', back_populates='vendas_associadas')