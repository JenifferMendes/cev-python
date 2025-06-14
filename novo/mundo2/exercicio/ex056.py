"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos
"""

media_idade = 0
mulher_menor = 0

primeiro_homem = True

for c in range(1, 5):
    print("{:=^69}".format("\33[30;45m {} pessoa\33[m").format(c))
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = int(input(
        "[1] Digite se for mulher\n"
        "[2] Digite se for homem\n"
        "Qual a opção: "
    ))
    media_idade = media_idade + idade
    if sexo == 1:
        if idade < 20:
            mulher_menor = mulher_menor + 1
    elif sexo == 2:
        if primeiro_homem:
            velho = novo = idade
            nome_velho = nome
            primeiro_homem = False
        else:
            if idade > velho:
                velho = idade
                nome_velho = nome
            elif idade < novo:
                novo = idade
    else:
        print("opção invalida")

media = media_idade / 4

print(
    f"A média de idade das pessoas é: {media} anos,\n"
    f"O nome do homem mais velho é: {nome_velho} com {velho} anos,\n"
    f"Tem {mulher_menor} mulher(es) menor de 20 anos."
)
