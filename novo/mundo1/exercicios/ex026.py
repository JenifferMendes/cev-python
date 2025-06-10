"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantos vezes aparece a letra A.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
"""


frase = input("Digite uma frase: ")

frase_lower = frase.lower()
letra_count_a = frase_lower.count("a")
letra_a = frase_lower.find("a")

print(
    f"A frase: {frase_lower}, contém: {letra_count_a}A, e" 
    f" o primeiro A aparece na posição: {letra_a}."
)
