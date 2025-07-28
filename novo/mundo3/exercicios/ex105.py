"""
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
"""


def notas(*num, sit=False):
    """"
    -> Função para analisar notas e situaçoes de vários alunos.
    :param num: um ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: diciónario com várias informações sobre a situação da turma.
    """
    tam = len(num)
    maior = menor = media = quantidade = soma =  0
    for p, n in enumerate(num):
        soma += n
        quantidade += 1
        if p == 0:
            maior = n
            menor = n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    media = soma / quantidade
    disc = {
        'total': tam,
        'maior': maior,
        'menor': menor,
        'media': media
    }
    if sit:
        if 10.0 > media >= 7.0:
            disc['situacao'] = 'BOA'
        elif 7.0 > media >= 5.0:
            disc['situacao'] = 'RASOAVEL'
        elif media < 5.0:
            disc['situacao'] = 'RUIM'
    return disc

resp = notas(1.5, 9.5, 10, 6.5, sit=True)
print(resp)
