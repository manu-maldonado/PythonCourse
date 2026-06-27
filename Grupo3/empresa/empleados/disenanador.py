# empleados/disenador.py
from .empleado import Empleado

class Disenador(Empleado):
    def __init__(self, nombre, apellido, fecha_contratacion, salario_base,
                 especialidad, herramientas=None):
        super().__init__(nombre, apellido, fecha_contratacion, salario_base)
        self.especialidad = especialidad
        self.herramientas = herramientas if herramientas else []
        self._portafolio = []
    
    def agregar_proyecto_portafolio(self, proyecto_nombre):
        self._portafolio.append(proyecto_nombre)
    
    def calcular_salario(self):
        salario = self._salario_base
        salario += len(self._portafolio) * 500
        salario += len(self.herramientas) * 1000
        return salario
    
    def obtener_rol(self):
        return f"Diseñador {self.especialidad}"
    
    def disenar(self, concepto):
        return f"{self.nombre} está diseñando: {concepto} usando {', '.join(self.herramientas[:2])}"
    
    def __str__(self):
        return f"{super().__str__()} | Especialidad: {self.especialidad}"