"""
A confederação nacional de natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: senior
- acima: master
"""


from datetime import date

hoje = date.today().year

nascimento = int(input("Digite o ano de nascimento: "))

idade = hoje - nascimento

if idade <= 9:
    print(f"Sua idade é {idade} anos.Você está na categoria Mirim")
elif idade <= 14:
    print(f"Sua idade é {idade} anos.Você está na categoria Infantil")
elif idade <= 19:
    print(f"Sua idade é {idade} anos.Você está na categoria Junior")
elif idade <= 20:
    print(f"Sua idade é {idade} anos.Você está na categoria Senior")
elif idade > 20:
    print(f"Sua idade é {idade} anos.Você está na categoria Master")
