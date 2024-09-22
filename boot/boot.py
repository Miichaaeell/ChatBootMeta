from flask import Blueprint, request
from boot.gerencia import filtrar_dados, reply, enviar_resposta
from os import getenv

token = getenv('TOKEN')
boot = Blueprint('boot', __name__, template_folder='templates')

@boot.route('/webhook', methods=['GET', 'POST'])
def bot():
    if request.method == 'GET':
        key = request.args.get('hub.challenge')
        verify_token = request.args.get('hub.verify_token')
        if verify_token == token:
            return key
        else:
            return 'Token incorreto'
    else:
        msg = request.get_json()
        if 'contacts' in msg['entry'][0]['changes'][0]['value']:
            usuario = filtrar_dados(msg)
            res = reply(usuario[0], usuario[1], usuario[2])
            status = enviar_resposta(res, usuario[0]['telefone'])
            return str(f'{status}')
        else:
            res = request.json
            print(f'Status message: {res["entry"][0]["changes"][0]["value"]["statuses"][0]["status"]}')
            return str(f'Status message: {res["entry"][0]["changes"][0]["value"]["statuses"][0]["status"]}')
