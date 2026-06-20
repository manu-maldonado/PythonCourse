# pass - to-do not implemented yet aun no tiene nada

class Cantante:
    def __init__(self, nombre, genero, nacionalidad):
        #atributos
        self.nombre = nombre
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.canciones = []

    def agregar_canciones(self, canciones):
        for cancion in canciones:
            self.canciones.append(cancion)        
    
    def eliminar_cancion(self, cancion):
        self.canciones.remove(cancion)                
        return f"la cancion fue borrada {cancion}"

    def buscar_cancion_id(self, id):
        for idx, cancion in enumerate(self.canciones, 1):
            if id == idx:
                return cancion
            
        return "no existe ese Id de canción"

    def mostrar_canciones(self):
        return self.canciones
    
    def actualizar_cancion(self):
        pass


cantante_a = Cantante("LuisMi", "Baladas pop", "Mexicana")
cantante_a.agregar_canciones(["La bikina", "Culpable o no", "Si no supiste amar", "Incondicional", "2 enamorados"])

print(cantante_a.buscar_cancion_id(int(input("ingresa # de canción a buscar:"))))

print(cantante_a.eliminar_cancion("Si no supiste amar"))
print(cantante_a.mostrar_canciones())
# cantante_b = Cantante("Cristian", "Baladas pop", "Mexicana")
# cantante_b.agregar_canciones("Solo", "Azul", "Lloviendo Estrellas", "Yo queria", "Dos amantes")
# cantante_c = Cantante("Chicoche", "Tropical", "Mexicana")
# cantante_c.agregar_canciones("Donde te agarro el temblor", "Quen pompo", "La estaca")