"""
tuplas
SÃO IMUTÁVEIS.

-> se for somar tuplas, a ordem importa
c.count(x) x => mostra quantos x tem em  c
c.index(y) y->em qual posicao estao y (primeira ocorrencia)
"""


bias = "Jungkook", "Yunho", "Haein", "Seonghwa"


""" for posicao in range(0, len(bias)):
    print(f"{bias[posicao]} é meu Idol {posicao}.") """

""" for posicao, bias in enumerate(bias):
    print(f"{bias} é meu Idol {posicao}.") """

print(sorted(bias))

""" posicao = 0
for idol in bias:
    print(f"{idol} é meu Idol {posicao}.")
    posicao += 1 """
print("Esses são meus bias.")

a = (0, 1, 2)
b = (3, 4, 5, 6)
c = a + b
d = b + a

print(c,d)
print(sorted(d))