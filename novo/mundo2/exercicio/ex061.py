"""
refaça o desafio 51, lendo o primeiro termo e a razão de uma pa.
mostrando os 10 primeiros termos da progressao usando a estrutura while.
"""


primeiro_termo = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razao da sua PA: "))

print(
    f"O primeiro da sua PA é {primeiro_termo}.\n"
    f"A razão da sua PA é {razao}."
)

opcao = 1
pa = [primeiro_termo]
while opcao != 10:
    pa.append(primeiro_termo + (opcao * razao))
    opcao += 1
print(f"Sua PA é {pa}")
