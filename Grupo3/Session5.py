#LIFO Stack 
# definen esto parecido a un arreglo []

first_stack = []

#agregarle un siguiente elementos 
first_stack.append("b")

first_stack.append("c")

#peek
# print(first_stack[-1])

# print(first_stack.pop())
# print(first_stack)


# para importar librerias en python necesitan utilizar from collection  import  - alias deque

from collections import deque

first_fifo = deque()
first_fifo.appendleft("a")
first_fifo.append("b")

print(first_fifo)


#Programacion Orientada a objetos
class Auto:
    # color , year, marca, modelo así podemos asignar atributos a una clase
    def __init__(self, color, year, marca, modelo):
        if color == "":
            self.color = "negro"
        else:
            self.color = color
        self.year = year
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    #metodos - func
    def encender(self):
        self.encendido = True
        print("esta encendido el auto")

    def apagar(self):
        self.encendido = False
        print("esta apagado el auto")
    
    def esta_encedido(self):
        return self.encendido
    
    def get_informacion_general(self):
        return(f"El auto de la marca {self.marca} es {self.color} del año {self.year}")


#instancia de un objeto - implementacion 
auto_1 = Auto("", 2020, "mazda", "2020 mamalon")
auto_2 = Auto("gris", 2025, "toyota", "yaris")
auto_3 = Auto("rojo", 2026, "vw", "virtus")
# Auto auto = new Auto()

print(auto_1.get_informacion_general())
auto_1.encender()
print(auto_1.esta_encedido())
auto_1.apagar()
print(auto_1.esta_encedido())

print(auto_2.get_informacion_general())
print(auto_3.get_informacion_general())


class Pelicula:
    #ctor clase
    def __init__(self, nombre, genero, clasificacion, year):
        self.nombre = nombre
        self.genero = genero
        self.clasificacion = clasificacion
        self.year = year

    def mostrar_informacion(self):
        return f"{self.nombre} de clasificacion: {self.clasificacion}, fue lanzada el año {self.year}" 
    
    def get_genero(self):
        return self.genero
    
#instancia de un objeto - implentacion 
pelicula_a = Pelicula("La vida es bella", "drama", "B", 1997)
pelicula_b = Pelicula("La bella y la bestia", "infantil", "A", 1991)
pelicula_c = Pelicula("Rocky IV", "accion", "B", 1985)

print(pelicula_a.mostrar_informacion())
print(pelicula_b.mostrar_informacion())
print(pelicula_c.mostrar_informacion())


#clase base - herencia - un nuevo tipo
class Animal:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    #metodo abstracto
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Wow wow!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"
    
class Pato(Animal):
    def hacer_sonido(self):
        return "cuak cuak"
    

animales = [Perro("Tobby", "gris"), Gato("Chispita", "amarillo"), Perro("Chispa", "blanco"), Pato("Donald", "blanco")]
for animal in animales:
    print(f"Animal: se llama:{animal.nombre} {animal.hacer_sonido()}")


