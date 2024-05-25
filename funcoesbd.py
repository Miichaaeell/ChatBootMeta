import mysql.connector
import os
import smtplib
import email.message

key_email = os.getenv("EMAIL_KEY")
my_email = os.getenv("MY_EMAIL")
key_bd = os.getenv("BD_KEY")


def cadastro(nome, telefone):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
    )
    cursor = conexao.cursor()
    seleciona = f'SELECT Telefone, Nome FROM clientes'
    cursor.execute(seleciona)
    dados = cursor.fetchall()
    cadastrado = False
    for numero, usuario in dados:
        if int(numero) == int(telefone):
            cadastrado = True
    if cadastrado == False:
        nome = nome.split()
        cadastrando = f'INSERT INTO `railway`.`clientes` (`Nome`, `Telefone`) VALUES ("{nome[0]}", "{telefone}")'
        cursor.execute(cadastrando)
        conexao.commit()
        return str('falso')
    else:
        return str('verdadeiro')
    cursor.close()
    conexao.close()


def cadastrar_email(email, telefone):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
    )

    cursor = conexao.cursor()
    comando = f"UPDATE `railway`.`clientes` SET `Email` = '{email[6:].strip()}' WHERE (`Telefone` = '{telefone}')"
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    cursor.close()


def consultar_email(telefone):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
    )
    cursor = conexao.cursor()
    comando = f'SELECT Email FROM clientes WHERE Telefone = {telefone}'
    cursor.execute(comando)
    contato = cursor.fetchall()
    return str(contato[0][0])
    cursor.close()
    conexao.close()


def enviar_email(nome='', telefone='', msg=''):
    adress = [consultar_email(telefone), my_email]
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
def consultar_atendimento(telefone):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
    )
    cursor = conexao.cursor()
    comando = f'SELECT Atendimento FROM clientes WHERE Telefone = {telefone}'
    cursor.execute(comando)
    atendente = cursor.fetchall()
    return atendente[0][0]
    cursor.close()
    conexao.close()
def atualizar_atendimento(telefone, atualizar):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
    )
    cursor = conexao.cursor()
    comando = f'UPDATE clientes SET Atendimento = "{atualizar}" WHERE Telefone = {telefone}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

