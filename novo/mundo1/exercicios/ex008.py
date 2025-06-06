"""Escreva um programa que leia um valor em metros e o exiba convertido 
em centrimentros e minilimetros"""

metro = float(input("Qual é o valor em metros? "))
centimetro = metro * 100
milimetro = metro * 1000
print(f'O valor digitado em metros é: {metro}', end="")
print(f', isso é {centimetro}cm e {milimetro}mm')
