"""
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada.
"""


def contador(inicio: int, fim: int, passo: int):
    dash = "-=" * 40
    print(dash)
    passo = abs(passo) or 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c)


contador(1,10,1)
contador(10,0,2)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)
