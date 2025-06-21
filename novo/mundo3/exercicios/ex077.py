"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""


idols = (
    "jungkook", "yunho", "seonghwa", "yeosang", "mingi", "jimin", "hongjoong",
    "taehyung", "namjoon", "yoongi", "jongho", "jhope", "jin",
    "san", "wooyoung",
)
letras = ("a", "e", "i", "o", "u")

for idol in idols:
    print(f"\nNo nome {idol.upper()}, temos: ", end="")
    for letra in letras:
        if letra in idol:
            print(f"{letra.upper()} ", end="")

print("\nDone")
