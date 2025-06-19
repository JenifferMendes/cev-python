"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo.
"""


dash = "\n" + "="* 25 + "\n"

print(dash)
numero = int(input("Digite um número: "))


while numero > 0:
    print(dash)
    print(f"TABUADA DO {numero}\n")
    for count in range(0,11):
        print(f" {numero} x {count} = {numero * count}")
    print(dash)
    numero = int(input("Digite um novo número: "))
print(f"Fim")
