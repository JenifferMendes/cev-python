"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio,
pergunta se o usuario qual será o valor a ser sacado (numero inteiro) e o
programa vai informar quantas cedulas de cada valor serao entregues.
considerando que o caixa possui cedulas de 50, 20, 10 e 1.
"""


n = 49
dash = "\n" + "=" * n + "\n"

print(dash)
print(f"{'Banco Jotume':^{n}}")
print(dash)

sacar = int(input("Qual valor você deseja sacar? R$"))

notas = [50, 20, 10, 5, 1]

for nota in notas:
    quantidade = sacar // nota
    resto = sacar % nota
    sacar = resto

    if quantidade > 0:
        print(f"A quantidade de notas de {nota} é {quantidade}.")

print(
    dash,
    (
        f"{'\bObrigado por utilizar nosso banco!':^{n}}\n"
        f"{'Banco Jotume':^{n}}"
    ),
    dash,
)
