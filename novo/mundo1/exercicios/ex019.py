"""
um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Lendo o nome deles e escrevendo o nome do escolhido.
"""


from random import choice


aluno1 = input("Digite o nome do Aluno1: ")
aluno2 = input("Digite o nome do Aluno2: ")
aluno3 = input("Digite o nome do Aluno3: ")
aluno4 = input("Digite o nome do Aluno4: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(alunos)

print(f"O aluno sorteado para limpar o quadro é o {sorteado}.")
