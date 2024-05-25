import requests
import json
from flask import Flask, request
import os
from gerencia import filtar_dados, cadastrar_usuario, reply
from respostas import resposta_formatada

token = os.getenv('TOKEN')
Bearer_TOKEN = os.getenv('Bearer_TOKEN')
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
        msg_usuario = filtar_dados(msg)
        verificar_cadastro = cadastrar_usuario(msg_usuario)
        res = reply(verificar_cadastro[0], verificar_cadastro[1])
        print(res)
        url = f'https://graph.facebook.com/v19.0/254050617801879/messages'
        data = resposta_formatada(res)
        json.dumps(data)
        r = requests.request(method='POST',
                             url=url,
                             headers={'Authorization': f'Bearer {Bearer_TOKEN}'},
                             json=data)
        return str(f'{r}')
    else:
        return 'Notificações'


if __name__ == '__main__':
    app.run(debug=True)
