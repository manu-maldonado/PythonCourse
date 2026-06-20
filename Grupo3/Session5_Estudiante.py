class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.califaciones = []
    
    def agregar_califaciones(self, calificacion):
        if 0 < calificacion and calificacion <= 100:
            self.califaciones.append(calificacion)

        else: 
            return "calificacion invalida"
        
    def get_promedio(self):
        if len(self.califaciones) == 0:
            return 0
        
        total_calificaciones = 0
        for calificacion in self.califaciones:
            total_calificaciones += calificacion

        numero_elementos = len(self.califaciones)

        return total_calificaciones / numero_elementos
    
    def mostrar_informacion(self):        
        return f"Información del estudiante Nombre: {self.nombre} \n Edad: {self.edad} \n promedio: {self.get_promedio():.2f}"


#instancia de un objeto
estudiante_a = Estudiante("Ferny", 36)
estudiante_a.agregar_califaciones(90)
estudiante_a.agregar_califaciones(80)
estudiante_a.agregar_califaciones(75)

print(estudiante_a.mostrar_informacion())

