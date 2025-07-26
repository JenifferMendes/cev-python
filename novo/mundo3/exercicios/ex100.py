"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.
"""


from random import randint


def sorteia():
    lista = [randint(0,10) for _ in range(5)]
    return lista


def soma_par(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma


print(f"Sorteando 5 valores da lista ", end="")

lista = sorteia()

for c in lista:
    print(f"{c} ", end="")
print("PRONTO!")

soma = soma_par(lista)

print(f"Somando os valores pares de {lista}, temos {soma}.")
