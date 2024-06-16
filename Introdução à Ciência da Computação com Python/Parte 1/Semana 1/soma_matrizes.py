def soma_matrizes (m1, m2):

    if (dimensoes (m1)) == (dimensoes (m2)):
        linhas, colunas = dimensoes (m1)
        nova_matriz = []

        for i in range (linhas):

            nova_linha = []
            for j in range (colunas):
                nova_linha.append (m1[i][j] + m2[i][j])
            nova_matriz.append (nova_linha)

        return nova_matriz


    else:
        return False

def dimensoes (matriz):

    linhas = len (matriz)
    colunas = len (matriz[0])

    return (linhas, colunas)

#   #   #
##  ##  ##
### ### ###