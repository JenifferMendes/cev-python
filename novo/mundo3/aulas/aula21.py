"""
25/09/2025

Aula 21

INTERACTIVE HELP
-> help()
funciona quando voce "ativa" o python no terminal e voce digita o comando para
voce digitar algum comando interno do python e ele te dar uma explicação sobre.

voce pode usar também o comando:
print(input.__doc__)
no caso do input, pode ser qualquer outro comando, mas nesse caso vai abrir so
sobre aquele comando


DOCSTRINGS
docstrings - é uma string de documentação

def contador(i,f,p):
    [entra aqui as docstring]
    """""" -> Faz uma contagem e mostra na tela.
   :param i:inicio da contagem
   :param f: fim da contagem
   :param p: passo da contagem
   :return: sem retorno
   """"""
    c = i
    while c <=f:
        print(f"{c} ", end="")
        c +=p
    print("FIM")


contador(2,10,2)

PARAMETROS OPCIONAIS

Parametros opcionais.

def somar(a,b,c):
    s= a+ b+ c
    print(f"A soma vale(s)")


somar(3,2,5)
somar(8,4)

caso o somar(a,b,c=0)
c nesse caso seria opcional e se não receber um valor, será substituido por 0
neste caso.
vc pode fazer isso com todos os parametros.

26/09/2025
Parte 2

ESCOPO DE VARIÁVEIS

Escopo de uma variável é uma região onde pode ser acessada.


def teste():
    x = 8
    print(f"na função texte, o n vale {n}")
    print(f"na função texte, o x vale {x}")


#Programa Principal
n = 2
print(f"No programa principal, n vale (n)")
teste()
print(f"No programa principal, x vale {x}")

esse programa deve dar erro, pois x não foi atribuido fora da função teste, logo
qualquer tentativa de usar o x fora da função deve dar erro. Nesse caso, o 
escopo da variavel x é local 
No caso da variavel n, ela possui escopo global

caso voce defina duas variaveis com o mesmo nome, o que vai mandar quando fazer
uma função, será a variavel local e não global. Ou seja, caso tenha uma variavel
x = 10 na função,será uma variavel local e uma X = 5 na variavel global.

def teste():
    x = 10
    print(f"dentro x vale: {x}")


x = 5
teste()
print(f"fora x vale: {x}")

nesse caso, vai aparecer o 10 no terminal para o valor de x dentro e fora x vale 
5.

voce pode usar a palavra global + variavel dentro da funcao, para que nesse o valor atribuido
seja o valor global.

def teste(b):
    global a
    a = 8
    b+=4
    c = 2
    print(f"dentro a vale: {a}")
    print(f"dentro b vale: {b}")
    print(f"dentro c vale: {c}")


a = 5
teste(a_
print(f"A fora vale(a)")

Retornando Valores

=> palavra reservada: return

def somar(a=0, b=0, c=0):
    s= a + b+ c
    return s


r1 = somar(3,2,5)
r2 = somar(8,4)

"""
