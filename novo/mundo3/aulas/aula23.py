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

11/10
Tratar exceções


try:
operação que você quer tentar, comandos que dariam 
except:
se falhou o try , é o que deve acontecer aqui.
else:
se deu certo o try, então vai rodar essa parte
finally:
certo/falha
se deu certo ou errado, irá acontecer

try:
    a = int(input("Numerador: "))
    b = int(input("Demoniador: "))
    r = a / b
except Exception as erro:
    print("Infelizmente tivemos um problema... :( ")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito Obrigada!")

no except voce pode escrever Exception as erro

try:
    a = int(input("Numerador: "))
    b = int(input("Demoniador: "))
    r = a / b
except Exception as erro:
    print("Problema encontrado foi {erro.___class__}:( ")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito Obrigada!")

pode ter except para cada um dos tipos de erros

try:
    a = int(input("Numerador: "))
    b = int(input("Demoniador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou. ")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito Obrigada!")



"""