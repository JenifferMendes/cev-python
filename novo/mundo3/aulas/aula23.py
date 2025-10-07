""""
AULAS 23
Erros e Exceções

-> ERROS ACONTECEM SEMPRE!
Exemplo

primt(x)
-> nesse caso sintaxe porque deveria ser print

quando o codigo é apenas:
print(x)
e da o erro neste caso é pq neste caso: o x não existe.
nesse caso há uma exceção: NameError

se você digitar uma letra em algum lugar que deveria ser um valor númerico vai
dar uma exceção, neste caso um ValueError

em casos de divisão por zero, também a erros como: ZeroDivisionError.


r = 2 / '2'
neste caso vai dar erro de TypeError

Quando voce tenta acessar o index que não existe de uma lista, o erro assumido 
será: IndexError

quando voce importa uma biblioteca que não pode ser acessada ou encontrada.
ModuleNotFoundError


há varias exceções dentro do python.


Exception

NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
EOFError
KeyboardInterrupt
OSError
MemoryError
ConnectionError
RuntimeError


try:
-> operação
except Exception as {erro.__class__}:
-> falhou
else:
-> deu certo
finally:
-> certo/falha

time da aula: 22:28
"""