"""
Defina a classe Triangulo cujo o construtor (__init__) recebe 3 valores correspontentes aos lados
a, b, c de um triangulo

a classe triângulo deve também possuir o método perimetro, que não recebe nada e devolve um valor
inteiro correspondente ao perímetro do triângulo
"""

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro (self):

        return self.a + self.b + self.c
    
#   #   #
##  ##  ##
### ### ###