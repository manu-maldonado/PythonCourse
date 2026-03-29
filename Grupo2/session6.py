#POO - Programacion orientada a objetos
# definir en POO un objecto es con una clase 
class Producto:
    def __init__(self, contador):
        # definimos atributo
        self.contador = contador        
        self.incrementa_contador()        
    
    def incrementa_contador(self):
        self.contador +=1              
    
    def get_obtener_contador(self):
        return self.contador # devuelve valor         
                     
# y para utilizar acceder o llamar a esa clase - lo vamos a conocer como instancia de un objeto
# instanciar una clase 

contador_general = 0
producto_pepsi = Producto(contador_general) #primera instancia
contador_general = producto_pepsi.get_obtener_contador()

producto_sabritas = Producto(contador_general)
contador_general = producto_sabritas.get_obtener_contador()
producto_vitaminas = Producto(contador_general)
contador_general = producto_vitaminas.get_obtener_contador()

print(contador_general)
# print(producto_pepsi.contador)
# print(producto_sabritas.contador)
# print(producto_vitaminas.contador)


# contructor  __init__
# destructor  del 

class ConexionBD:
    def __init__(self):
        print("Conexión establecida")
    def __del__(self):
        print("Conexión fue cerrada")

instancia_conexion_1 = ConexionBD()
instancia_conexion_2 = ConexionBD()        
instancia_conexion_3 = ConexionBD()
instancia_conexion_4 = ConexionBD()

# del instancia_conexion_1
# del instancia_conexion_2
# del instancia_conexion_3
# del instancia_conexion_4


"""
Herencia simple, cuando ustedes quieran heredar a una clase base CLASEHIJA(ELNOMBREDECLASEBASE)
"""

class Animal:
    #constructor
    def __init__(self, nombre):
        #atributo
        self.nombre = nombre        
    
    #metodos - funciones
    def hacer_sonido(self):
        return "sonido generico"
    
    def saludar(self):
        return f"{self.nombre} hace {self.hacer_sonido()}"
    
class Perro(Animal):
    def hacer_sonido(self):
        return "guau guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "miau miau"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "muuhhhh"
    
perro_1 = Perro("Tobby")
print(perro_1.saludar())

perro_2 = Perro("Hatchie")
print(perro_2.saludar())

gato_s = Gato("Oliver")
# print(f"{gato_s.nombre} hace {gato_s.hacer_sonido()}")
print(gato_s.saludar())

vaca_l = Vaca("Lechera")
print(vaca_l.saludar())
#Ejercicio dado un atributo saluda, imprimir un mensaje que diga Tobby hace guau
#f string



"""
Ejemplo multiherencia o herencia multiple
"""

class Volador:
    def volar(self):
        return "Esta volando"
    
class Nadador:
    def nadar(self):
        return "Esta nadando"

    
class Corredor:
    def correr(self):
        return "Esta corriendo"
    
class Pato(Volador, Nadador, Corredor):
    pass

instancia_pato = Pato()
print(instancia_pato.nadar())
print(instancia_pato.volar())
print(instancia_pato.correr())



class A:
    def __init__(self):
        self.publico = 1,
        self._protegido = 2,
        self.__privado = 3
    
# clase b que hereda de A
class B(A):
    def mostrar(self):
        print(self.publico)

class C(A):
    def mostrar(self):
        print(self._protegido)

class D(A):
    def mostrar(self):
        print(self.__privado)
        
instancia_b = B()
instancia_c = C()

#Esto va a fallar porque es privado y no podemos acceder a ese metodo de manera publica
instancia_d = D()
print(instancia_b.mostrar())
print(instancia_c.mostrar())
# print(instancia_d.mostrar())



"""
Clase sobrecarga 
se emula la sobrecarga con valores por default a sus argumentos - args.*
"""

class Calculadora:
    def suma(self, a, b, c= 0, d = 0):
        return a + b + c + d

instancia_calculadora_dos_args = Calculadora()
print(instancia_calculadora_dos_args.suma(5 , 7))
instancia_calculadora_tres_args = Calculadora()
print(instancia_calculadora_dos_args.suma(5 , 7, 9))

instancia_calculadora_cuatro_args = Calculadora()
print(instancia_calculadora_cuatro_args.suma(5 , 7, 9, 19))



"""
Overrides
"""
class Figuras:
    def calcular_area():
        return 0
    

class Cuadrado(Figuras):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return self.lado1 * self.lado2
    

instancia_cuadrado = Cuadrado(5, 9)
print(instancia_cuadrado.calcular_area())

#calculen el area de un triangulo, rectangulo
#impriman el resultado de cada una de esas instancias


#En programacion al momento de debugear hay un concepto muy importante que se llama 
#breakpoint -punto de interrupción

"""
Try Except - manejo de excepciones
"""
try:
    arregloA = [2,1]

    print(arregloA[4])
except: 
    print("Es un indice inexistente")


try:
    arregloB = [2,1]

    print(arregloB[4])
except Exception as ex: 
    print(f"Es un indice inexistente {ex}")



"""
Ejemplo diccionario 

"""

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Mexico",    
}


print(persona.get("nombre"))
print(persona.keys())
print(persona.values())



