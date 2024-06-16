"""
Escreva um método semelhantes (triangulo) que recebe um objeto do tipo Triangulo como parâmetro
e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro devolvendo True
ou False
"""

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lados = [a, b, c]
        self.lados.sort ()

    def semelhantes (self, triangulo):
        divisevel = 0
        for l in range (3):
            if self.lados [l] % triangulo.lados [l] == 0:
                divisevel += 1
            if triangulo.lados [l] % self.lados [l] == 0:
                divisevel += 1
        
        if divisevel == 3:
            return True
        elif triangulo.lados == self.lados:
            return True
        else:
            return False

#   #   #
##  ##  ##
### ### ###