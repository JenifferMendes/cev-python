"""
Escreva um programa que faça o computador "pensar"em um número inteiro entre 0
e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""


from random import randint
from time import sleep


print("Vou pensar em um número entre 0 e 5. Tente aivinhar!") 
numero = int(input("Tente adivinhar o número, digite um número de 0 a 5: "))

print("Loading...")

sleep(2)

numero_pc = randint(0,5)

if numero == numero_pc:
    print(f"Parabéns, você ganhou: {numero}")
else:
    print(
        f"Ganhei, melhore! O número que pensei foi: {numero_pc} e não {numero}."
    )
