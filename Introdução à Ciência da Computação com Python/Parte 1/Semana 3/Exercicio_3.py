"""
Neste exercicio vamos receber um numero inteiro e imprimir Buzz se o numero for divisivel por 5
e o proprio numero se não for
"""

def main ():

    numero = int (input ("Digite um numero inteiro: "))

    if numero % 5 == 0:
        print ("Buzz")
    
    else:
        print (numero)
main()

#   #   #
##  ##  ##
### ### ###