import requests
from tkinter import *
from API import *

#Funções
#Pegando todas as cotações
def cotacoes():
    requisicao_api = requests.get(API)

    requisicao_dic = requisicao_api.json()

    dolar = requisicao_dic['USDBRL']['bid']
    euro = requisicao_dic['EURBRL']['bid']
    btc = requisicao_dic['BTCBRL']['bid']
    eth = requisicao_dic['ETHBRL']['bid']

    texto = f'''
    Dólar: R${dolar}
    Euro: R${euro}
    BTC: R${btc}
    ETH: R${eth}'''

    texto_resultado["text"] = texto

#Pegando cotação Dolar
def pegar_cotacao_dolar():
    requisicao_api = requests.get(API)

    requisicao_dic = requisicao_api.json()

    dolar = requisicao_dic['USDBRL']['bid']
    
    texto = f'''
    Dólar: R${dolar}'''

    texto_resultado["text"] = texto  

#Pegando cotação Euro
def pegar_cotacao_euro():
    
    requisicao_api = requests.get(API)

    requisicao_dic = requisicao_api.json()

    euro = requisicao_dic['EURBRL']['bid']
    
    texto = f'''
    Euro: R${euro}'''

    texto_resultado["text"] = texto 

#Pegando cotaAPI)
def pegar_cotacao_btc():
    
    requisicao_api = requests.get(API)
    
    requisicao_dic = requisicao_api.json()

    btc = requisicao_dic['BTCBRL']['bid']
    
    texto = f'''
    BTC: R${btc}'''

    texto_resultado["text"] = texto      
    
def pegar_cotacao_eth():
    
    requisicao_api = requests.get(API)
    
    requisicao_dic = requisicao_api.json()

    eth = requisicao_dic['ETHBRL']['bid']
    
    texto = f'''
    ETH: R${eth}'''

    texto_resultado["text"] = texto               
        
#Tkinter
#Cria a janela
janela = Tk()

#Titulo
janela.title("Cotação atual das Moedas")

#Textos
#Criando texto
texto_orientacao = Label(janela, text='Clique nos botões abaixo para ver a cotação atual das moedas')
texto_orientacao.grid(column=0, row=0, padx=15, pady=15)

#Resultado da busca
texto_resultado = Label(janela, text='Por favor,clique no botão para ver as cotações')
texto_resultado.grid(column=0, row=6, padx=15, pady=15)


#Botões
#Criando botão para todas as cotações
botao_todos = Button(janela, text='Ver todas as cotações', command=cotacoes)
botao_todos.grid(column=0, row=1, padx=15, pady=20)

#Criando botão para cotação do dolar
botao_todos = Button(janela, text='Ver a cotação do Dolar', command=pegar_cotacao_dolar)
botao_todos.grid(column=0, row=2, padx=15, pady=15)

#Criando botão para cotação do Euro
botao_todos = Button(janela, text='Ver a cotação do Euro', command=pegar_cotacao_euro)
botao_todos.grid(column=0, row=3, padx=15, pady=15)

#Criando botão para cotação do BTC
botao_todos = Button(janela, text='Ver a cotação do Bitcoin', command=pegar_cotacao_btc)
botao_todos.grid(column=0, row=4, padx=15, pady=15)

botao_todos = Button(janela, text='Ver a cotação do Ethereum', command=pegar_cotacao_eth)
botao_todos.grid(column=0, row=5, padx=15, pady=15)


#Deixa a janela em loop
janela.mainloop()





