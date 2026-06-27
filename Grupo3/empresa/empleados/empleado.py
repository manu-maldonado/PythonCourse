# empleados/empleado.py
from datetime import datetime

class Empleado:    
    contador_empleados = 0
    
    def __init__(self, nombre, apellido, fecha_contratacion, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_contratacion = fecha_contratacion
        self._salario_base = salario_base
        self._id = Empleado.contador_empleados
        Empleado.contador_empleados += 1
        self._proyectos_asignados = []
    
    @property
    def id(self):
        return self._id
    
    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salario_base = valor
    
    def calcular_salario(self):
        """Método que debe ser sobrescrito por las subclases"""
        raise NotImplementedError("Las subclases deben implementar calcular_salario()")
    
    def obtener_rol(self):
        """Método que debe ser sobrescrito por las subclases"""
        raise NotImplementedError("Las subclases deben implementar obtener_rol()")
    
    def asignar_proyecto(self, proyecto):
        self._proyectos_asignados.append(proyecto)
        proyecto.agregar_miembro(self)
    
    def obtener_antiguedad(self):
        hoy = datetime.now()
        year = hoy.year - self.fecha_contratacion.year
        if (hoy.month, hoy.day) < (self.fecha_contratacion.month, self.fecha_contratacion.day):
            year -= 1
        return year
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} (ID: {self.id}) - {self.obtener_rol()}"
    
    def __repr__(self):
        return f"<Empleado {self.id}: {self.nombre} {self.apellido}>"