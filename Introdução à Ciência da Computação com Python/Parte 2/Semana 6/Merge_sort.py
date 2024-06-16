def merge_sort (lista):

    ### Base da recursão 
    if len (lista) <= 1: # Se a lista tem tamanho menor ou igual a 1
        return lista
    ### Fim da base de recursão 

    meio = len (lista) // 2 # define o meio como a divisão inteira do tamanho da lista

    lado_esquerdo = merge_sort (lista[: meio]) # o lado esquerdo da lista é do inicio da lista até o meio - 1
    lado_direito = merge_sort (lista[meio: ]) # o lado direito da lista é do meio - 1 até o final da lista
    
    return merge (lado_esquerdo, lado_direito) # chama a função merge que intercala os lados esquerdo e direito

def merge (lado_esquerdo, lado_direito):

    ### Base da recursão 
    if not lado_esquerdo: # se o lado esquerdo é uma lista vazia
        return lado_direito
    if not lado_direito: # se o lado direito é uma lista vazia
        return lado_esquerdo
    ### Fim da base de recursão 

    if lado_esquerdo[0] < lado_direito[0]: # qual primeiro elemento de cada lado é menor
        return [lado_esquerdo[0]] + merge (lado_esquerdo[1:], lado_direito)
    """retorna uma lista com o primeiro elemento do lado esquerdo + uma a lista intercalada da sublista do 
    lado esquerdo com o lado direito"""

    # se o priemiro do lado direito é menor que o primeiro elemento do lado esquerdo
    return [lado_direito[0]] + merge (lado_esquerdo, lado_direito[1:])
    """retorna uma lista com o primeiro elemento do lado direito com + uma lista intercalado da sublista do
    lado direito com o lado esquerdo"""
    
    
#    #    #
##   ##   ##
###  ###  ###