from models.clientes import session, Cliente, atualizar_fluxo
from os import getenv
from boot.respostas import *
import requests
from atendimento.atendimento import atendimento
def filtrar_dados(dados):
    novo = False
    fluxo = ''
    cliente = {}
    cliente['nome'] = dados['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name']
    cliente['telefone'] = dados['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
    cliente['msg'] = dados['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    cliente['remetente'] = dados['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
    cliente['id'] = dados['entry'][0]['changes'][0]['value']['messages'][0]['id']
    clientes = session.query(Cliente).filter_by(telefone = cliente['telefone']).first()
    if not clientes:
        new_cliente = Cliente(nome=cliente['nome'], telefone=cliente['telefone'])
        session.add(new_cliente)
        session.commit()
        novo = True
        fluxo = 'inicial'
    else:
        fluxo = clientes.fluxo


    return cliente, novo, fluxo

def reply(usuario, novo, fluxo):
    print(f'Cliente: {usuario["nome"]} \nMensagem: {usuario["msg"]}')
    print(f'Fluxo anterior: {fluxo}')
    if fluxo == 'atendimento' or 'atendimento' in usuario["msg"] or 'atendente' in usuario["msg"]:
        atualizar_fluxo(usuario['telefone'],'atendimento')
        resposta = atendimento(usuario['nome'], usuario['msg'])
        if resposta.lower() == 'finalizado' or resposta == '':
            atualizar_fluxo(usuario['telefone'], 'inicial')
            return agradecimento(usuario['nome'])
        else:
            return resposta
    elif fluxo == 'inicial' and usuario["msg"] in 'bom dia boa tarde boa noite ola oi':
        return boas_vindas(usuario["nome"], novo)
    elif fluxo == 'inicial' and usuario['msg'] in 'serviços servico':
        atualizar_fluxo(usuario['telefone'], 'Informações')
        return servicos(usuario['nome'])
    elif fluxo == 'Informações' or usuario['msg'] in 'orçamento , orcamento':
        atualizar_fluxo(usuario['telefone'], 'Cadastro E-mail')
        return cadastro_email(usuario['nome'])
    elif fluxo == 'Cadastro E-mail':
        atualizar_fluxo(usuario['telefone'], 'Finalizando Orçamento')
        return orcamento(nome=usuario['nome'], email=usuario['msg'], telefone=usuario['telefone'])
    elif fluxo == 'Finalizando Orçamento':
        atualizar_fluxo(usuario['telefone'], 'inicial')
        return despedida(usuario['nome'], usuario['telefone'], usuario['msg'])
    else:
        return 'Desculpe, mas faltou alguma informação, poderia me enviar os dados novamente, lembrando que todas as informações são essências para nosso atendimento'

def enviar_resposta(msg, telefone):
    bearer = getenv('Bearer_TOKEN')
    data = {'messaging_product': 'whatsapp',
            'to': telefone,
            'type': 'text',
            'text': {'body': f'{msg}'}}
    r = requests.request(method='POST',
                         url='https://graph.facebook.com/v20.0/254050617801879/messages',
                         headers={'Authorization': f'Bearer {bearer}'},
                         json=data)
    print(r)
    return str(r)
