"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

- 1 para binario
- 2 para octal
- 3 para hexadecimal

"""

numero = int(input("Digite um número: "))
base = int(input(
    "Escolha uma das bases para conversão:\n" 
    "[1] converter para binário,\n" 
    "[2] converter para octal\n" 
    "[3] converter para hexadecimal\n"
    "Qual sua opção:"
))

if base == 1:
    binario = bin(numero)
    print(f"{numero} convertido para Binário é igual: {binario[2:]}")
elif base == 2:
    octal = oct(numero)
    print(f"{numero} convertido para Octal é igual: {octal[2:]}")
elif base == 3:
    hexadecimal = hex(numero)
    print(
        f"{numero} convertido para Hexadecimal é igual: {hexadecimal[2:]}"
    )
else:
    print("voce digitou o número errado.")
