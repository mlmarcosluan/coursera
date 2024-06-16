def primeiro_lex (lista):

    menor_lex = lista[0][0]

    primeiro = lista[0]

    for str in range (len (lista)):
        lex = lista[str][0]
        
        if ord (lex) < ord (menor_lex):
            menor_lex = lista[str][0]
            primeiro = lista[str]

    return primeiro

#   #   #
##  ##  ##
### ### ###