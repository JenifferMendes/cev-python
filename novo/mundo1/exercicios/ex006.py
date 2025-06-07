"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
raiz quadrada.
"""

num = int(input("Digite um número: "))
num_dobro = num * 2
num_triplo = num * 3
num_raiz_quadrada = num ** (1 / 2)

print(
    f"O número que você digitou foi: {num}"
    f", O dobro de {num} é {num_dobro}"
    f", O Triplo de {num} é {num_triplo}"
    f", A raiz quadrada de {num} é {num_raiz_quadrada:.2f}."
)
