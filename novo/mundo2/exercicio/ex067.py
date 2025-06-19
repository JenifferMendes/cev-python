"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo.
"""


dash = "\n" + "="* 25 + "\n"
count = 1

numero = int(input("Digite um número: "))

print(dash)

while True:
    if numero < 0:
        break
    print(dash)
    print(f"TABUADA DO {numero}\n")
    while count <= 10:
        tabuada = numero * count 
        print(f" {numero} x {count} = {tabuada}")
        count += 1
    print(dash)
    numero = int(input("Digite um novo número: "))
    count = 1
print(f"Fim")
