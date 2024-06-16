"""
Repaça o exercício 1 imprimindo os retângulos sem preenchimento
"""

def main ():

    largura = int (input ("digite a largura: "))
    altura = int (input ("digite a altura: "))

    a = 0

    while a < altura:
        l = 0
        while l < largura:
            
            if l == 0:
                print ("#", end = "")
            elif l == (largura - 1):
                print ("#", end = "")
            else:
                if a == 0:
                    print ("#", end = "")
                elif a == (altura - 1):
                    print ("#", end = "")
                else:
                    print (" ", end = "")

            l = l + 1
        print ()
        a = a + 1


            


main ()

#   #   #
##  ##  ##
### ### ###