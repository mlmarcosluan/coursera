"""
Receba um número inteiro positivo na entrada e imprima os n primieros números ímpares naturais
"""

def main ():

    numero = int (input ("Digite um valor de n: "))

    n = 1
    passagens = 0

    while passagens < numero:
        if n % 2 != 0:
            print (n)
            passagens = passagens + 1
        n = n + 1
        

    
    

main ()

#   #   #
##  ##  ##
### ### ###