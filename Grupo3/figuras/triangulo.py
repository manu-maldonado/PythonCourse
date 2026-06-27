from figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triangulo")
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura) / 2