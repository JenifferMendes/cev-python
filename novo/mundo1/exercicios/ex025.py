"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome.
"""


nome = input("Digite seu nome completo: ").strip()

nome_lower = nome.lower()
silva = "silva" in nome_lower

print(
    f"Seu nome é: {nome.title()}.\n"
    f"Seu nome tem Silva? {silva}."
)
