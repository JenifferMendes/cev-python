"""
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização detalhada do aproveitamento de cada jogador.
"""
jogadores = []
n = 25
dash = "--" * n

while True:
    print(dash)
    
    jogador = {}
    gols = []
    total = 0
    
    jogador['nome']= input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for p in range(0, partidas):
        qgol = int(input(f"quantos gols na partida {p + 1}: "))
        gols.append(qgol)
        total += qgol

    jogador["gols"] = gols[:]
    jogador["total"] = total
    jogadores.append(jogador.copy())
    opcao = ["S", "N"]
    continuar = " "
    while continuar not in opcao:
        continuar = input("Quer continuar? [S/N]: ").strip().upper()[0]
        if continuar not in opcao:
            print("ERRO! Por favor, digite S ou N.")
    if continuar == "N":
        break

print("-=" * n)
print(f'cod', end="")
for i in jogador.keys():
     print(f" {i:<15}", end=" ")
print()
print(dash)

tamanho = len(jogadores)

for k,v in enumerate(jogadores):
    print(f"{k:>4} ", end="")
    for d in v.values():
         print(f"{str(d):<15}", end="")
    print()
print(dash)


while True:
    joga = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if joga == 999:
            print("<<<VOLTE SEMPRE>>>")
            break
    if  joga >= tamanho or joga < 0:
        print(f"ERRO! Não existe jogador com código {joga}! Tente novamente!")
    else:
        print(f"-> LEVANTAMENTO DO JOGADOR: {jogadores[joga]["nome"]}")
        for k,v in enumerate(jogadores):
            for i,e in enumerate(jogadores[k]["gols"]):
                if k == joga:
                    print(f"     => No jogo {i + 1}, fez {e} gols.")
