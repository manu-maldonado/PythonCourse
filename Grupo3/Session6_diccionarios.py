# key string: value (de cualquier tipo)

usuario = {
   "id": 21291,
   "nombre": "Ferni",
   "ciudad": "Mexico"
}

print(usuario["nombre"])
print(usuario.get("ciudad"))
print(usuario.get("id"))


#agregar/actualizar valores en un diccionario
usuario["profesion"] = "Ingenieria"
usuario["edad"] = 37

print(f"Antes de eliminar llaves/keys/ propiedades{usuario}")


if "edad" in usuario:
    print("existe esta llave en usuario")
#eliminar elementos 
del usuario["ciudad"]
print(f"Despues de eliminar llaves/keys/ propiedades{usuario}")

if not "ciudad" in usuario:
    print("no existe esta llave en usuario")


for key, value in usuario.items():
    print(key, value)