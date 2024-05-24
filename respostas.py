from funcoesbd import cadastrar_email, consultar_email, enviar_email


def resposta_formatada(msg):
    data = {'messaging_product': 'whatsapp',
            'to': '5519999894514',
            'type': 'text',
            'text': {'body': f'{msg}'}}
    return data


def boas_vindas(nome='', validacao='false'):
    if 'verdadeiro' in validacao:
        return (f'Olá {nome}, que bom te ver novamente por aqui, tudo bem? em que posso te ajudar hoje?'
                f'\n\n Orçamento \n Serviços')
    else:
        return (f'Olá {nome} tudo bem? em que posso te ajudar hoje?'
                f'\n\n Orçamento \n Serviços')


def orcamento(nome, email, telefone):
    cadastrar_email(email, telefone)
    return (f'{nome}, estamos quase lá, só mais algumas informações:'
            f'\n\nTipo de projeto* (sistema ou automação)*: \n\nNome completo:'
            f'\n\nDescreva com o máximo de detalhes possivel o que deseja fazer:')


def orcamento1(nome):
    return (
        f'{nome} Obrigado por nos escolher, por favor me informe um e-mail para contado. '
        f'\nOBS: para que seja feito o cadastro corretamente insira o e-mail como no exemplo: \n"email: meuemail@email.com":')


def servicos(nome=''):
    return (
        f'{nome} vou te apresentar alguns de meus seviços: \n\n Automação de tarefas repetitivas \n Criação de boot de atendimento'
        f'\n Criações de sistemas \n Sistemas ou automações para análise de dados '
        f'\n\n Se desejar realizar um orçamento, só me enviar "orçamento" que já daremos início')


def despedida(nome, telefone, msg=''):
    email = consultar_email(telefone)
    enviar_email(nome, telefone, msg)
    return (
        f'Perfeito! {nome} iremos analisar a sua solicitação e retornaremos o contato com seu orçamento no e-mail {email}'
        f' então fique de olho, se precisarmos de mais algum detalhe também entraremos em contato pelo e-mail.\n\nAtt, \nMichael Dev ')
