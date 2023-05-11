"""Crie um programa que leia o nome de uma pessoa e diga se ela tem 
"Silva" no nome"""


nome = input('Digite o seu nome: ').strip().lower()

silva = nome.find('silva')

print(silva != -1)
