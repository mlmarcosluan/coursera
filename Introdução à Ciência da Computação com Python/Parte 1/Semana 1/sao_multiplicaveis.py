def dimensoes (matriz):

    linhas = len (matriz)
    colunas = len (matriz [0])

    return linhas, colunas

def sao_multiplicaveis (m1, m2):

    linhas_m1, colunas_m1 = dimensoes (m1)
    linhas_m2, colunas_m2 = dimensoes (m2)

    if colunas_m1 == linhas_m2:
        return True

    else:
        return False

#   #   #
##  ##  ##
### ### ###