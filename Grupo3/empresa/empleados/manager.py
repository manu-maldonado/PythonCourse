# empleados/manager.py
from .empleado import Empleado

class Manager(Empleado):
    def __init__(self, nombre, apellido, fecha_contratacion, salario_base,
                 departamento, equipo=None):
        super().__init__(nombre, apellido, fecha_contratacion, salario_base)
        self.departamento = departamento
        self.equipo = equipo if equipo else []
        self._objetivos_trimestrales = []
    
    def agregar_miembro_equipo(self, empleado):
        self.equipo.append(empleado)
    
    def establecer_objetivo(self, objetivo):
        self._objetivos_trimestrales.append(objetivo)
    
    def calcular_salario(self):
        salario = self._salario_base
        salario += len(self.equipo) * 1000
        salario += len(self._objetivos_trimestrales) * 2000
        return salario
    
    def obtener_rol(self):
        return f"Manager de {self.departamento}"
    
    def liderar_reunion(self):
        return f"{self.nombre} está liderando una reunión del departamento {self.departamento}"
    
    def __str__(self):
        return f"{super().__str__()} | Equipo: {len(self.equipo)} miembros"