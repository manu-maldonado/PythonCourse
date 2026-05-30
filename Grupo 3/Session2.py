
lado_a = 1 # integer - int
is_valid_user = True # bool - boolean

"""
    recomendaciones - no utilicen simbolos , porcentajes, acentos,ñ u otros cáracteres que no sean 
    del alfabeto en ingles - numeros
    Ejemplos de Tipos primitivos    
"""

#int - enteros
edad = 17
peso = 80
year = 1990

# float 
estatura = 1.80 
numero_calzado = 27.5 
promedio = 9.88


#f-string -  para hacer saltos de linea pueden utilizar un \n
print(f"la edad es:{edad}, su peso es: {peso} \n, tiene un promedio de: {promedio}")

#string puede ser con "" o comillas simples ''
name = "Juanito"
last_name = 'Escarcha'

print(f"el nombre del usuario es:{name} {last_name} \t del año: {year} \\ promedio")

print(type(edad))
print(type(promedio))
print(type(name))

#bool - False - True

nAme =""
NamE = ""
NAME = ""
naME = ""
es_mayor_edad = False

if edad >= 18:
    es_mayor_edad = True

print(es_mayor_edad)


total_ventas = 121
fecha_nacimiento = ""    

#unarios
x = 21
y = 38
y -= x
print(y)

#multiplicaciones  * 
print(x*y)
#division /
print(x/y)
#modulo -remanente -residuo - remaining
print(x % y == 0)

if x == y:
    print("es igual")


#operadores comparacion  != diferente de, ==igual que, <= menor igual a que, >= mayor a igual a que
print(x==y) #false
print(x!=y) #true
print(x<=y) #true
print(x>=y) #false


#precedencia de acción
resultado = 5 + 3 *2 
print(resultado)

resultado = (5 + 3) * 2
print(resultado)

#!true - no sea
#pendiente ejmplos remanentes, modulos 

#ejemplo de not - basicamente si algo era verdadero - lo intepreta como lo contrario que seria falso,  EVALUA DE MANERA INVERSA
print(not edad <= 18)


edad = 18
#if - deben de especificar : en linea de abajo un tabulador
if edad == 18:
    print("apenitas, bienvenido ya puedes votar")
elif edad >= 18:
    print("bienvenido votante")
elif edad == 17:
    print("ya casi falta poco , para que ya puedas votar")
else: #en caso contrario
    print("Todavia no puedes votar, Eres menor de edad, estás muy verde")


#Realizar una calculadora una suma , una resta, multiplicacion y division
#van a agregar una variable que se va a llamara tipo_operacion = "division"


# input es utilizado para recibir parametros de lado de la interaccion con el usuario
# un input retorna un string


tipo_operacion = input("ingresa el tipo de operación: \n")
valor_a = 21
valor_b = 29
message = f"el valor de la operación: {tipo_operacion}"

if(tipo_operacion == "+"):
    print(f"{message} {valor_a + valor_b}")
elif(tipo_operacion == "-"):
    print(f"{message} {valor_a - valor_b}")
elif(tipo_operacion == "*"):
    print(f"{message} {valor_a * valor_b}")
elif(tipo_operacion == "/"):
    print(f"{message} {valor_a / valor_b}")
else:
    print("opción invalida")

#hacer una pequeña logica para poner calificaciones
"""
variables califacion - 70
si es mayor a 90 -> "A++"
si es 89-80 - A
79 - 70 - B
69-60 - C
< 60 - F
"""
temp_value_input = input("Ingresa una calificacion")
int(temp_value_input)

int(input("Ingresa una calificacion"))

type()


#ejemplo parse, convertir string -> int 
edad = int(input("Ingresa una edad"))
print(type(edad))

"""
    funciones - print, input, int, type
    para llamar a una funcion debe de ser el nombre de la funcion - nameFuction() - una funcion tiene parentesis
    f string - {},
    [] arrays
    () - diccionarios

"""

variable_n = "dasdasdasd"
flag_a = True
year = 29


""""Ejercicio calcular el area de figuras geometricas basicas Cuadrado, rectangulo, triangulo
variable, base, altura, lado 
input de lado del usuario tipo_calculo = cuadrado, rectangulo, triangulo
output resultado con print
""""