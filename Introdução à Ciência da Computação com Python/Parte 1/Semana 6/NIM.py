def computador_escolhe_jogada (n, m): # Devolve o numero de peças que o computador retirou do tabuleiro
    
    maximo_pecas = m
    while maximo_pecas > 0:
        pecas_restante = n - maximo_pecas
        
        if pecas_restante % (m + 1) == 0:
            return maximo_pecas
        
        maximo_pecas = maximo_pecas - 1

    return m

def usuario_escolhe_jogada (n, m): # Pede ao jogador que retire um numero de peças validos

    saida = False

    while not saida:

        jogada_jogador = int (input ("Quantas peças você vai tirar? "))

        if jogada_jogador <= m and jogada_jogador < n and jogada_jogador > 0:
            return jogada_jogador
        else:
            print ("Oops! Jogada inválida! Tente novamente")

def partida (): # Começa a partida e solicita os valores de n e m
    n = int (input ("Quantas peças? "))
    m = int (input ("Limite de peças por jogada? "))

    return n, m

def jogadas (n, m):

    if n % (m + 1) == 0: # O jogador começa
            jogador_atual = "jogador"
            print ("Você começa!")
    else:
        jogador_atual = "computador"
        print ("Computador começa!")

    pecas_atuais = n

    while pecas_atuais > 0:

        if jogador_atual == "computador": # Vez do computador
            jogada_computador = computador_escolhe_jogada (pecas_atuais, m)

            if jogada_computador == 1:
                print ("O computador tirou uma peça.")
            else:
                print ("O computador tirou", jogada_computador, "peças.")

            jogador_atual = "jogador"
            pecas_atuais = pecas_atuais - jogada_computador

        else: # Vez do jogador
            jogada_jogador = usuario_escolhe_jogada (n, m)
                
            if jogada_jogador == 1:
                print ("Você tirou uma peça.")
            else:
                print ("Você tirou", jogada_jogador, "peças.")
            
            jogador_atual = "computador"
            pecas_atuais = pecas_atuais - jogada_jogador

        if pecas_atuais > 0:
            if pecas_atuais > 1:
                print ("Agora restam", pecas_atuais, "peças no tabuleiro.")
            else:
                print ("Agora resta apenas uma peça no tabuleiro.")

        else:
            if jogador_atual == "jogador": # O computador ganhou
                print ("Fim do jogo! O computador ganhou!")
                return "computador"
            else:
                print ("Fim do jogo! Você ganhou!")
                return "jogador"
    
def main ():

    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print ("1 - para jogar uma partida isolada")

    tipo_de_jogo = int (input ("2 - para jogar um campeonato "))

    if tipo_de_jogo == 1: # Jogo isolado
        print ("Você escolheu jogo isolado!")

        n, m = partida ()

        vencedor = jogadas (n, m)

    else:
        print ("Você escolheu um campeonato!")

        n_jogada = 1

        vencedor_computador = 0
        vencedor_jogador = 0

        while n_jogada <= 3:
            print ("**** Rodada", n_jogada, "****")

            n, m = partida ()

            vencedor = jogadas (n, m)

            if vencedor == "computador":
                vencedor_computador = vencedor_computador + 1
            else:
                vencedor_jogador = vencedor_jogador + 1

            n_jogada = n_jogada + 1

        print ("**** Final do campeonato! ****")
        print ("Placar: Você", vencedor_jogador, "X", vencedor_computador, "Computador")




main ()

#   #   #
##  ##  ##
### ### ###