#Vectores - array - arreglo unidemensional - lista


"""
    "" - si pones dobles comillas significa que es un string
    [] - corchetes
    {} - llaves
    () - parentesis
    funciones - return 
    len() - funcion para recuperar la longitud de algo(arreglo)
    get - nomenclatura, o prefijo para el nombre de una función    
    [0] para acceder al primer elemento utilizamos el indice 0 en un arreglo
    arreglo[] - van a poder acceder a ese elemento por medio de indices 
"""

def imprimir_elementos_numeros():    
    numeros = [10, 20, 30, 40, 50]
    primer_elemento = numeros[0]
    ultimo_elemento = get_ultimo_elemento(numeros)

    imprime_elementos_posiciones("numeros", ultimo_elemento, primer_elemento)

#segundo ejemplo de arreglo - vectores - arreglo unidimensional -lista
def imprimir_elementos_dias():    
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
    primer_elemento_dias = dias[0]
    u_dias =  get_ultimo_elemento(dias)

    imprime_elementos_posiciones("dias", u_dias, primer_elemento_dias)

def imprime_elementos_posiciones(nombre_arreglo, u_elemento, p_elemento):
    print(f"el ultimo elemento del arreglo de {nombre_arreglo} es: {u_elemento}  \n  el primer elemento es {p_elemento}")

def get_ultimo_indice(arreglo_param):
    return len(arreglo_param) -1

def get_ultimo_elemento(arreglo_param):
     return arreglo_param[get_ultimo_indice(arreglo_param)]

imprimir_elementos_dias()
print("AQUI EMPIEZA EL OTRO ARREGLO \n")
imprimir_elementos_numeros()

###EJERCIO Arreglo - lista -array
### hagan un arreglo del 1 - 10
### otro arreglo de vocales
### que sean funciones y que las manden a llamar, reutilicen las funciones que ya tenemos 

#Repaso de for - bucle 

vocales = ["a", "e", "i", "o", "u"]
abecedario = ["a", "b"]
for letra in abecedario:
    print(f"cada letra es:{letra}")

for vocal in vocales:
    print(vocal)


# Para escribir una clase necesitamos mandar a llamar la palbra reservada class el nombre de dicha clase:
# contructor - ctor -  __init__
class Auto_sin_ctor:
    #atributos
    color = "rojo"
    modelo = "tsuru"
    
auto_sin_ctor = Auto_sin_ctor
print(auto_sin_ctor.color)

class Auto:     
    esta_encendido = False
    #metodo - comportamiento
    def __init__(self, modelo_instancia, color_instancia):
        self.modelo = modelo_instancia
        self.color = color_instancia
        # self.esta_encendido = False        
        pass

    def set_encender_auto(self):
        self.esta_encendido = True
    
    def apagar_auto(self):
        self.esta_encendido = False

    def get_esta_encendido(self):
        if self.esta_encendido:
            print(f"el auto {self.modelo} esta encendido")
        else:
            print(f"el auto {self.modelo} esta apagado")

objeto_auto_rojo = Auto("tsuru", "red")
objeto_auto_amarillo = Auto("mustang", "amarillo")
objeto_auto_azul = Auto("mustang", "azul")
# print(f"{objeto_auto.modelo} , {objeto_auto.color}")    
# objeto_auto.encender_auto()
print(f"{objeto_auto_rojo.modelo} , {objeto_auto_rojo.color}")    
print(f"{objeto_auto_amarillo.modelo} , {objeto_auto_amarillo.color}")    
print(f"{objeto_auto_azul.modelo} , {objeto_auto_azul.color}")  

objeto_auto_rojo.set_encender_auto()
objeto_auto_rojo.apagar_auto()
objeto_auto_rojo.get_esta_encendido()


##ejemplo de una clase Usuario
class Usuario:
    def __init__(self, user_name, email):
        self.username = user_name
        self.email = email
        # pass - markup - marcador aqui debería de haber código 

instancia_clase_usuario = Usuario("juanito", "test@gmail.com")
print(instancia_clase_usuario.username)

# Realicen un ejercicio con una clase que se llame admin, que tenga 3 atributos nombre, apellido, email
class Admin:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.__id = 1 # __ con doble guion bajo significa que es privada esa propiedad y que no puede ser alcanzable por otras intancias        
        self.incrementaId()

    def get_fullname(self):
        return f"Bienvenido admin:{self.email} - {self.nombre} {self.apellido}"
    
    #ejemplo de destructor __del__ el destructor se ejecuta automaticamente por el garbage collector - pero pueden mandar a llamarlo de manera explicita
    def __del__(self):
        print(f"la instancia de esta clase de: {self.nombre} ha finalizdo, destruiremos esta instacia del objeto")

    def incrementaId(self):
        for n in range(0, 10):
            self.__id +=1        
        print(self.__id) 

instancia_clase_admin = Admin("Juanito", "escarcha", "email@email.com")
print(instancia_clase_admin.get_fullname())
# del(instancia_clase_admin)

# print(instancia_clase_admin.__id)
