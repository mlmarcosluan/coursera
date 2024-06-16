"""
Escreva uma função sao_multiplicaveis que recebe como paramentro duas funções e retorna
True se as matrizes forem multiplicavel e False caso contrario
"""

def sao_multiplicavees (matriz_1, matriz_2):

    colunas_1 = len (matriz_1 [0])

    linhas_2 = len (matriz_2) 

    if colunas_1 == linhas_2:
        return True
    
    else:
        return False
    
#   #   #
##  ##  ##
### ### ###