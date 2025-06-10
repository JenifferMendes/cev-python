"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos digitos separados.
"""


numero = input("Digite um número de 0 a 9999:")

print(
    f"Unidade: {numero[3]}\n"
    f"Dezenha: {numero[2]}\n"
    f"Centena:{numero[1]}\n"
    f"Milhar: {numero[0]}"
)
