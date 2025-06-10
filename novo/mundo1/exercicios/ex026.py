"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantos vezes aparece a letra A.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
"""


frase = input("Digite uma frase: ").strip()

frase_lower = frase.lower()
letra_count_a = frase_lower.count("a")
letra_primeira_a = frase_lower.find("a")
letra_ultimo_a = frase_lower.rfind("a")

print(
    f"A frase: {frase_lower}, contém: {letra_count_a}A, e" 
    f" o primeiro A aparece na posição: {letra_primeira_a}.\n"
    f"O último A aparece na posição: {letra_ultimo_a}"
)
