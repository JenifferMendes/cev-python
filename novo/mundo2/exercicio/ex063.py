"""
escreva um programa que leia um numero n inteiro qualquer e mostre na tela os
n primeiros elementos de uma sequencia de fibonacci
ex
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""


numero = int(input(
    "Digite a quantidade de números da sequência de Fibonacci: ")
)
fibonacci = [0, 1]

while len(fibonacci) < numero:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)

if numero == 1:
    print("Sua sequência de Fibonacci [0].")
else:
    print(f"Sua sequência de fibonacci é {fibonacci}.")
