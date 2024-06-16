"""
Escreva um programa que recebe como entrada dois números inteiros correspindentes à largura e à
altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo
"""

def main ():
    largura = int (input ("digite a largura: "))
    altura = int (input ("digite a altura: "))

    a = 0

    while a < altura:
        l = 0
        while l < largura:
            print ("#", end ="" )
            l = l + 1
        print ()
        a = a + 1

        
main ()

#   #   #
##  ##  ##
### ### ###