"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatros e mostre
a ordem sorteada
"""


from random import sample


aluno1 = input("Digite o nome do Aluno1: ")
aluno2 = input("Digite o nome do Aluno2: ")
aluno3 = input("Digite o nome do Aluno3: ")
aluno4 = input("Digite o nome do Aluno4: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = sample(alunos, k=4)

print(f"A ordem para apresentação é: {sorteio}")
