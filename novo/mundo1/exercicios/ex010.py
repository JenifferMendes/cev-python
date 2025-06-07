"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dolares ela pode comprar.
"""


real = float(input("Quanto de reais você tem: "))

dolar = real / 3.27

print(
    f"Você tem R${real:.2f} e você pode comprar "
    f"${dolar:.2f} com câmbio: R$3,27"
)
