"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e a quantidade de tinta necessária para pintá-la, sabendo que litro
de tinta pinta uma área de 2m²"""


largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Agora, digite a altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print(f'A largura da parede é igual a {largura}m e a altura é {altura}m')
print(f'A área dessa parede é igual {area}m²')
print(f'A quantidade necessaria de tinta para pintar a parede será de {tinta:.2f}l')
