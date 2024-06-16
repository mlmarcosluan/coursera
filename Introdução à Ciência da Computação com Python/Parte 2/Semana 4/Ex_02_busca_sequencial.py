"""
Implemente a função busca (lista, elemento) que busca um determinado elemento em uma lista e devolve
o índice correspondente à posição do elemento encontrado
"""

def busca (lista, elemento):

    for i in range (len (lista)):

        if elemento == lista [i]:
            return i
        
    return False

#   #   #
##  ##  ##
### ### ###