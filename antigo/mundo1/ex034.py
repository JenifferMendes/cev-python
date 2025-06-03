"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
para salários superiores a R$1250,00 calcule um aumento de 10%
para salarios inferiores ou iguais, o aumento é de 15%"""


salario = float(input('Digite seu salário: '))

if salario > 1250:
    salario_aumento = salario + (salario * 0.1)
    print(f'O seu salário aumentou para R${salario_aumento:.2f}')
if salario <= 1250:
    salario_aumento2 =salario + (salario * 0.15)
    print(f'O seu salário aumentou para R${salario_aumento2:.2f}')
