"""Escreva um programa que converta uma temperatura digitada em °C e converta 
para °F"""


temperatura = float(input('Digite a temperatura em °C: '))

fahrenheit = (temperatura * 9 / 5) + 32

print(f'A temperatura atual é {temperatura:.1f} °C e a temperatura em fahrenheit é {fahrenheit:.1f}°F')
