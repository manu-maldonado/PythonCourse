"""
Como definir una funcion def 
nombre de la funcion ():
podemos pasarle parametros a una funcion 
return - devolver un valor
"""

def suma(valor_a, valor_b):
    return valor_a + valor_b

def multiplicacion(valor_a, valor_b):
    return valor_a * valor_b

def resta(valor_a, valor_b):
    return valor_a - valor_b

def division(valor_a, valor_b):
    # que solo numeros que sean divisibles  != 0
    if valor_b == 0:
        return "Error no se puede dividir"
    else:
        return valor_a / valor_b

def funciones_aritmeticas(a, b, operator):
    temp_a = float(a)
    temp_b = float(b)

    #toma de decisiones / flujos condicionales
    #if elif else 
    if(operator == "+"):
        return suma(temp_a, temp_b)
    elif(operator == "-"):
        return resta(temp_a, temp_b)
    elif(operator == "*"):
        return multiplicacion(temp_a, temp_b)
    elif(operator == "/"):
        return division(temp_a, temp_b)
    else:
        return "operacion no reconocida"


def obtener_operador(operador):
    if operador == "+":
        return "suma"
    elif operador == "-":
        return "resta"
    elif operador == "*":
        return "multiplicación"
    elif operador == "/":
        return "división"
    else:
        return "operador no existente"

def imprimir_resultado(res, operator):
    print(f"El resultado de la {obtener_operador(operator)} es: {res}")

def calculadora(a, b, operator):
    resultado = funciones_aritmeticas(a, b, operator)    
    imprimir_resultado(resultado, operator)

# input_a = input("ingresa el valor de a: \n")
# input_b = input("ingresa el valor de b \n")
# operador = input("ingresa el simbolo de la operacion a realizar: ")

# calculadora(input_a, input_b, operador)


# Sigue con solo dos datos, Hacer una calculadora básica suma, resta , division y multiplicacion 
# if elif elif else
# podrían pasar un parametro extra que se llame operador + , - , * , /

"""
Ejercicio para calculo de areas geometricas basicas
Triangulo, cuadrado, rectangulo

El usuario ingresara que tipo de calculo necesita hacer: 
y los valores necesarios por cada tipo de figura geometrica
Definan unas funciones para el calculo de areas
otra funcion para mostrar los mensajes (solo en esta funcion pueden usar print)
"""

def area_cuadrado(lado):
    return lado * lado

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def calcular_area(tipo):
    if(tipo == "cuadrado"):
        lado_input = float(input("lado: \n"))        
        return area_cuadrado(lado_input)
    elif(tipo == "rectangulo"):
        base_input = float(input("base: \n"))        
        altura_input = float(input("altura: \n"))         
        return area_rectangulo(base_input, altura_input)
    elif(tipo == "triangulo"):
        base_input = float(input("base: \n"))        
        altura_input = float(input("altura: \n"))        
        return area_triangulo(base_input, altura_input)
    else:
        return "tipo invalido para calcular"
    
def mostrar_calculo_area(figura_geometrica):
    calculo_total = calcular_area(figura_geometrica)
        
    print(f"El resultado del area de la figura geometrica:{figura_geometrica} es: {calculo_total}")

#mostrar_calculo_area(input("ingresa el nombre de una figura geometrica \n"))
## inmutables(por valor) vs mutables(referencia)

# no mutable 
def actualizar_x(x):
    x += 90
    print(x)


x = 2
actualizar_x(3)
print(x)

# ejemplo mutable - listas array

def agregar_canciones(lista):
    lista.append('Mañanitas')
    lista.append("Hombre de acción")
    print(lista)

lista_canciones = ["El triste", "Quen pompo"]
agregar_canciones(lista_canciones)
print(lista_canciones)


"""
Return multiples (tuples)
"""

def operaciones(a, b):
    suma = a +b
    resta = a -b
    multiplacion = a * b
    division = a / b

    # return mostrar_message_op("+", suma), mostrar_message_op("-", resta), mostrar_message_op("*", multiplacion), division
    return suma, resta, multiplacion, division, "hola"

s, r, m, d, message = operaciones(1,3)
print(f"el valor de r: {r}, de s:{s}")

def mostrar_message_op(operador, resultado):
        return f"El resultado de la {obtener_operador(operador)} es: {resultado}"


print(operaciones(5, 4))


# Imprimir las areas basicas de figuras geometricas con return multiple (tuples)
def operaciones_geometricas():
    area_cuadrado = calcular_area("cuadrado")
    area_rectangulo = calcular_area("rectangulo")
    area_triangulo = calcular_area("triangulo")

    return area_cuadrado, area_rectangulo, area_triangulo



def calcular_area_harcodeado(tipo):
    if(tipo == "cuadrado"):
        lado_input = 10
        return area_cuadrado(lado_input)
    elif(tipo == "rectangulo"):
        base_input = 9
        altura_input = 7
        return area_rectangulo(base_input, altura_input)
    elif(tipo == "triangulo"):
        base_input = 6
        altura_input = 5
        return area_triangulo(base_input, altura_input)
    else:
        return "tipo invalido para calcular"

print(operaciones_geometricas())



def mostrar_vocales():
    return "a", 42, False, "o", "u"

print(mostrar_vocales())