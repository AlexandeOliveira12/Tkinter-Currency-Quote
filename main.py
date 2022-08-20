import requests
from tkinter import *

#Funções
#Pegando todas as cotações
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_resultado_todos["text"] = texto

#Pegando cotação Dolar
def pegar_cotacao_dolar():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    
    texto = f'''
    Dólar: {cotacao_dolar}'''

    texto_resultado_todos["text"] = texto  

#Pegando cotação Euro
def pegar_cotacao_euro():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_euro = requisicao_dic['EURBRL']['bid']
    
    texto = f'''
    Euro: {cotacao_euro}'''

    texto_resultado_todos["text"] = texto 

#Pegando cotação BTC
def pegar_cotacao_btc():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    
    texto = f'''
    BTC: {cotacao_btc}'''

    texto_resultado_todos["text"] = texto           
        
#Tkinter
#Cria a janela
janela = Tk()

#Titulo
janela.title("Cotação atual das Moedas")

#Textos
#Criando texto
texto_orientacao = Label(janela, text="Clique no botão para ver a cotação das moedas")
texto_orientacao.grid(column=0, row=0, padx=15, pady=15)

#Resultado da busca
texto_resultado_todos = Label(janela, text='Por favor,clique no botão apra ver as cotações')
texto_resultado_todos.grid(column=0, row=5, padx=15, pady=15)


#Botões
#Criando botão para todas as cotações
botao_todos = Button(janela, text='Clique aqui para ver cotações', command=pegar_cotacoes)
botao_todos.grid(column=0, row=1, padx=15, pady=20)

#Criando botão para cotação do dolar
botao_todos = Button(janela, text='Clique aqui para ver a cotação do Dolar', command=pegar_cotacao_dolar)
botao_todos.grid(column=0, row=2, padx=15, pady=15)

#Criando botão para cotação do Euro
botao_todos = Button(janela, text='Clique aqui para ver a cotação do Euro', command=pegar_cotacao_euro)
botao_todos.grid(column=0, row=3, padx=15, pady=15)

#Criando botão para cotação do BTC
botao_todos = Button(janela, text='Clique aqui para ver a cotação do BTC', command=pegar_cotacao_btc)
botao_todos.grid(column=0, row=4, padx=15, pady=15)


#Deixa a janela em loop
janela.mainloop()





