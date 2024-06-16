"""
Neste exercicio vamos receber um numero inteiro e imprimir FizzBuzz se o numero for divisivel
por 3 e por 5, caso contrario imprima o mesmo numero
"""

def main ():

    numero = int (input ("Digite um numero inteiro: "))

    if numero % 3 == 0 and numero % 5 == 0:
        print ("FizzBuzz")

    else:
        print (numero)

main () 