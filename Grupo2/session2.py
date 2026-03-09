# #Tipos de primitivos con numeros
# #INT
# # [] - corchetes ,  son utilizados para arreglos
# # {} llaves  son utilizadas para objetos, reemplazar valores
# # () parentesis significa que vamos agrupar, o son utilizados para igresar parametros a una funcion
# # |

# PI = 3.1416
# GRAVEDAD = 9.8
# VELOCIDAD_LUZ = 299792458
# RADIO = 2222
# age = 0
# year = 0
# childs = 0
# persons = 0

# print(f"la edad de Juan cuando nacio: {age} ")

# childs = 5
# persons =3
# age = 19

# print("la edad de Juan cuando nacio: " + str(age))
# print(f"la edad de Juan cuando nacio: {age}")

# formatStringJuan = f"la edad de Juan cuando nacio: {age} "



# ### Float 
# total = 12.23
# print(f"el valor total es: {total}")

# name = "Jose"

# print(type(name))
# print(type(age))
# print(type(total))



# ## Ejemplo con strings con comillas simples y dobles
# ## " comilla doble
# ## ' comilla simple
# ## estructura o sintaxis de format string en python f""


# nameSimple = 'Jane'
# nameDouble = "Panfilo"

# print(f"ejemplo con comillas simples: {nameSimple}")
# print(f"ejemplo con comillas dobles: {nameDouble}")

# print(f'ejemplo con comillas simples:  {nameSimple} \n \t ejemplo con comillas dobles: {nameDouble} \n \\ la edad es {age}')

# # comentarios simples
# """
#     comentarios multipleslineas, multilineas 
#     para ejemplos con multiples lineas necesitamos utilizar triple doble comillas 
#     para apertura y para cierre.
#     Ejemplos para bool - booleanos

#     true/false
# """

# isUser = False
# hasLibrarian = True
# isPremiumUser = False
# valA = 5
# valB = 3

# print(valA > valB)
# print(valA >= valB) #mayor o igual OR valA > valB OR valA == valB
# print(valA == valB)
# print(valA != valB)
# print(not valA == valB)
# print(isUser)

# has_librarian = False
# Edad = 12
# edad = 19
# totalVentas = 12

# # valA == 8 comparando un valor
# # = asignaria un valor

# radio = 5
# area = PI * radio ** 2
# print(round(area, 2))  # 78.54


# result_without_p = 5 +3 *2
# result  = (5+3) *2

# print(f"el resultado sin parentesis {result_without_p} \n el resultado agrupado o por jeraquia: {result}")
# print(result_without_p)
# print(result)
# print("el resulta es", result_without_p, "resuldado agrupado", result)


# # input() vamos a poder recibir valores de lado del usuario como string
# str_age_input = input("Ingresa la edad del usuario:")
# print(type(str_age_input))
# age = int(str_age_input) #hacemos una conversion a int

# print(type(age))

# print(f"el valor ingresado por el usuario es: {age}")


# """
#     cls - para limpiar consola
#     shortcut ctrl +k + c -> comenta el codigo seleccionado
#     shortcut ctrl +k + u -> descomenta el codigo seleccionado

#     Ejercicios: Calculao de un rectangulo
#     operadores * - + /
#     para leer de consola usen input
#     conviertan a float base y la altura
#     Ejemplo calculo de area de un rectangulo
#     INICIO
#         LEER base
#         leer altura
#         Calculo del area base*altura
#         Print del area
#     FINAL
# """

# base = input("Ingresa el valor de base: ")
# altura = float(input("Ingresa el valor de altura: "))
# area = base * altura

# print(area)

### Calcular el area de un cuadrado
### Calcular el area de triangulo

# Para que puedan definir una función deben de usar la palabra reservada def
def calculateArea(base_str, altura_str):
    area = float(base_str) * float(altura_str)
    print("")
    return area

# base_str_input = input("ingresa el valor de la base")
# altura_str_input = input("ingresa el valor de la altura")

S

def getHelloWorld():
    return "Hola Mundo"

print(getHelloWorld())