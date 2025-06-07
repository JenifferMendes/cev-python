"""
Faça um programa que leia a largura e a altura de uma parece em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma area de 2m².
"""


largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = largura * altura
tinta = area / 2

print(f"A área que deseja pintar é {area}m² e a tinta necessaria é {tinta}l")
