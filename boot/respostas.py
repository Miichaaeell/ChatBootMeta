from models.clientes import session, Cliente, enviar_email
def boas_vindas(nome, novo):
    if novo == False:
        return (f'Olá {nome}, que bom te ver novamente por aqui, tudo bem? em que posso te ajudar hoje?'
                f'\n\n Orçamento \n Serviços')
    else:
        return (f'Olá {nome} tudo bem? em que posso te ajudar hoje?'
                f'\n\n Orçamento \n Serviços')


def orcamento(nome, email, telefone):
    cliente = session.query(Cliente).filter_by(telefone=telefone).first()
    cliente.email = email
    session.add(cliente)
    session.commit()
    return (f'{nome}, estamos quase lá, só mais algumas informações:'
            f'\n\nNome completo: \n\nTipo de projeto* (sistema ou automação):'
            f'\n\nDescreva com o máximo de detalhes possível o que deseja fazer:')


def cadastro_email(nome):
    return (f'{nome} Obrigado por nos escolher, por favor me informe um e-mail válido para contado.'
            f'Lembrando que esse e-mail que será utilizado para retornarmos o contato, então informe um e-mail'
            f'que é acompanhado diariamente.')


def servicos(nome=''):
    return(f'{nome} vou te apresentar alguns de meus seviços: \n\n Automação de tarefas repetitivas \n Criação de boot de atendimento'
        f'\n Criações de sistemas \n Sistemas ou automações para análise de dados '
        f'\n\n Se desejar realizar um orçamento, só me enviar "orçamento" que já daremos início')


def despedida(nome, telefone, msg):
    cliente = session.query(Cliente).filter_by(telefone=telefone).first()
    enviar_email(nome, cliente.email, msg)
    return (
        f'Perfeito! {nome} iremos analisar a sua solicitação e retornaremos o contato com seu orçamento no e-mail {cliente.email}'
        f' então fique de olho, se precisarmos de mais algum detalhe também entraremos em contato pelo e-mail.\n\nAtt, \nMichael Dev ')
def agradecimento(nome):
    return (f'{nome} agradecemos o contato.\nAté logo')
