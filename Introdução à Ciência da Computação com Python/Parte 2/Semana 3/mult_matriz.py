"""
Neste programa vamos fazer uma função que multiplica matrizes	Contato com a Assistente Social Sonia
"""
def cria_matriz (linhas, colunas):
    """
    Cria uma matriz a partir de um numero de linha e coluna dado e pede cada linha da matriz para o usuario
    linha por linha separados por virgulas
    """
    matriz = []

    for l in range (linhas):

        linha_str = input ("Digite os elementos da linha " + str (l + 1) + " separados por virgulas: ").split  (",")
        linha_int = []
        for c in range (colunas):

            linha_int.append (int (linha_str [c]))
        
        matriz.append (linha_int)
    
    return matriz

def def_matriz ():
    """
    Pede ao usuario o numero de linhas e colunas e chama a função que cria as matrizes
    """

    linhas = int (input ("Digite o número de linhas da matriz: "))
    colunas = int (input ("Digite o número de colunas da matriz: "))

    matriz = cria_matriz (linhas, colunas)

    return matriz

def verifica (matriz_1, matriz_2):
    """
    Para multiplicar duas matrizes o numero de colunas da matriz_1 tem que ser igual ao número de linhas 
    da matriz_2
    """
    colunas_m1 = len (matriz_1 [0])
    linhas_m2 = len (matriz_2)

    if colunas_m1 == linhas_m2:
        return True
    else:
        return False

def multiplica (matriz_1, matriz_2):
    """
    Essa função pega duas matrizes e as multiplica
    """
    linhas_1 = len (matriz_1)
    colunas_1 = len (matriz_1 [0])
    linhas_2 = len (matriz_2)
    colunas_2 = len (matriz_2[0])
    
    matriz_3 = []
    for linha in range (linhas_1):
        matriz_3.append ([])
        for coluna in range (colunas_2):
            matriz_3[linha].append (0)

            for k in range (colunas_1):
                matriz_3[linha][coluna] += matriz_1[linha][k] * matriz_2 [k][coluna]
                 
    return matriz_3

def main ():
    """
    ### Entradas das matrizes ###
    print ("### Criando a primeira matriz ###")
    matriz_1 = def_matriz ()

    print ("### Criando a segunda matriz ###")
    matriz_2 = def_matriz ()

    if verifica (matriz_1, matriz_2): # Se a função verifica retornar True podemos multiplicar as funções
        multiplicacao = multiplica (matriz_1, matriz_2)

    else:
        print ("As matrizes não podem ser multiplicadas")

    """

    matriz_1 = [[2, 3, 1],[-1, 0, 2]]
    matriz_2 = [[1, -2],[0, 5],[4, 1]]

    if verifica (matriz_1, matriz_2): # Se a função verifica retornar True podemos multiplicar as funções
        multiplicacao = multiplica (matriz_1, matriz_2)

    else:
        print ("As matrizes não podem ser multiplicadas")

    print ("Fim do programa")

main ()

#   #   #
##  ##  ##
### ### ###