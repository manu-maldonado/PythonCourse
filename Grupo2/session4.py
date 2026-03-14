"""
 existen dos manera de definir nomenclaturas de funciones: 
  Get -> significa que mediante una funcion nos va a retornar un valor
    cuando ustedes definan una fuuncion con parametros de entrada, lo puede conocer como 'argumentos'
  Set -> .... no nos va a retornar ningun valor - procedimiento 
"""

nombre_grupo = "the best"
#Ejemplo de Get funcion sin parametros pero esta retornando algo utilizamos return
def get_hello_world():
    message_custom = f"hola mundo, hola grupo: {nombre_grupo}"
    return message_custom

# print(get_hello_world())


#Ejemplo de una funcion como Get con parametros - significa que argumentos voy a recibir como variable
def get_hello_param(name, is_admin, nivel_usuario , message):
    message_custom = f"hola {name}, hola grupo: {nombre_grupo} {is_admin}-{message}:{nivel_usuario}"
    return message_custom

# funcion que no retorna nada pero hace cosas internas - sean calculos sean mensajes, tracking como si fuera de tipo SET
# salto de linea \n
def set_hello(saludo, flag, edad):
    message_custom = f"{saludo} \n Juan \n bienvenido {flag} {edad}"
    message_custom += "no olvides que se cierra tu sesion en 10 seg"
    print(message_custom)
    print("este print es independiente de otras cosas no hay que confudirlo con un return")
# print(get_hello_param(input("ingresa el nombre"), True, 10, "test"))

set_hello("Hola", True, 7)

def set_hello_param(name, edad):
    message_custom = f"hola {name} es un integrante del curso"    
    print(message_custom)
    edad += 10
    print(edad)

mensaje_final = get_hello_param(("Test"), True, 10, "test")
print(mensaje_final)
# set_hello_param(input("ingresa el nombre"), 1)    


""" Ejemplos para identificar porque se conoce como procedimiento o funciones, 
    o lo que vimos arriba simplemente utilizando nomenclaturas get => return, set si solo operaciones conjunto de intrucciones etc.

    OJO es para enriquecer o ser mas descriptivos los nombres de sus funciones,
     NO ES REQUERIDO que le agreguen get, set es opcional.
       si a ustedes les queda mas claro 
    como "funcion" quien retorna valor, y "procedimiento" a las que no retornan un valor esta bien.
"""
def operacion_math(operator, valor_a, valor_b):    
    #dado un operator ustedes haran el calculo 
    resultado = 0
    if operator == "+":        
        resultado = valor_a + valor_b
        # return resultado        
        # return valor_a + valor_b        
    elif operator == "-":        
        return valor_a - valor_b        
    elif operator == "*":        
        resultado = valor_a * valor_b
    else:
        resultado = 0

    return resultado

def calculadora_simple(str_valor, str_valor_b, operador):
    set_imprimir_resultado(operacion_math(operador, float(str_valor), float(str_valor_b)))

def get_calculadora_simple(valor_a, valor_b):
    return valor_a * valor_b

# = asignacion
# == comparacion
### suma , resta, multiplicacion

def set_imprimir_resultado(total):
    print(f"El resultado total de la operación es: {total}")          

# ejercicio utilizando una funcion / procedimiento que no retorna nada pero que hace calculos dentro
# print(calculadora_simple(input("ingresa el valor de a"), input("ingresa el valor de b"), input("ingresa el operador deseado") ))
# print(get_calculadora_simple(3, 5 ))

# Por Valor - Inmutable - porque si quieren veanlo porque trabaja sobre la copia
# variables/ parametros inmutables son todos aquellos que sean de tipo primitivo (bool, string, int, float)
nombre = "Juan"

def set_modifica_usuario(nombre):
    nombre = f"nuevoNombre {nombre}"
    print(f"Dentro de la funcion toma el argumento o el parametro de este alcance/scope{nombre}")

set_modifica_usuario("Nombredesdellamadademetodo")
print(f"fuera de la funcion, nombre es un parametro inmutable")


#POR referencia - Mutable - y trabaja sobre la referencia del objeto en este caso array
# variables / parametros mutables son lo que pertencen a list, dict, objetos
lista_canciones = ["tons que mami" , "mi credo", "azul", "uprising"]
def get_last_element():
    return lista_canciones[len(lista_canciones)-1]

def set_modifica_canciones():
    lista_canciones.append("aline")
    print(f"imprime las canciones acumuladas, dentro de esta funcion. {get_last_element()}")

set_modifica_canciones()
print(f"imprime la ultima cancion {get_last_element()}")


##Valor de retorno multiple - utilizando tuplas
def operaciones(a, b):
    suma = a + b  
    resta = a - b
    mult = a * b
    return suma, resta, mult

# def operaciones(a, b):
#     suma = a + b
#     return suma

# def operaciones(a, b):    
#     return a - b

# sum = operaciones(10,7)
# r = operaciones(10,7) 
s , r , m = operaciones(4,6)


def metodo_return_inmediatamente(numero):    
    if numero == 5:        
        return "No califica para las siguiente operaciones"
    
    message_final = "Felicidad aprobaste el curso \n te gustaria tomar otro curso"    
    return message_final
    
print(metodo_return_inmediatamente(6))


print(f"el valor desde una tupla de operaciones para la suma es: {s} \n y la resta es: {r} \n la multiplicacion es: {m}")


"""Ejemplos pilas(stack) LIFO Last in, first out, tabla de equivalenias en python
# push - append - agregar elemento
# pop - pop - sacar/eliminar el ultimo elemento de una pila 
# peek - len(coleccion/array)-1 - ver el ultimo elemento sin eliminar
"""
stack_lifo_example = ["enero", "febrero", "marzo"]

stack_lifo_example.append("abril")

def get_last_element(coleccion):
    return coleccion[len(coleccion)-1]

print(f"el ultimo elemento es {get_last_element(stack_lifo_example)}")

stack_lifo_example.pop()
print(f"el ultimo elemento despues del pop es {get_last_element(stack_lifo_example)}")

"""
 Queue - Colas - FIFO First in , First out
 enqueue - append
 eliminar - popleft - va a sacar al primer elemento
 importante deben de utilizar una libreria de python from collections import deque
"""

from collections import deque
queue_dias = deque()

queue_dias.append("Lunes")
queue_dias.append("Martes")
queue_dias.append("Miercoles")
queue_dias.append("Jueves")
queue_dias.append("Viernes")
print(queue_dias[0])

primer_elemento = queue_dias.popleft()
print(f"el primer elemento que quito fue: {primer_elemento}")
print(queue_dias[0])
primer_elemento = queue_dias.popleft()
print(primer_elemento)

# retornar el primer elemento y el ultimo elemento para 
#los meses utilizando FIFO y 
#días utilizando LIFO

def get_last_indice(collecion):
    return len(collecion)-1

# print(queue_dias[get_last_indice(queue_dias)])
print(f"recupera el primer indice {queue_dias[0]}")