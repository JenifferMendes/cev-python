"""Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

1) para binário
2) para octal
3) hexadecimal 
"""


numero = int(input('Digite um número: '))
opcao = int(input("""Qual a base de conversão? 
                  DIGITE 1 PARA BINÁRIO
                  DIGITE 2 PARA OCTAL,
                  DIGITE 3 PARA HEXADECIMAL: """))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if opcao == 1:
    print(f'Você escolheu a opção 1(binário) - seu número {numero} e em binário {binario} ')
elif opcao == 2:
    print(f'Você escolheu a opção 2(octal) - seu número {numero} e em octal {octal} ')
elif opcao == 3:
    print(f'Você escolheu a opção 3(hexadecimal) - seu número {numero} e em hexadicimal {hexadecimal}')
else:
    print('Opção inválida.')
