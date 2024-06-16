"""
Implemente a função busca (lista, elemento), que busca um determinado elemento em uma lista
e devolve o índice correspondente à posiçao do elemento
"""

def busca (lista, elemento):
    
    elemento_inicial = 0
    elemento_final = len (lista) - 1

    while elemento_inicial <= elemento_final:

        meio = (elemento_inicial + elemento_final) // 2

        print (meio)
        if lista [meio] == elemento:
            return meio
        else:
            if elemento < lista [meio]:
                elemento_final = meio -1
            else:
                elemento_inicial = meio + 1

    return False

#   #   #
##  ##  ##
### ### ###