"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante á função input() do python, só que fazendo a validação para aceitar
apenas um valor númerico.
ex:
n = leiaInt("Digite um n")
"""


def leia_int(msg):
    ok = False
    valor = 0
    while True:
        print(msg, end="")
        num = input()
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print("ERRO! Digite um número inteiro válido.")
        if ok:
            break
    return valor


n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
