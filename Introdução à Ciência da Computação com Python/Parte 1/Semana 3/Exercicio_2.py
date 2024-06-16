"""
Neste exercicio vamos receber um numero inteiroe imprimir: 
"Fizz" se o número for divisível por 3
caso contrario imprima o mesmo numero que foir dado na entrada
"""

def main():

    numero = int (input ("Digite um numero inteiro: "))

    if numero % 3 == 0: # O numero é divisivel por 3
        print ("Fizz")

    else:
        print (numero)
main()