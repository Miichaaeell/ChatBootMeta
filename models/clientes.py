from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_login import UserMixin
from os import getenv
import smtplib
import email.message
DB = getenv("DB_URL")
db = create_engine(DB)
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()
# criar a tabela
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(42))
    email = Column('email', String(42))
    telefone = Column('telefone', String(20), unique=True)
    fluxo = Column('fluxo', String(42))
    def __init__(self, nome = '', email = '',telefone = '', fluxo = 'inicial'):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.fluxo = fluxo



class Funcionario(Base, UserMixin):
    __tablename__ = 'funcionarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(42))
    email = Column('email', String(42))
    usuario = Column('usuario', String(42), unique=True)
    senha = Column('senha', String(42))
    previlegio = Column('previlegio', String(42))
    def __init__(self, nome, email, usuario, senha, previlegio):
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.previlegio = previlegio

class Mensagens(Base):
    __tablename__ = 'mensagens'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    mensagem = Column('mensagem', String)
    cliente = Column('cliente', ForeignKey("clientes.id"))
    def __init__(self, mensagem, cliente):
        self.mensagem = mensagem
        self.cliente = cliente

Base.metadata.create_all(bind=db)


def atualizar_fluxo(telefone, fluxo):
    cliente = session.query(Cliente).filter_by(telefone = telefone).first()
    cliente.fluxo = fluxo
    session.add(cliente)
    session.commit()
    print(f'Fluxo atual: {cliente.fluxo}')

def enviar_email(nome, e_mail, msg):
    my_email = getenv('my_email')
    key_email = getenv('key_email')
    adress = [e_mail, my_email]
    corpo_email = f"""Olá {nome}, seu pedido de orçamento foi realizado com Sucesso!
    \nDetalhes da solicitação:\n--> {msg}\n\nAtt.\nMichael Dev
    """
    for endereco in adress:
        msg = email.message.Message()
        msg['Subject'] = 'Confirmação do pedido de orçamento - no reply'
        msg['From'] = f'{my_email}'
        msg['To'] = endereco
        password = f'{key_email}'
        msg.add_header('Content-Type', 'text')
        msg.set_payload(corpo_email)
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
        print(msg['To'])
        print('Email enviado com sucesso!')




