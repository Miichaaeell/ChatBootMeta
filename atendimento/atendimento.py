from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, logout_user, login_required
from models.clientes import Funcionario, session



atendimento = Blueprint('atendimento', __name__, template_folder='templates')

@atendimento.route('/inicio', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('inicio.html')
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
        id = session.query(Funcionario).count() + 1
        new_user = Funcionario(id, nome, email, usuario, senha, previlegio)
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
def atendente(nome, msg):
    print(f'Nome do cliente -> {nome}')
    print(f'Mensagem do cliente -> {msg}')
    resposta = input(f'Resposta -> ')
    return str(resposta)


mensagens = [
    {'Numero1': 'xxxxx',
     'mensagem': 'xxxx1'},
    {'Numero2': 'xxxxx',
     'mensagem': 'xxxx2'},
    {'Numero3': 'xxxxx',
     'mensagem': 'xxxx3'}
]