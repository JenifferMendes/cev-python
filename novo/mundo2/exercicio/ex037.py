"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

- 1 para binario
- 2 para octal
- 3 para hexadecimal

voltar a fazer quando entender as conversoes.(assistir o curso do guanabara.)
"""

numero = int(input("Digite um número: "))
base = int(input(
    "Qual a base da conversão, digite 1-binário,2-octal,3-hexadecimal" 
        ))

if base == 1:
    print("Base de conversão escolhida foi: binário")
elif base == 2:
    print("Base de conversão escolhida foi octal")
elif base == 3:
    print("Base de conversão escolhida foi hexadecimal")
print("voce digitou os números errados.")
