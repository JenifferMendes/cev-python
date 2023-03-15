"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento"""


salario =  float(input('Digite o salário do funcionário: '))

ajuste_salario = salario * 0.15
salario_reajustado = salario + ajuste_salario

print(f'O salário do funcionário é igual a R${salario:.2f}.')
print(f'O novo salário com reajuste é igual a R${salario_reajustado:.2f}')
