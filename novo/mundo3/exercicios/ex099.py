"""
Faça um programa que tenha uma função chamada maior(), que recebe vários parâme
tros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*num: int):
    dash = "-=" * 20
    print(dash)
    print("Analisando os valores passados...")
    tam = len(num)
    for n in num:
        print(f"{n} ", end="")
    print(f"Foram informados {tam} valores ao todo.")
    if tam == 0:
        print(f"Nenhum valor foi informado.")
    else:
        print(f"O maior valor informado foi {max(num)}.")


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
