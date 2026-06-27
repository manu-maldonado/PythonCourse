#sobreescritura (override)

class Figura:
    def area():
        return 0
    # mostrar resultados 



class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado                

    def area(self):
        pass
    

instancia_rectangulo = Rectangulo(8, 16)
print(instancia_rectangulo.area())

#implementar un menu interactivo que cada que presionen un . saldria del menu
# menu ingresa el calculo de la fig geometrica: c = cuadrado, t = triangulo ....