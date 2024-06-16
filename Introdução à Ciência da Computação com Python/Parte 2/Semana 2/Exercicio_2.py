"""
Escreva uma função menor_nome que recebe como parâmetro uma lista de strings com nomes e devolve o nome mais curto
"""

def menor_nome (lista_nomes):

    primeiro_nome = lista_nomes [0].strip ().lower ()

    nome_menor = primeiro_nome
    caracter_nome_menor = len (nome_menor)

    for nome in lista_nomes:
        
        nome_atual = nome.strip ().lower ()
        caracter_nome_atual = len (nome_atual)

        if caracter_nome_atual < caracter_nome_menor:
            nome_menor = nome_atual
            caracter_nome_menor = len (nome_atual)



        
    return nome_menor.capitalize ()

#   #   #
##  ##  ##
### ### ###