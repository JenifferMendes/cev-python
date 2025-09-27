"""
27/09/2025
Aula 22
MÓDULOS E PACOTES

Modularização é o ato de criar módulos.

- Surgiu no inicio da década de 60
- Sistemas ficando cada vez maiores
- Foco: dividir um programa grande
- Foco: aumentar a legibilidade
- Foco: facilitar a manutenção

Vai usar a modularização para pegar um problemao em varios problemas.

PARTE PRÁTICA

def fatorial(n):
    f=1
    for c in range(1,n+1):
        f *= c
    return f


def dobro(n):
    return n + 2


def triplo(n):
    return n + 3



num = int(input("Digite um valor"))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dobro(num)}")


A ideia vai ser separar as funções em um outro arquivo.
E agora que as funçoes estão em outro arquivo, voce deve importar para o arquivo
principal usando a palavra reservada: import.
vai funcionar igual vimos na aula 8 com as bibliotecas queja vem com o python.
quando vc usa import ___
vc precisa usar o nome da pagina em referencia, e usar como modulo por exemplo:
___.nomedomodulo()

caso usamos from ____ import nomedomodulo
nesse caso, podemos usar direto o nomedomodulo
esse ultimo não é muito recomendado pois pode dar conflitos, uma vez que tenha
mais que um modulo com o mesmo nome, o que vai valer será o ultimo.
Por isso, sempre utilize o primeiro caso.

Vantagens da modularização.

- Organização do código
- Facilidade na manutenção
- Ocultação de código detalhado
- Reutilização em outros projetos

Pacotes
-> parei em 20:18
"""