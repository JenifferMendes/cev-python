"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com aumento de 15%
"""


salario = float(input("Qual é o seu salario? R$"))

salario_aumento = salario * 1.15

print(
    f"Parabéns, seu salario passou de R${salario:.2f}"
    f" para R${salario_aumento:.2f}"
)
