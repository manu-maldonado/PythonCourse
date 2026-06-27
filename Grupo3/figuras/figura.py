class Figura:
    def __init__(self, nombre):
        self.nombre = nombre        

    def area(self):
        raise NotImplementedError("Las subclases deben de ser implementadas area()")
        