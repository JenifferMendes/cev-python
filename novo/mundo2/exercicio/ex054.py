"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""


from datetime import date


ano = date.today().year

menores = 0
maiores = 0
for c in range(0, 7):
    nascimento = int(input("Digite seu ano de nascimento: "))
    idade = ano - nascimento
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
    #print(nascimento, ano, idade, menores, maiores)
print(f"Tem {menores} menores de idade e {maiores} maiores de idade.")
