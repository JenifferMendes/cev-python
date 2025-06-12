"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

- 1 para binario
- 2 para octal
- 3 para hexadecimal

"""

numero = int(input("Digite um número: "))
base = int(input(
    "Qual a base da conversão, digite 1-binário,2-octal,3-hexadecimal" 
))

if base == 1:
    binario = bin(numero)
    print(f"Base de conversão escolhida foi: binário, seu número é: {binario}")
elif base == 2:
    octal = oct(numero)
    print(f"Base de conversão escolhida foi octal, seu número é: {octal}")
elif base == 3:
    hexadecimal = hex(numero)
    print(
        f"Base de conversão escolhida foi hex, seu número é: {hexadecimal}"
    )
else:
    print("voce digitou o número errado.")
