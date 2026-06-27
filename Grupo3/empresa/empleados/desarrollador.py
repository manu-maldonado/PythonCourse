# empleados/desarrollador.py
from .empleado import Empleado

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, fecha_contratacion, salario_base,
                 lenguaje_principal, anos_experiencia):
        super().__init__(nombre, apellido, fecha_contratacion, salario_base)
        self.lenguaje_principal = lenguaje_principal
        self.anos_experiencia = anos_experiencia
        self._tecnologias = set()
    
    def agregar_tecnologia(self, tecnologia):
        self._tecnologias.add(tecnologia)
    
    def obtener_tecnologias(self):
        return list(self._tecnologias)
    
    def calcular_salario(self):
        salario = self._salario_base
        salario += self.anos_experiencia * 2000
        salario += min(len(self._tecnologias), 5) * 1500
        return salario
    
    def obtener_rol(self):
        return "Desarrollador de Software"
    
    def escribir_codigo(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje_principal}"
    
    def __str__(self):
        return f"{super().__str__()} | {self.lenguaje_principal} ({self.anos_experiencia} años)"