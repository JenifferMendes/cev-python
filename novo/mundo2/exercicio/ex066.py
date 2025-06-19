"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que é a condição
de parada. no final, mostre quantos números foram digitados e qual foi a soma
entre eles(desconsiderando a flag).
"""


soma = quantidade = 0

while True:
    numero = int(input("Digite um número: [999 para parar] "))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print(f"Você digitou {quantidade} números e a soma entre eles {soma}.")
