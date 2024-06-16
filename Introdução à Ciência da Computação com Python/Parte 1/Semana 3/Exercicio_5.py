"""
Neste exercicio vamos receber uma sequencia de 3 numeros e imprimir "crescente"
se os numeros estiver em ordem crescente, caso contrario imprimir "não esta em ordem crescente"
"""


def main ():

    numero_1 = int (input ("Digite o primeiro numero: "))
    numero_2 = int (input ("Digite o segundo numero: "))
    numero_3 = int (input ("Digite o terceiro numero: "))

    if numero_1 < numero_2 and numero_2 < numero_3:
        print ("crescente")

    else:
        print ("não está em ordem crescente")
            
main ()