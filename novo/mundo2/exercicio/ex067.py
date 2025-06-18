"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo.
"""

dash = "\n" + "="* 25 + "\n"

print(dash)

numero = int(input("Digite um número: "))

count = 1


while True:
    print(dash)
    print(f"TABUADA DO {numero}\n")
    while count <= 10:
        tabuada = numero * count 
        print(f" {numero} x {count} = {tabuada}")
        count += 1
    if count > 10:
        print(dash)
        numero = int(input("Digite um novo número: "))
        count = 1
    if numero < 0:
        break
print(f"Fim")
