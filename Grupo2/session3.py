""" con triple comillas dobles 
se utiliza para multiples lineas

example if-elif-else

para llamar una funcion en python necesitamos utilizar el nombre del metodo o funcion y abrir parentesis
para espefiificarle o mandarle, o pasarle valores a una funcion.
"""
# comentario para una sola linea  >, <, >=, <= , == , != ,not 

def obtener_cancion_seleccionada(name):
    return f"la cancion seleccionada es: {name}"

tipo_cliente = "premium"
total_pago = 0
zona = "centro"
descuento = 10
total_descuento = 0
# total_pago = int(input("Ingresa el valor total"))

# if total_pago >= 1000:
#     total_descuento = total_pago * (descuento / 100) 
#     totalPago = total_pago - total_descuento 
# elif total_pago >= 800:
#     print()     
# elif total_pago == 700:
#     if tipo_cliente == "premium":
#         if zona == "centro":
#             print()
#         print()
#     else: 
#         print()
#     print()     
# else:
#     totalPago = total_pago - total_descuento 

# print(f"el total de pago es: {total_pago}, su descuento fue del {descuento}%: {total_descuento}")


""" 
Arreglos - arrays [] - corchetes - para separar o delimitar que es otro elemento en el arreglo
utilizamos 
empezamos desde el indice 0 .... n-1
para poder saber cuál es el último elemento utilizamos len -1
"""
canciones = ["la bikina", "las mañanitas", "No podras", "Donde te agarro el temblor"]
last_element = len(canciones) -1 #3
print(canciones[int(input("agrega un indice"))]) 
print(last_element)

# recorrer del ultimo al primer elemento - LIFO Last First - Ultimo en entrar primero en salir
while last_element >= 0:
    print(obtener_cancion_seleccionada(canciones[last_element])) # {last_element}")
    last_element = last_element -1    
    # last_element -= 1    

# FIFO - First Inp first out, el primero en entrar es el primero en salir 
contador = 0
last_element = len(canciones) -1
while contador <= last_element:
    print(obtener_cancion_seleccionada(canciones[contador])) # {contador}")    
    contador = contador + 1
    # contador += 1

""" Realicen un arreglo de meses e impriman en consola cada de uno de ellos, 
    de las dos maneras con FIFO y con LIFO
"""

#Contador basico utilizando while - orden ascendente
contador_basico = 1
while contador_basico <= 5:
    print(f"Numero del contador es:{contador_basico}")
    contador_basico+=1 # contador_basico = contador_basico + 1

# contador estilo LIFO - descendente
contador_basico = 5
while contador_basico >= 1:
    print(f"Numero del contador es:{contador_basico}")
    contador_basico-=1 # contador_basico = contador_basico + 1


# While con validacion de parametros de entrada
numero = int(input("Ingresa un numero positivo"))

while numero <= 0:
    print("Error: el valor esperado es un número positivo")
    numero = int(input("Ingresa un numero positivo"))

print("Numero valido")

# funcion puede recibir, tener, pasar parametros o puede simplmente no tenerlos
# NOTA: la sintaxis para escribir una funcion es def nombredelafuncion()
def obtener_menu():    
    print("\n === Menu Principal ===")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3. Salir")

def accion_seleccionada(opcion_input):     
    if opcion_input == 1:
        nombre = input("Ingresa tu nombre")
        print(f"hola {nombre}")
    elif opcion_input == 2:
        from datetime import datetime
        print(f"La fecha actual es {datetime.now()}")    
    elif opcion_input == 3:
        print(f"Hasta luego")    
        return True    
    else:
        print("Opcion invalida, intenta nuevamente")   

#Menu interactivo 
def mostrar_menu_interactivo():
    while True:
        print(obtener_menu())
        opcion_seleccionada = int(input("Selecciona una opcion"))
        is_exit = accion_seleccionada(opcion_seleccionada)    
        if is_exit:
            break #break es para salir de un loop - bucle - for o while

# Definir una funcion -> después pueden invocarla, llamara desde otras lineas codigo

## Ejemplos con for
# for con range(inicio, fin, paso- iterador - i)
for index in range (1, 6):
    print(index)

# for para recorrer listas
for cancion in canciones:
    print(obtener_cancion_seleccionada(cancion))

#() significa que estan agrupando operadores logicos , o que estan trabajando con funciones
#[] sig... que estan trabajando con arreglos array, colecciones etc.. y tambien los puedes
# utilizar para recuperar un valor en espec de un arreglo canciones[2] - obtendrias su respectivo valor