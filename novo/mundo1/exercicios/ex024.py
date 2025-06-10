"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou
não com o nome Santo.
"""


cidade = input("Qual é o nome da sua cidade? ")

cidade_lower = cidade.lower()
cidade_santo = "santo"in cidade_lower
print(
    f"A sua cidade é: {cidade.title()}, "
    f"a cidade possui Santo no nome? {cidade_santo}."
)
