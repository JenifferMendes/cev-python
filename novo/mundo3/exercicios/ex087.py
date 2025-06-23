"""
Aprimore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados.
b) a soma dos valores da terceira coluna.
c) o maior valor da segunda linha
"""


matrix = []
linha_um = []
linha_dois = []
linha_tres = []
maior = pares_soma = posicao = coluna_tres = 0
dash = "\n"+ "-" * 50 + "\n"

for num in range(0, 9):
    numero = int(input(f"Digite um número: [0, {posicao}]: "))
    if posicao == 2:
        coluna_tres += numero
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
    if posicao == 1:
        for pos, num in enumerate(numero):
            if pos == 0:
                maior = num
            if num > maior:
                maior = num

print(
    dash,
    f"\bA soma dos valores pares é {pares_soma}.\n"
    f"A soma dos valores da terceira coluna é {coluna_tres}.\n"
    f"O maior valor da segunda linha é {maior}.\n"
    "Fim"
    )
