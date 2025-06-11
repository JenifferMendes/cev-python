"""
Escreva um programa que faça o computador "pensar"em um número inteiro entre 0
e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""


from random import randint


numero = int(input("Tente adivinhar o número, digite um número de 0 a 5: "))

numero_pc = randint(0,5)

if numero == numero_pc:
    print(f"Parabéns o número que você digitou é igual ao do pc: {numero}")
else:
    print(f"que pena, o número foi: {numero_pc}")
print("Adeus")
