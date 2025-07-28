"""
Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai 
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa se encerrará.
obs: use cores(não)
"""


def ajuda(com):
    help(com)


def titulo(msg):
    tam = len(msg)
    dash = '-' * tam 
    print(dash)
    print(msg)
    print(dash)


comando = ''
while True:
    titulo("SISTEMA DE AJUDA PYHELP")
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

titulo("ATÉ LOGO!")
