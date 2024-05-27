import PySimpleGUI as sg
from random import randint
from respostas import resposta_formatada
# def atendimento(nome, msg):
#     layout = [
#         [sg.Text(f'Nome cliente -> {nome}')],
#         [sg.Text(f'Mensagem do cliente -> {msg}')],
#         [sg.InputText(key='resposta')],
#         [sg.Button('Enviar')],
#     ]
#     c = randint(0,100)
#     janela = sg.Window(f'Mensagem Whatsap {c}', layout=layout)
#     evento, valores = janela.read()
#     if evento == sg.WIN_CLOSED:
#         resposta = 'finalizado'
#     if evento == 'Enviar':
#         resposta = valores['resposta']
#
#     return resposta

def atendimento(nome, msg):
    print(f'Nome do cliente -> {nome}')
    print(f'Mensagem do cliente -> {msg}')
    resposta = input(f'Resposta -> ')
    return str(resposta)
