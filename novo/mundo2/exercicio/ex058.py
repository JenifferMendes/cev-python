"""
melhore o jogo desafio 028, onde o computador vai pensar em um numero entre 0 e
10. so que agora o jogador vai tentar adivinhar ate acertar, mostrando
no final quantos palpites foram necessarios para vencer.
"""


from random import randint


print("Bem vindo ao jogo tente adivinhar um número.")
print("Tente adivinhar o número que estou pensando! um número entre 0 a 10.")

numero_pc = randint(0,10)
numero_jogador = 0
palpites = 0
while numero_pc != numero_jogador:
    numero_jogador = int(input("De um palpite:"))
    if numero_jogador > 10:
        print("Você digitou um número errado. Tente novamente")
    if numero_jogador <= 10:
        if numero_jogador!= numero_pc:
            if numero_jogador > numero_pc:
                print("Menos... tente um número menor!")
            if numero_jogador < numero_pc:
                print("Mais...tente um número maior!")
            palpites += 1
print(f"Você acertou!! O número total de palpites foi de {palpites} vezes.")
