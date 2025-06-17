"""
melhore o desafio 061, perguntando para o usuario se ele quer mostrar
mais alguns termos. o programa encerra quando ele disser que quer mostrar
0 termos.
"""

primeiro_termo = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razão da sua PA: "))


termos = 1
i = 0
pa = []

while termos != 0:
    termos = int(input("Digite a quantidade de termos que você deseja: "))
    soma = termos + i
    while i != soma:
        pa.append(primeiro_termo + (i * razao))
        i += 1
    print(f"Aqui está sua PA: {pa}")
