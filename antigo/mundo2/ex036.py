"""Escreva um programa para aprovar o empréstimo bancário de uma casa. 
O programa vai perguntar o valor da casa, o salário do comprador e 
em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
30% do salário ou então o empréstimo será negado.
"""


casa_valor = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

meses = anos * 12
parcela = casa_valor / meses
salario_parcela = salario * 0.30

if parcela <= salario_parcela:
    print('Pode pegar o empréstimo')
else:
    print('Não pode pegar o empréstimo')
