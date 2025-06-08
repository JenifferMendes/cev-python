"""
Escreva um programa que pergunte a quantidade de KM percorridos por um carro
alugado e a quantidade de dias pelas quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
"""


dias = int(input("Quantos dias foi utilizado o carro? "))
km_rodado = float(input("Quantos km foram rodados? "))

valor_km_rodado = km_rodado * .15
valor_dia_usado = dias * 60
total_pagar = valor_km_rodado + valor_dia_usado

print(
    f"Você usou o carro por {dias} dias, e rodou por {km_rodado:,.2f}km "
    f"o valor a pagar fica R${total_pagar:,.2f}."
)
