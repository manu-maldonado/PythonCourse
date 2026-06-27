from figura import Figura

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def area(self):
        return self.lado * self.lado