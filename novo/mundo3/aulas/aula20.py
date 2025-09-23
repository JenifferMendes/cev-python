""""
Funções - parte 01
"""
""" n = 40

def titulo(msg):
    print('-' * n)
    print(f"{msg:^{n}}")
    print('-' * n)


titulo("BTS")
titulo("Stray Kids")
titulo("Ateez")

22/09/2025

funcoes - parte 01

rotina.
o python tem varias funcoes que vem com ele como :print(), len(), input(), 
int(), float().... são funções

def - define a função
cria a função
pule duas linhas abaixo 
voce pode usar parametros na função para ficar ainda mais personalizado sua função.

def mostraLinha():
    print("-------------------")


mostraLinha()
print("sistema de alunos")
mostraLinha()


def mensagem(msg):
    print("----------------")
    print(msg)
    print("----------------")

mensagem("SISTEMA DE ALUNOS")


até 20:13

23/09/2025

funções são rotinas

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

def soma(a,b):
    s = a + b
    print(s)


# programa principal
soma(4,5)
soma(8,9)
soma(2,1)

def contador(* num):
    tam = len(num)
    print(f"Recebe os valores {num} e são ao todo {tam} números ")


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos +=1

valores = [1,2,3,4,5]
dobra(valores)
print(valores)

-> fiz os exercicios já.
revi as resolução do 97 até 100
 """


for c in range(10, -1, -1):
    print(c)