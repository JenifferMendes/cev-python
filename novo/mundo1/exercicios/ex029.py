"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 POR CADA KM acima do limite.
"""


velocidade = int(input("Qual é a velocidade do carro: "))

if velocidade <= 80:
    print("Parabéns, está dentro do limite. Dirija com cuidado!")
else:
    multa = (velocidade - 80) * 7
    print(f"Você está acima do limite, foi multado em: R${multa:,.2f}!")
