"""Desenvolva um programa que pergunte a distância de um viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens até 200km 
e R$ 0,45 para viagens mais longas"""


distancia = int(input('Digite a distância percorrida em KM: '))

passagem_pequena = distancia * 0.50
passagem_longa = distancia * 0.45

if distancia > 200:
    print(f'O valor da passagem é igual a R${passagem_longa:.2f} ')
else:
    print(f'O valor da passagem é igual a R${passagem_pequena:.2f}')
