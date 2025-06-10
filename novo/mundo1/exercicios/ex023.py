"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos digitos separados.
"""


numero = int(input("Digite um número de 0 a 9999:"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(
    f"Unidade: {u}\n"
    f"Dezenha: {d}\n"
    f"Centena:{c}\n"
    f"Milhar: {m}"
)
