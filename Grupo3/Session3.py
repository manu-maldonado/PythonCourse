"""Array - arreglos , listas 
{} - llaves
[] - corchetes  -> determinar si es un arreglo, o si quieren recuperan un indice en especifico 
() - parentesis -> funcion
Array empieza siempre desde el indice 0
en un array podemos recuperar el ultimo indice len(tu_arreglo) -1,  slice -1
"""

array_int = [1,2,5,9]
array_string = ["a", "b", "c", "d", "e"]
array_bool = [True, False, False]
array_float = [1.5,2.1,3.8]

print(array_int[3])
print(array_string[3])

last_elem_array_float = len(array_float) -1

print(last_elem_array_float)
print(array_float[last_elem_array_float])


last_elem_array_string = len(array_string) -1
print(array_string[last_elem_array_string])

## ciclos bucles loops
contador = 1
while contador <= 5:
    print(contador)
    # contador = contador +1
    contador += 1

is_active = False 
contador_2 = 0
while not is_active:
    contador_2+=1
    print("no esta activa")
    
    if contador_2 == 3:
        is_active = True
        print("finalmente fue activado")


contador = 0
while contador <= 10:
    if contador == 2:
        print(f"ya encontre el valor, en el indice:{contador}")
        break

    contador+=1
    

""" un nuevo arreglo con las letras de las vocales
tienen un que utilizar un while  
para mostrar cada una de las iteraciones 
print(f"esta es la letra: {valor}")
"""

vocales = ["a","e","i","o","u"]
total_vocales = len(vocales)

while total_vocales == 0:
    valor = vocales[contador]
    print(f"esta es la letra: {valor}")
    contador -= 1 #decrementando o estoy restandole uno
    # contador +=1 #incrementando

#
for vocal in vocales:
    print(f"esta es la letra: {vocal}")


canciones = ["El triste", "corazon partio", "Donde te agarro el temblor", "con el apagon", "la calle de las sirenas"]
for cancion in canciones:
    print(f"el nombre de la cancion es: {cancion}")

# for esta compuesto por un iterador - variable temporal por cada elemento

#ejemplo con rangos 
for i in range(0, 10):
    print(f"valor: {i}")

#ejemplo con rangos 
for i in range(1, 11):
    print(f"valor: {i}")



# #ejemplo con enumare empieza en 0 un enumerate automaticamente
for id, cancion in enumerate(canciones):
    print(f"#{id +1}: {cancion}")


# for range de dos en dos 
for i in range(0, 6, 2):
    print(i)

#format f string {valores}
valor_a = "texto a"
valor_b = "texto b"
print(f"{valor_a}_____::::: {valor_b}")


#ejemplo de uso de indentacion
for id, cancion in enumerate(canciones):
    print(f"#{id +1}: {cancion}")
    for i in range(0, 6, 2):
        print(i)


for id, cancion in enumerate(canciones):
    print(f"#{id +1}: {cancion}")
    if id == 3:
        print(f"hola {id}")

for i in range(0, 6, 2):
    print(i)    


valor_a = "aaaaa"
valor_b = "bbbbb"

print(f"Estos son los valores de:{valor_a}, {valor_b} ")

#Se pueden hacer saltos en una interacion pasando un tercer argumento , como si fuera el multipo de algo
for i in range(0,2, 10):
    print(i)


"""
Dado un arreglo de Cantantes

Deben de imprimir al primer cantante - print(elPrimerCantante)
al ultimo cantante - print(elUltimoCantante)

y deben de imprimir otro mensaje
por cada uno de los cantantes con el siguiente formato 
"{id} Nombre del cantante{cantante}" utilicen range y enumate y for

"""


cantantes = ["Juanga", "ACDC", "Chente", "Muse", "Paul Mchartney", "Cristian Castro", "Pancho Barraza", "Chico che"]
primer_cantante = cantantes[0]
ultimo_cantante = len(cantantes) -1

print(f"el primer cantante es:{primer_cantante} \n el ultimo cantante es:{ultimo_cantante}")

for i in range(len(cantantes)):
    cantante = cantantes[i]
    print(f"{i} Nombre del cantante: {cantante}")


for i, cantanteEnum in enumerate(cantantes):
    print(f"{i} Nombre del cantante: {cantanteEnum}")


array_int = ["a", "e", "i", "o", "u"]
last_elem_array_string = len(array_string) -1
print(array_string[last_elem_array_string])
contador = 0
while contador < len(array_int): 
    contador +=1
    print("esta es la letra {valor}")
    if contador == 4:
        print ("san se acabo")
        break