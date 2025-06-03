"""Escreva um programa que pergunte a quantidade KM percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço 
a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado"""


km_rodado = float(input('Digite a quantidade de KM rodado: '))
dias_alugados = float(input('Digite a quantidade de dias que foi utilizado: '))

valor_dias = dias_alugados * 60
valor_km = km_rodado * 0.15
valor_total = valor_dias + valor_km

print(f'A quantidade de km rodados foi igual a {km_rodado}km')
print(f'A quantidade de dias alugados foi {dias_alugados}')
print(f'A quantidade de km cobrado foi R${valor_km:.2f}')
print(f'A quantidade de dias cobrado foi R${valor_dias:.2f}')
print(f'O valor total a pagar é R${valor_total:.2f}')
