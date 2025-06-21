"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequencia.
No final, mostre uma listagem de preços. Organizando os dados em forma tabular.
"""


produtos = (
    "Lápis", 1.75, 
    "Borracha", 2.00,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canetas", 22.30,
    "Livro", 34.90
)

n = 51
dash = "-" * n

print(dash)
print(f"{'LISTAGEM DE PREÇOS':^{n}}")
print(dash)

tamanho = len(produtos)

for c in range(0, tamanho, 2):
    print(f"{produtos[c]:.<40}R${produtos[c+1]:>8.2f}")
print(dash)
