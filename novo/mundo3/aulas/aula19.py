"""
Dicionários
"""

""" 
kpop = {'group': "BTS", "members": ("JK", "JH", "RM", "JM", "J", "YG", "TH")}
print(f"Os membros do {kpop['group']} são {kpop['members']}")
print(kpop.keys(), kpop.items(), kpop.values())


for k, v in kpop.items():
    print(f"O {k} = {v}") """


masculino = dict()
kpop = list()
for c in range(0,3):
    masculino['masculino'] = str(input("Grupo masculino de KPOP: "))
    masculino["sigla"] = str(input("Sigla do grupo: "))
    kpop.append(masculino.copy())
for e in kpop:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
print(kpop)