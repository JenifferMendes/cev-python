"""
crie um programa que leia varios numeros inteiros pelo teclado.
o programa so vai aparar quando o usuario digitar o valor 999, que é a condição
de parada. no final, mostre quantos numeros foram digitados e qual foi a soma
entre eles, desconsiderando o flag.(o 9990)
"""

numero = 0
soma = 0
quantidade = 0
while numero != 999:
    numero = int(input("digite um número: "))
    if numero != 999:
        soma += numero
        quantidade += 1
        print(soma, quantidade)
print(
    f"Você digitou {quantidade} números e a soma de todos eles é: {soma}."
)
