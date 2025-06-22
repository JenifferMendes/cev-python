"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma descente.
c) se o valor 5 foi digitado e esta ou não na lista.
"""


numeros = []
opcoes = ["S", "N"]

while True:
    numero = int(input("Digite um valor: "))
    numeros.append(numero)
    continuar = " "
    while continuar not in opcoes:
        continuar = input("Deseja continuar? [S/N]").upper().strip()
    if continuar == "N":
        break

numeros.sort(reverse=True)

print(
    f"Foram digitados: {len(numeros)} números.\n"
    f"A lista digitada ordenada de forma decrescente foi: {numeros}."
)

quantos_cinco = numeros.count(5)

if quantos_cinco == 0:
    print("Não foi digitado 5 dessa vez.")
elif quantos_cinco == 1:
    print("Há apenas 1 número 5 na lista.")
else:
    print(f"Tem {quantos_cinco} números 5 na lista.")
