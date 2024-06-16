"""
Nesse programa vamos criar uma matriz e imprimila de um jeito mais comum de vizualizar matrizes
"""

def imprime_matriz (matriz):
    """
    Função que recebe uma lista de listas (matriz) e imprima do modo usual de ver uma matriz
    """

    linhas = len (matriz)

    for l in range (linhas):

        print (matriz[l])

        

def cria_matriz ():
    """
    Função que ira pedir ao usuario o numero de linha e coluna e cada elemento da matriz
    retornando uma matriz completa
    """

    linhas = int (input ("Digite o numero de linhas da matriz: "))
    colunas = int (input ("Digite o numero de colunas da matriz: "))

    matriz = []

    for l in range (linhas):

        linha = []

        for c in range (colunas):

            print ("Digite o elemento da linha", (l + 1), "e coluna", (c + 1), ":")
            n = int (input ())
            linha.append (n)

        matriz.append (linha)

    return matriz


        

def main ():
    """
    Função principal do programa
    """

    print ("Bem vindo ao programa \"imprima_matriz\" ")

    matriz = cria_matriz ()

    imprime_matriz (matriz)

main ()

#   #   #
##  ##  ##
### ### ###