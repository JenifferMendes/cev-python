"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
"""


termo = int(input("Digite o primeiro termo da sua PA: "))
razao = float(input("Digite a razão da sua PA: "))

pa_soma = termo

print(f"Os termos da sua são PA: {termo:.2f}, ", end="")
for c in range(termo, 9):
    pa_soma = pa_soma + razao
    if c < 8:
        print(f"{pa_soma:.2f}, ",  end="", )
    elif c == 8:
        print(f"{pa_soma:.2f}.")
