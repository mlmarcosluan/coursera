"""
Escreva uma função soma_matrizes que recebe como parametro duas matrizes e devolve
uma matriz que representa a soma das duas matrizes caso seja possivel, caso contrario
devolva False
"""

def soma_matrizes (matriz_1, matriz_2):
    """
    Essa função pega duas matrizes, se ambas forem de mesma dimenções ela retorna uma matriz
    com a soma das duas, caso contrario devolve False
    """

    linhas_1 = len (matriz_1)
    colunas_1 = len (matriz_1 [0])

    linhas_2 = len (matriz_2)
    colunas_2 = len (matriz_2 [0])

    if linhas_1 == linhas_2 and colunas_1 == colunas_2: # Podemos fazer as somas das matrizes

        matriz_soma = []
        for l in range (linhas_1):

            linha_soma = []
            for c in range (colunas_1):

                soma = matriz_1[l][c] + matriz_2[l][c]
                linha_soma.append (soma)

            matriz_soma.append (linha_soma)
        
        return matriz_soma

    else: # Não podemos fazer as somas das matrizes
        return False

#   #   #
##  ##  ##
### ### ###