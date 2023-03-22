"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome delas e escrevendo o nome do escolhido"""


import random


aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4 ]

aluno_sorteado = random.choice(alunos)

print(f'O aluno sorteado foi {aluno_sorteado}')
#print(f'O aluno sorteado foi {alunos[aluno_sorteado]}')
#print(f'{globals().get(f"aluno{aluno_sorteado}")}')
