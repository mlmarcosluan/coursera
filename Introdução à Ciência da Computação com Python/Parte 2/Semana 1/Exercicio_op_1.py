"""
Escreva uma função imprime_matriz que recebe como parâmetro uma matriz e imprima a  matriz
linha por linha 
"""

def imprime_matriz (matriz):

    for i in range (len (matriz)):

        for j in range (len (matriz [0])):
            print (matriz [i][j], end = " ")

        print (end = "")
        
matriz = [[1, 2, 3], [4, 5, 6]]

imprime_matriz (matriz)

#   #   #
##  ##  ##
### ### ###