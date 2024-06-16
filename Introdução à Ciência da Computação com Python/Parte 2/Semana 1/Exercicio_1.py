"""
Escreva uma função chamada dimensoes que recebe uma matriz como parâmetro e imprima as
dimensões da matriz dada no formato iXj
"""

def dimensoes (matriz):

    linhas = len (matriz)
    colunas = len (matriz[0])

    print (linhas, "X", colunas, sep = "")

#   #   #
##  ##  ##
### ### ###