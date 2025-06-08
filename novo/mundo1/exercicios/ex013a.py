"""
Crie um programa que leia o preço de um produto, mostrando seu preço a vista
com desconto de 10% e preço parcelado com aumento de 8%.
"""


produto = float(input("Qual é o valor do produto? R$"))

produto_vista = produto * .90
produto_parcelado = produto * 1.08

print(
    f"O valor do produto no débito fica R${produto:,.2f}, "
    f"a vista R${produto_vista:,.2f} e parcelado {produto_parcelado:,.2f}."
)
