import requests
import json
from flask import Flask, request
from os import getenv
from gerencia import filtrar_dados, cadastrar_usuario, reply, enviar_resposta
from respostas import resposta_formatada
token = getenv('TOKEN')
Bearer_TOKEN = getenv('Bearer_TOKEN')
app = Flask(__name__)
@app.route('/')
def home():
    return f'Hello World \nWebhook Online'
@app.get('/webhook')
def verify_key():
    key = request.args.get('hub.challenge')
    verify_token = request.args.get('hub.verify_token')
    if verify_token == token:
        return key
    else:
        print('Token incorreto')
@app.post('/webhook')
def bot():
    msg = request.get_json()
    if 'contacts' in msg['entry'][0]['changes'][0]['value']:
        msg_usuario = filtrar_dados(msg)
        verificar_cadastro = cadastrar_usuario(msg_usuario)
        res = reply(verificar_cadastro[0], verificar_cadastro[1], verificar_cadastro[2])
        status = enviar_resposta(res)
        return str(f'{status}')
    else:
        return ('Notificação')


if __name__ == '__main__':
    app.run(debug=True)

