"""
Escreva um programa para aprovar o empréstimo bancário para a compra de
uma casa.O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salario ou então o emprestimo será negado.
"""


casa = float(input("Qual é o valor da casa? R$"))
salario = float(input("Qual é o seu sálario? R$"))
ano = float(input("Quantos anos você quer pagar o valor da casa? "))

mes = ano * 12
parcela = casa / mes
salario_limite = salario * 0.3
print(parcela)
if parcela <= salario_limite:
    print(f"Você pode financiar sua casa em {mes} x R${parcela:,.2f}.")
else:
    print(f"Infelizmente você não pode pegar emprestimo")
