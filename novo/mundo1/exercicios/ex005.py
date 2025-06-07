"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
e seu antecessor.
"""


num = int(input("digite um número: "))
num_antecessor = num - 1
num_sucessor = num + 1

print(
    f"O número que você digitou foi: {num}"
    f", o seu antecessor é: {num_antecessor}"
    f", o seu sucessor é: {num_sucessor}."
)
