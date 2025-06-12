"""
Condiçoes Aninhadas
"""


name = str(input("Qual é o idol? "))

idol = name.title()

if idol == "Jungkook" or idol == "Jeon Jungkook" or idol == "Jk":
    print(f"{idol} é o meu marido")
elif idol == "Yunho" or idol == "Jeong Yunho":
    print(f"{idol} é meu namorado")
elif idol == "Haein" or idol == "Jung Haein":
    print(f"{idol} é meu amante")
elif idol == "Chan Eun" or idol == "Cha Eun-woo":
    print(f"É minha amizade colida")
else:
    print(f"Pode ser seu utt, eu deixo")
