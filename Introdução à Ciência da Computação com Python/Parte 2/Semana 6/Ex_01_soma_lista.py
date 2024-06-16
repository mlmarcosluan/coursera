"""
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve 
um número inteiro correspondente à soma dos elementos desta lista
"""

def soma_lista (lista):
    ### Base de recursão
    if len (lista) == 1: # Se a lista tem tamanho igual a 1 não precisa fazer nada
        return lista [0]
    
    return lista[0] + soma_lista (lista[1: ]) # Retorna a soma do primeiro elemento com a soma da sublista

#    #    #
##   ##   ##
###  ###  ###