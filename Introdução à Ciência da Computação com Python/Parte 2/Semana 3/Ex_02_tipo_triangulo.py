"""
Na classe triângulo no exercicio 1, escreva um metodo tipo_lado () que devolve uma string dizendo
se o triângulo é:
isóceles (dois lados iguais)
equilátero (todos os lados iguais)
escaleno (todos os lados diferentes)
"""

class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro (self):

        return self.a + self.b + self.c
    
    def tipo_lado (self):
        if self.a == self.b and self.b == self.c: # Todos os lados iguais
            return "equilátero"
        
        if self.a == self.b and self.a != self.c: # Dois lados iguais
            return "isóceles"
        
        if self.a == self.c and self.a != self.b: # Dois lados iguais
            return "isóceles"
        
        if self.b == self.c and self.a != self.a: # Dois lados iguais
            return "isóceles"
        
        if self.a != self.b and self.b != self.c: # Todos os lados diferentes
            return "escaleno"
        
#   #   #
##  ##  ##
### ### ###