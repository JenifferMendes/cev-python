""""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro(), e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


import moeda


b = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(b)} é {moeda.metade(b, True)}")
print(f"O dobro de {moeda.moeda(b)} é {moeda.dobrar(b, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(b, 10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(b, 13, True)}")
