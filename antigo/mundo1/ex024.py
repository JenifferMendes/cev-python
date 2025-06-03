"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não 
com o nome "Santo". """


cidade = input(f'Digite o nome da sua cidade: ').strip()

cidade = cidade.split()
santo = cidade[0]

print(santo.upper() == 'SANTO')
