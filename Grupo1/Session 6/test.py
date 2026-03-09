class Perro:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Método
    def ladrar(instancia_objeto):
        return "¡Guau!"
    
    def dormir(instancia_objeto):
        message = ""
        if instancia_objeto.edad > 5:
           message= "no muerde"
        else:
           message = "no hagas ruido porque el muerde"
        
        return f"{instancia_objeto.nombre} esta durmiendo {message}"

# Crear objeto
mi_perro = Perro("Firulais", 3)
print(mi_perro.ladrar())
mi_perro2 = Perro("James", 12)
print(mi_perro.dormir())
print(mi_perro2.dormir())