"""
Crie um programa que leia quantos dolares uma pessoa tem na carteira e
mostre quantos reais ela pode comprar.
"""


dolar = float(input("Digite quantos dolar você possui: $"))

real = dolar * 5.56

print(
    f"Você tem ${dolar:.2f} e você pode comprar "
    f"R${real:.2f} com câmbio: $5,56."
)
