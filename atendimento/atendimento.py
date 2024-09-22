def atendimento(nome, msg):
    print(f'Nome do cliente -> {nome}')
    print(f'Mensagem do cliente -> {msg}')
    resposta = input(f'Resposta -> ')
    return str(resposta)
