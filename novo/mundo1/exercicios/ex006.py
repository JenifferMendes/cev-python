"""" Crie um algoritmo que leia um número e mostre o seu dobro, triplo e 
raiz quadrada"""

num = int(input('Digite um número: '))
numDobro = num * 2
numTriplo = num * 3
numRaizQuadrada = num * (1/2)
print(f'O número que você digitou foi: {num}', end="")
print(f', O dobro de {num} é {numDobro}', end="")
print(f', O Triplo de {num} é {numTriplo}', end="")
print(f', A raiz quadrada de {num} é {numRaizQuadrada}.')
