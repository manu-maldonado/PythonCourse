edad = 12
name = "Juanito Escarcha"
is_active = False
total = 212.2


array_a_strings = ["a", "bn"]
array_b = [12, 9,8]
array_c = [True, False]
array_d = [21.2, 921.89]

#ciclos/ loops para recorrer arreglos (while, for)
# for item in array_a_strings:
#     item 

#return - funciones


#procedimiento - no retorna
def testProc():
    a = 2
    b= 3
    total = a+b
    
    print(total)



#por default una funcion/procedimiento que no retorna nada es None
def siguienteFunct():
    pass

# si retorna algo lo conoceran como funcion
def test():
    return "hola mundo" 

# == compara , = define
def testArguments(a, b, any):
    if a == 10:
        print("")
    elif b == 10 and a!= 12:
        print()
    return

print(testProc())

# valor_a = input("ingresa el valor que desees:")
# valor_a_int = int(valor_a)

#Proteccion de varialbes y metodos 
#private, protected , public si tiene prefijos

class Persona:
    #atributos
    #constructor
    def __init__(self, nombre):
        self.nombre = nombre
    #metodos

p = Persona("Panchito")
print(p.nombre)


#ejemplo de herencia multiple
class Caminador:
    def caminar(self):
        return "caminando"

class Volador:
    def volar(self):
        return "Volando"
    
class Nadador:
    def nadar(self):
        return "nanando"
    
class Cazador:
    def cazar(self):
        return "correle que esta cazando"
    
class Pato(Volador, Nadador, Caminador):
    def __init__(self, nombre):
        self.nombre = nombre
    pass

class Leon(Caminador, Cazador):
    pass

pato = Pato("Panchito")
print(pato.nadar())
print(pato.volar())
print(pato.caminar())


leon = Leon()
leon.cazar()


class A:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada = 3

    def getTest(self):
        print(self.__variable_privada)
   
class B(A):
    def mostrar(self):
        print(self.variable_publica)
        print(self.__variable_privada)



# ejemplo = B()
# ejemplo.mostrar()


class Calculadora:
    def sumar(self, a, b, c= 0, d=0):
        return a + b + c+d
    
instancia_clase_cal = Calculadora()
print(instancia_clase_cal.sumar(1,9,8,7))
print(instancia_clase_cal.sumar(1,9,8))
print(instancia_clase_cal.sumar(1,9))


class Procesador: 
    def procesar(self, dato):
        if isinstance(dato, int):
            return dato * 2
        # elif isinstance(dato, str):
        #     return dato.upper()
        elif isinstance(dato, float):
            return dato *2.36
        elif isinstance(dato, Pato):
            
            return f"{dato.volar()} {dato.nadar()} {dato.nombre} cuack es de tipo pato"
        else:
            return "tipo no implementado o soportado"
        

p = Procesador()
print(p.procesar(5))
print(p.procesar("test"))
print(p.procesar(6.36))
print(p.procesar(pato))
print(p.procesar(Persona("Julito")))
