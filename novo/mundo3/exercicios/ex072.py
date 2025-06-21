"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
extenso.
"""


numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
    "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
    "dezeseis", "dezessete", "dezoito", "dezenove", "vinte",
)

usuario = int(input("Digite um número entre 0 e 20: "))

while not 0 < usuario < 20:
    usuario = int(input("Tente novamente. Digite um número entre 0 e 20: "))

print(f"Você digitou o número {numeros[usuario]}.")
