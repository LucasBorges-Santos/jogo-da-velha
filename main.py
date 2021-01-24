def PegarValores(tab):
    a = 'a  ' + tab.get('a1') + ' | ' + tab.get('a2') + ' | ' + tab.get('a3') + ' '
    b = 'b  ' + tab.get('b1') + ' | ' + tab.get('b2') + ' | ' + tab.get('b3') + ' '
    c = 'c  ' + tab.get('c1') + ' | ' + tab.get('c2') + ' | ' + tab.get('c3') + ' '
    return ['Jogo da velha', ' ', '  1   2   3', a, '  ' + ('-' * 13), b, '  ' + ('-' * 13), c]


def CriarTabuleiro():
    return {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}


def MostrarTabela(valores):
    for valor in valores:
        print(valor.center(20))


def ConferirVitoria(tab):
    vit = None
    for vitoria in vitorias:
        if vit is None:
            if tab.get(vitoria[0]) == 'X' and tab.get(vitoria[1]) == 'X' and tab.get(vitoria[2]) == 'X':
                vit = "X"

            if tab.get(vitoria[0]) == 'O' and tab.get(vitoria[1]) == 'O' and tab.get(vitoria[2]) == 'O':
                vit = "O"
    return vit


def ConferirJogador(jog):
    if jog == 'X':
        jog = 'O'
    else:
        jog = "X"
    return jog


while True:
    tabuleiro = CriarTabuleiro()

    vitorias = (
        ('a1', 'a2', 'a3'),
        ('b1', 'b2', 'b3'),
        ('c1', 'c2', 'c3'),
        ('a1', 'b1', 'c1'),
        ('a2', 'b2', 'c2'),
        ('a3', 'b3', 'c3'),
        ('a1', 'b2', 'c3'),
        ('a3', 'b2', 'c1')
    )

    jogador = 'X'
    x = 1

    while x <= 9:
        MostrarTabela(valores=PegarValores(tabuleiro))

        Resposta = input(f'\nJogador {jogador}: ')
        print()

        if Resposta in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
            if Resposta[0] == 'a':
                if tabuleiro[Resposta] == " ":
                    tabuleiro[Resposta] = jogador
                    x += 1
                    jogador = ConferirJogador(jogador)

                else:
                    print('\nJá preenchido, Informe outra opção.\n')

            elif Resposta[0] == 'b':
                if tabuleiro[Resposta] == " ":
                    tabuleiro[Resposta] = jogador
                    x += 1
                    jogador = ConferirJogador(jogador)

                else:
                    print('\nJá preenchido, Informe outra opção.\n')

            elif Resposta[0] == 'c':
                if tabuleiro[Resposta] == " ":
                    tabuleiro[Resposta] = jogador
                    x += 1

                    jogador = ConferirJogador(jogador)

                else:
                    print('\nJá preenchido, Informe outra opção.\n')

            Vitoria = ConferirVitoria(tabuleiro)
            if Vitoria is not None:
                break

        else:
            print("\nInforme uma opção valida.\n")

    MostrarTabela(valores=PegarValores(tabuleiro))
    print()

    if Vitoria is None:

        print("Empate.")
    else:
        print(f"Vitoria de {Vitoria}.")

    continuar = input("Deseja repitir?(s/n)")
    if continuar == 'n':
        break
