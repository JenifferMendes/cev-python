"""
Crie um programa que crie uma matriz de dimensão 3x3 e preenha com valores
lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""


matrix = []
linha_um = []
linha_dois = []
linha_tres = []
posicao =  0
dash = "\n"+ "-" * 50 + "\n"

for num in range(0, 9):
    numero = int(input(f"Digite um número: [0, {posicao}]: "))
    posicao += 1
    if posicao == 3:
        posicao = 0
    if numero % 2 == 0:
        pares_soma += numero
    if num < 3:
        linha_um.append(numero)
    elif num < 6:
        linha_dois.append(numero)
    else:
        linha_tres.append(numero)

matrix.append(linha_um)
matrix.append(linha_dois)
matrix.append(linha_tres)

print(dash)

for posicao, numero in enumerate(matrix):
    print(f"[ {numero[0]} ] [ {numero[1]} ] [ {numero[2]} ]")

print("Fim")
