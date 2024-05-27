from funcoesbd import cadastrar_email, consultar_email, enviar_email

def resposta_formatada(msg, telefone):
    data = {'messaging_product': 'whatsapp',
            'to': telefone,
            'type': 'text',
            'text': {'body': f'{msg}'}}
    return data


def boas_vindas(nome, validacao, telefone):
    if 'verdadeiro' in validacao:
        return resposta_formatada(f'Olá {nome}, que bom te ver novamente por aqui, tudo bem? em que posso te ajudar hoje?'
                f'\n\n Orçamento \n Serviços', telefone)
    else:
        return resposta_formatada(f'Olá {nome} tudo bem? em que posso te ajudar hoje?'
                f'\n\n Orçamento \n Serviços', telefone)


def orcamento(nome, email, telefone):
    cadastrar_email(email, telefone)
    return resposta_formatada(f'{nome}, estamos quase lá, só mais algumas informações:'
            f'\n\nNome completo: \n\nTipo de projeto* (sistema ou automação):'
            f'\n\nDescreva com o máximo de detalhes possível o que deseja fazer:', telefone)


def cadastro_email(nome, telefone):
    return resposta_formatada(
        f'{nome} Obrigado por nos escolher, por favor me informe um e-mail válido para contado.', telefone)


def servicos(nome='', telefone=''):
    return resposta_formatada(
        f'{nome} vou te apresentar alguns de meus seviços: \n\n Automação de tarefas repetitivas \n Criação de boot de atendimento'
        f'\n Criações de sistemas \n Sistemas ou automações para análise de dados '
        f'\n\n Se desejar realizar um orçamento, só me enviar "orçamento" que já daremos início', telefone)


def despedida(nome, telefone, msg=''):
    email = consultar_email(telefone)
    enviar_email(nome, telefone, msg)
    return resposta_formatada(
        f'Perfeito! {nome} iremos analisar a sua solicitação e retornaremos o contato com seu orçamento no e-mail {email}'
        f' então fique de olho, se precisarmos de mais algum detalhe também entraremos em contato pelo e-mail.\n\nAtt, \nMichael Dev ', telefone)
def agradecimento(nome, telefone):
    return resposta_formatada(f'{nome} agradecemos o contato.\nAté logo', telefone)