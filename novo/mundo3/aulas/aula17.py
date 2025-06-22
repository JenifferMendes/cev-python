"""
Lista

a = [2,3,4,5]
b = a[:] (assim voce cria uma copia e não mexe na lista original)
"""


idols = ["Jungkook", "Yunho", "Seonghwa"]
print(idols)
idols[2] = "Mingi"
print(idols)
idols.append("Seonghwa")
print(idols)
idols.insert(4, "san")
print(idols)
idols.pop()
print(idols)
idols.sort()
print(idols)
idols.sort(reverse=True)
print(idols)



idols = []
idols.append("Jungkook")
idols.append("Yunho")
idols.append("Seonghwa")

for posicao, idol in enumerate(idols):
    print(f"Na posicão {posicao} encontrei o idol {idol}!")
print("Cheguei ao final dos idols")