""""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro(), e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


from utilidadesCev import moeda
from utilidadesCev import dado

b = dado.leiaDinheiro("Digite o preço: R$")

moeda.resumo(b)
