def computador_escolhe_jogada(n, m):
    pcRemove = 1

    while pcRemove != m:
        if (n - pcRemove) % (m+1) == 0:
            return pcRemove

        else:
            pcRemove += 1

    return pcRemove


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        userRemove = int(input("Quantas peças você vai tirar? "))
        if userRemove > m or userRemove < 1:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            jogadaValida = True

    return userRemove

def campeonato():
    vc=0
    pc=3
    numeroRodada = 1
    while numeroRodada <= 3:
        print(f"\n**** Rodada {numeroRodada} ****\n")
        partida()
        numeroRodada += 1
    print(f"\nPlacar: Você {vc} X {pc} Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vezDoPC = False
    if n % (m+1) == 0:
        print("\nVoce começa!")
    else:
        print("\nComputador começa!")
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            pcRemove = computador_escolhe_jogada(n, m)
            n = n - pcRemove
            if pcRemove == 1:
                print("\nO computador tirou uma peça")
            else:
                print(f"\nO computador tirou {pcRemove} peça")

            vezDoPC = False
        else:
            userRemove = usuario_escolhe_jogada(n, m)
            n = n - userRemove
            if userRemove == 1:
                print("Você tirou uma peça")
            else:
                print(f"Você tirou {userRemove} peças")
            vezDoPC = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            if n != 0:
                print(f"Agora restam, {n} peças no tabuleiro.\n")

    print("Fim do jogo! O computador ganhou!")
print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
tipoDePartida = int(input("2 - para jogar um campeonato "))

if tipoDePartida == 2:
    print("\nVoce escolheu um campeonato!\n")
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()
