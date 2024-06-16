"""
Este exercício tem duas partes:

1 - Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um 
espaço) n vezes. Se n não for um inteiro estritamente positivo, a função deve devolver uma string vazia. 
Essa função deve ser implementada utilizando recursão

2 - Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da 
música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve 
devolver uma string vazia. Essa função também deve ser implementada utilizando recursão
"""

def incomodam (n):
    ### Caso base de recursão
    if n < 1:
        return ""
    
    ### Recursão
    return "incomodam " + incomodam (n - 1)

def elefantes (n):
    ### Caso base de recursão
    if n < 1:
        return ""
    
    ### Recursão
    def verso (n):
        if n == 1:
            return "Um elefante incomoda muita gente\n"
        else:
            return str(n) + " elefantes " + incomodam (n) + "muito mais\n" + str(n) + " elefantes incomodam muita gente\n"
        
    if n == 2:
        return verso (1) + verso (2)
    else:
        return elefantes (n - 1) + verso (n)

elefantes (4)

#    #    #
##   ##   ##
###  ###  ###