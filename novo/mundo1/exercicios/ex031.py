"""
Desenvolva um programa que pergunte a distância de uma viagem em km. calcule o
preço da passagem, cobrando R$0,50 por km para viagens até 200km e R$0,40 para
viagens mais longas.
"""


distancia = float(input("Qual a distância da sua viagem? "))

if distancia <= 200:
    valor = distancia * .5
    print(f"Sua passagem fica no valor de R${valor:,.2f}")
else:
    valor = distancia * .45
    print(f"Sua passagem fica no valor de R${valor:,.2f}.")
print("Boa viagem!")
