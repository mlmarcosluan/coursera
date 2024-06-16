"""
Escreva na calsse Triangulo, o métodos retangulo () que devolve True se o triângulo for retângulo
e False caso contrário
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
        
    def retangulo (self):
        if self.a >= self.b and self.a >= self.c: # Lado a é o maior
            if ((self.a) ** 2) == (((self.b) ** 2) + ((self.c) ** 2)): # O triângulo é retângulo
                return True
            else: # O Triângulo não é retângulo
                return False
            
        elif self.b >= self.a and self.b >= self.c: # Lado b é o maior
            if ((self.b) ** 2) == (((self.a) ** 2) + ((self.c) ** 2)): # É retângulo
                return True
            else: # Não é retângulo
                return False
            
        else: # Lado c é o maior
            if ((self.c) ** 2) == (((self.a) ** 2) + ((self.b) ** 2)): # É retângulo
                return True
            else: # Não é retângulo
                return False

#   #   #
##  ##  ##
### ### ###