"""
Escreva um programa que converta uma temperatura digita em ºC e converta para
ºF.  C = 5/9 x (F – 32).
"""


celsius = float(input("Qual a temperatura em graus celsius?" ))

fahrenheit = celsius * 9 / 5 + 32

print(f"A temperatura de {celsius:,.0f}ºC é igual a {fahrenheit:,.0f}ºF")
