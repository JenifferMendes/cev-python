"""
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$1250,00 calclue um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.
"""


salario = float(input("Digite seu salário: R$"))

if salario <= 1250:
    aumento = salario * 1.15
    print(f"Parabéns seu salario de R${salario} subiu para R${aumento}")
else:
    aumento = salario * 1.10
    print(f"Parabéns seu salario de R${salario} subiu para R${aumento}")
