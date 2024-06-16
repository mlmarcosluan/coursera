"""
Escreva a função ordenada (lista), que recebe uma lista com números inteiros como parâmetro e devolve
True se a lista estiver ordenada e False se a lista não tiver ordenada
"""

def ordenada (lista):
    fim = len (lista)
    for i in range (fim - 1):

        posicao_minimo = i

        for x in range ((i + 1), fim):
            if lista [x] < lista [posicao_minimo]:
                return False
    
    return True

#   #   #
##  ##  ##
### ### ###