"""
Crie um programa onde o usuário possas digitar cinco valores númericos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""


numeros = []
for pos in range(0,5): 
    numero = int(input(f"Digite o número da posição {pos}: "))
    if pos == 0 or numero >= numeros[-1]:
        numeros.append(numero)
        print(f"Adicionado ao final da lista...")
    else:
        for posicao,num in enumerate(numeros):
            if numero <= num: 
                numeros.insert(posicao, numero)
                print(f"Adicionado na posição {posicao}...")
                break 

print(f"Os números digitados em ordem foi: {numeros}.")
