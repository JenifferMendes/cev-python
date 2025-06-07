"""
Escreva um programa que leia um valor em metros e o exiba convertido
em centrimentros e minilimetros
"""


medida = float(input("Uma distancia em metro? "))

kilometro = medida * 1e-3
hectometro = medida * 1e-2
decametro = medida * 1e-1
decimetro = medida * 1e1
centimetro = medida * 1e2
milimetro = medida * 1e3
micrometro = medida * 1e6
nanometro = medida * 1e9
picometro = medida * 1e12

print(
    f"O valor digitado em metros é: {medida} que é igual a:\n"
    f"{kilometro:,.3f}km\n"
    f"{hectometro:,.3f}hm\n"
    f"{decametro:,.3f}dam\n"
    f"{centimetro:,.0f}cm\n"
    f"{milimetro:,.0f}mm\n"
    f"{micrometro:,.0f}µm \n"
    f"{nanometro:,.0f}nm \n"
    f"{picometro:,.0f}pm \n"
)
