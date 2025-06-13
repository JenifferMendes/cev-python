"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa. Calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- entre 25-30 - sobrepeso
- entre 30-40 - obesidade
- acima de 40: obesidade mórbida.
"""


peso = float(input("digite o seu peso: kg"))
altura = float(input("digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu imc é: {imc:.0f}. Você está abaixo do peso.")
elif 18.5 <= imc <= 25:
    print(f"Seu imc é: {imc:.0f}. Você está no peso ideal.")
elif 25 < imc <= 30:
    print(f"Seu imc é: {imc:.0f}. Você esta com sobrepeso.")
elif 30 < imc <= 40:
    print(f"Seu imc é: {imc:.0f}. Você está com obesidade.")
elif imc > 40:
    print(f"Seu imc é: {imc:.0f}. Você está com obesidade mórbida.")
else:
    print(f"Digitou algo errado.")
