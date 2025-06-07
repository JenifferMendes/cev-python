"""
Escreva um programa que leia um valor em metros e o exiba convertido
em centrimentros e minilimetros
"""


metro = float(input("Qual é o valor em metros? "))

centimetro = metro * 1e2
milimetro = metro * 1e3

print(
    f"O valor digitado em metros é: {metro}"
    f", isso é {centimetro}cm e {milimetro}mm"
)
