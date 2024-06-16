def menor_nome (nomes):
    """ Essa função recebe uma lista de nomes e retorna o menor deles, "capilalizado" """
    menor = 9999

    for nome in nomes:
        nome_sem = nome.strip()
        if len (nome_sem) < menor:
            menor = len (nome_sem)
        
    for i in range(len (nomes)):
        nome = nomes[i]
        nome_sem = nome.strip()
        if len (nome_sem) == menor:
            nome_menor = nome_sem
            break

    return nome_menor.capitalize()
    
#   #   #
##  ##  ##
### ### ###
