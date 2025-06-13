"""
Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que
tipo de triangulo será formado:

-equilátero: todos os lados iguais.
-isosceles: dois lados iguais
-escaleno: todos os lados diferentes.
"""


reta_um = float(input("Digite a reta_um: "))
reta_dois = float(input("Digite a reta_dois: "))
reta_tres = float(input("Digite a reta_tres: "))

if (
    reta_um + reta_dois > reta_tres 
    and reta_dois + reta_tres > reta_um 
    and reta_um + reta_tres > reta_dois
):
    if reta_um == reta_dois == reta_tres:
        print("Voce tem um equilátero.")
    elif (
        reta_um == reta_dois and reta_um != reta_tres 
        or reta_um == reta_tres and reta_tres != reta_dois 
        or reta_dois == reta_tres and reta_tres != reta_um
    ):
        print("Voce é um isosceles")
    else:
        print("Voce é um escaleno")
else:
    print("Não forma um triângulo")
