"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- media abaixo de 5.0:
reprovado
- media entre 5.0 e 6.9:
recuperação
média 7.0 ou superior:
aprovado.
"""


nota_um = float(input("Digite a nota1: "))
nota_dois = float(input("Digite a nota2: "))

media = (nota_um + nota_dois) / 2

if media >= 7:
    print(f"Sua média é: {media:.1f}.Parabéns, você foi aprovado.")
elif media >= 5:
    print(f"Sua média é: {media:.1f} Você ficou de reperação.")
else:
    print(f"Sua média é: {media:.1f}. Você está reprovado.")
