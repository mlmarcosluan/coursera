"""
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste númeor na saída
"""

def main ():

    entrada = input ("Digite um número inteiro: ")
    passagens = len (entrada)
    numero = int (entrada)

    n = 0
    while passagens > 0:
        n = n + (numero % 10)
        numero = numero // 10
        passagens = passagens - 1

    print (n)


main ()

#   #   #
##  ##  ##
### ### ###