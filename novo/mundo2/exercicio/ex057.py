"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite valores M ou F.
caso esteja errado, peça a digitação novamente até ter um valor correto.
parei aqui
"""


resposta = "H M"
while "M" in resposta or "H" in resposta:
    resposta = input(
        "Digite uma das opçoes abaixo:\n"
        "[M] para Mulher\n"
        "[H] para Homem \n"
    ).upper()
print("Fim")