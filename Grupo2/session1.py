name = "Panchito"
age = 24
isAdmin = True ## = asignación 
## == comparación
##isAdmin == False:  not isAdmin

## Casos para booleanos
if not isAdmin:
    print(f"{name} no tienes permisos de admin")
else:
    print(f"{name} bienvenido admin!")


##casos para enteros
if age == 18: # si se cumple la condicion
    print(f"{name} eres mayor de edad")
elif age <18: # si es menor se cumple la condicion
    print(f"{name} estas muy chavo")
elif age >18: # si las condiciones anteriores no se cumplen entonces evalua la siguiente expresión
    print(f"{name} nombre, ya pasale!")
else:    #si no sucede ningungo de esas condiciones entonces imprime mensaje por default
    print(f"{name} bienvenido admin!")


##casos para strings
if name == "Panchito" and isAdmin and age >= 23:
    print("Hola amigo")
elif name != "Panchito" and name != "":
    print("Tú no eres panchito , quén eres tú y para quien trabajas!")
else:
    print("quién eres tú, cómo te llamas?")
