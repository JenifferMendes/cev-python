"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
"""


primeiro = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razão da sua PA: "))

decimo = primeiro + (10 - 1) * razao
print(f"Os termos da sua são PA: ")
for c in range(primeiro, decimo + razao , razao):
    print(f"{c}", end="~ ")
print("Sua PA.")
