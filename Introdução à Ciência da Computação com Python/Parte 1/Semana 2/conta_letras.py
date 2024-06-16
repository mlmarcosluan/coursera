def conta_letras(frase, contar="vogais"):

    lista_palavras = frase.split(" ")
    cont_vogais = 0

    frase_sem_espa = ""
    for i in range (len (lista_palavras)): 
        """ Retorna uma string com todas palavras sem espaços """
        frase_sem_espa += lista_palavras[i] 
    
    for letra in frase_sem_espa:
        if letra == "a":
            cont_vogais += 1
        elif letra == "e":
            cont_vogais += 1
        elif letra == "i":
            cont_vogais += 1
        elif letra == "o":
            cont_vogais += 1
        elif letra == "u":
            cont_vogais += 1

    if contar == "consoantes": # Aqui vamos contar as consoantes
        cont_consoantes = len (frase_sem_espa) - cont_vogais
        return cont_consoantes
        
              
    else: # Aqui vamos contar as vogais
        return cont_vogais

#   #   #
##  ##  ##
### ### ###