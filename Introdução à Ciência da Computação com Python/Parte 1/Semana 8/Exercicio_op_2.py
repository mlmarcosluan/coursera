"""
Escreva um programa que recebe uma sequência de números inteiros e imprima todos valores
em ordem inversa
"""

def main ():

    lista = []
    elemento = int (input ("Digite um número: "))
    if elemento != 0:
        lista.append (elemento)

    while elemento != 0:
        elemento = int (input ("Digite um número: "))

        if elemento != 0:
            lista.append (elemento)

    for x in range (len (lista), 0, -1):
        print (lista[x - 1])

main ()

#   #   #
##  ##  ##
### ### ###