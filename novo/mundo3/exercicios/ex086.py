"""
Crie um programa que crie uma matriz de dimensão 3x3 e preenha com valores
lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""


matrix = []
linha_um = []
linha_dois = []
linha_tres = []

for num in range(0, 9):
    if num < 3:
        linha_um.append(int(input(f"Digite um número: [0, {num}]: ")))
    elif num < 6:
        linha_dois.append(int(input(f"Digite um número: [1, {num}]: ")))
    else:
        linha_tres.append(int(input(f"Digite um número: [2, {num}]: ")))

matrix.append(linha_um)
matrix.append(linha_dois)
matrix.append(linha_tres)

dash = "\n"+ "-" * 50 + "\n"

for posicao, numero in enumerate(matrix):
    print(f"[ {numero[0]} ] [ {numero[1]} ] [ {numero[2]} ]")

print("Fim")
