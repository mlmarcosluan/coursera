"""
Escreva a função ordena (lista), que recebe uma lista com números inteiros como parâmetro e devolve
esta lista ordenada em ordem crescente
"""

def ordena (lista):

    fim = len (lista)

    for i in range (fim - 1):

        posicao_minimo = i

        for j in range (i + 1, fim):

            if lista[j] < lista [posicao_minimo]:
                posicao_minimo = j

        lista [i], lista [posicao_minimo] = lista [posicao_minimo], lista [i]

    return lista

#   #   #
##  ##  ##
### ### ###