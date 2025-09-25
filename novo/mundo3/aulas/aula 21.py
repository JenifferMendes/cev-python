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
    """
   """ -> Faz uma contagem e mostra na tela.
   :param i:inicio da contagem
   :param f: fim da contagem
   :param p: passo da contagem
   :return: sem retorno
   """
    """
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

"""
