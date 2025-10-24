"""
Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu
nome e idade em um arquivo de texto simples.

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as 
pessoas cadastradas.
"""


from biblioteca.interface import *
from biblioteca.arquivo import *
from time import sleep


nome_arquivo = "exercicios/ex115/bancodedados.txt"

if not arquivoExiste(nome_arquivo):
    criarArquivo(nome_arquivo)

while True:
    resposta = menu([
        "Ver pessoas cadastradas",
        "Cadastrar nova Pessoa" ,
        "Sair do Sistema",
        ])
    if resposta == 1:
        # opcao de listar o conteúdo de um arquivo
        lerArquivo(nome_arquivo)
        sleep(5)
    elif resposta == 2:
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrarPessoa(nome_arquivo, nome, idade)
    elif resposta == 3:
        titulo("Saindo do sistema...Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida! ")
    sleep(2)
