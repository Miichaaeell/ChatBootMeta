from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.clientes import Funcionario, session


atendimento = Blueprint('atendimento', __name__, template_folder='templates')

@atendimento.route('/inicio', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('inicio.html', mensagem=mensagens)

@atendimento.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')
        user = session.query(Funcionario).filter_by(usuario=username).first()
        if user:
            if user.senha == senha:
                login_user(user)
                flash('Logado com Sucesso!')
                return redirect('inicio')
            else:
                return render_template('login.html', erro='Senha incorreta')
        else:
            return render_template('login.html', erro='Usuário incorreto')
    else:
        return render_template('login.html')

@atendimento.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        usuario = request.form.get('username')
        senha = request.form.get('senha')
        previlegio = request.form.get('previlegio')
        new_user = Funcionario(nome, email, usuario, senha, previlegio)
        session.add(new_user)
        session.commit()
        return redirect('inicio')

    else:
        return render_template('cadastro.html')
@atendimento.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('login')
@atendimento.route('/painel')
@login_required
def painel():
    return render_template('painel.html')



@atendimento.route('/listar_usuarios', methods=['GET', 'POST'])
@login_required
def listar_usuarios():
    if request.method == 'POST':
        id = request.form.get('id')
        nome = request.form.get('nome')
        email = request.form.get('email')
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        previlegio = request.form.get('previlegio')
        user = session.query(Funcionario).filter_by(id=id).first()
        user.nome = nome
        user.email = email
        user.usuario = usuario
        user.senha = senha
        user.previlegio = previlegio
        session.add(user)
        session.commit()
    usuarios = session.query(Funcionario).all()
    return render_template('listar_usuarios.html', usuarios=usuarios)


@atendimento.route('/editar/<user>')
@login_required
def editar(user):
    usuario = session.query(Funcionario).filter_by(usuario=user).first()
    return render_template('editar_usuario.html', usuario=usuario)

@atendimento.route('/excluir/<user>')
@login_required
def excluir(user):
    return f'excluir {user}'

@atendimento.route('/alterar_senha', methods=['GET', 'POST'])
@login_required
def alterarsenha():
    if request.method == 'GET':
        return render_template('alterar_senha.html')
    else:
        senha = request.form.get('senha')
        user = session.query(Funcionario).filter_by(id=current_user.id).first()
        user.senha = senha
        session.add(user)
        session.commit()
        logout_user()
        return redirect('login')
@atendimento.route('/detalhes/<user>')
@login_required
def detalhes_usuario(user):
    usuario = session.query(Funcionario).filter_by(usuario=user).first()
    return render_template('detalhes_usuario.html', usuario=usuario)
def atendente(nome, msg):
    print(f'Nome do cliente -> {nome}')
    print(f'Mensagem do cliente -> {msg}')
    resposta = input(f'Resposta -> ')
    return str(resposta)


mensagens = [
    {'nome': 'Morelo',
     'mensagem': ['Perdeu Evandro']},
    {'nome': 'Evandro',
     'mensagem': ['Vem me pegar', 'arruma nada']},
    {'nome': 'Andreia',
     'mensagem': ['Invade!! vai logo porra vai vai vai', 'ele esta fugindo, corre!!', 'la em cima pega ele']}
]