"""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada KM acima do limite"""


velocidade = int(input('Digite a velocidade do seu carro: '))

multa = (velocidade - 80) * 7

if velocidade >= 80:
    print(f'Sua velocidade ultrapassou 80km/h, sua velocidade foi {velocidade}km/h.')
    print(f'Você tem uma multa de R${multa:.2f} Reais')
else:
    print(f'Continue andando com segurança!')
    