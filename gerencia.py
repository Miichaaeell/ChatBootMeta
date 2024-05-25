import respostas
from funcoesbd import cadastro, consultar_atendimento, atualizar_atendimento
from atendimento import atendimento
class clientes:
    def __init__(self, nome, telefone, msg):
        self.nome = nome
        self.telefone = telefone
        self.msg = msg
def filtar_dados(dados):
    response = {}
    response['nome'] = dados['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name']
    response['telefone'] = dados['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
    response['msg'] = dados['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    response['remetente'] = dados['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
    response['id'] = dados['entry'][0]['changes'][0]['value']['messages'][0]['id']
    return response

def cadastrar_usuario(dados):
    cliente = clientes(dados['nome'], dados['telefone'], dados['msg'].lower())
    cadastrado = cadastro(cliente.nome, cliente.telefone)
    atendente = consultar_atendimento(cliente.telefone)
    return cliente, cadastrado, atendente


def reply(usuario, validacao, atendente):
    if atendente == 'sim' or 'atendimento' in usuario.msg or 'atendente' in usuario.msg:
        atualizar_atendimento(usuario.telefone,'sim')
        resposta = atendimento(usuario.nome, usuario.msg)
        if resposta == 'finalizado':
            atualizar_atendimento(usuario.telefone, 'nao')
            return respostas.agradecimento(usuario.nome)
        else:
            return resposta
    elif usuario.msg in 'bom dia boa tarde boa noite ola oi':
        return respostas.boas_vindas(usuario.nome, validacao)
    elif usuario.msg in 'orçamento , orcamento':
        return respostas.orcamento1(usuario.nome)
    elif 'email:' in usuario.msg:
        return respostas.orcamento(usuario.nome, usuario.msg, usuario.telefone)
    elif usuario.msg in 'serviços servico':
        return respostas.servicos(usuario.nome)
    elif 'automação' in usuario.msg or 'automacao' in usuario.msg or 'sistema' in usuario.msg:
        return respostas.despedida(usuario.nome, usuario.telefone, usuario.msg)
    else:
        return 'Desculpe, mas faltou alguma informação, poderia me enviar os dados novamente, lembrando que todas as informações são essências para nosso atendimento'