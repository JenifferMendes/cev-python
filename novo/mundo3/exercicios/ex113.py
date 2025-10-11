def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário")
            return 0
        else: 
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número real válido.")
        except (KeyboardInterrupt):
            print("Usuário preferiu não digitar esse número.")
            return 0
        else:
            return n


num_int = leiaInt("Digite um número Inteiro: ")
num_float = leiaFloat("Digite um número Float: ")
print(f"O valor inteiro digitado foi {num_int} e o valor float foi {num_float}")