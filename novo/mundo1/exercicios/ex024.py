"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou
não com o nome Santo.
"""


cidade = input("Qual é o nome da sua cidade? ").strip()

cidade_lower = cidade.lower()
cidade_santo = cidade_lower[:5] == "santo"
print(
    f"A sua cidade é: {cidade.title()}, "
    f"a cidade possui Santo no começo do nome? {cidade_santo}."
)
