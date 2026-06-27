from figura import Figura

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Circulo")
        self.radio = radio
        
    def area(self):
        return 3.1416 * self.radio ** 2 