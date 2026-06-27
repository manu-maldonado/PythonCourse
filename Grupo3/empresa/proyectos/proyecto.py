# proyectos/proyecto.py
from datetime import datetime

class Proyecto:
    def __init__(self, nombre, fecha_inicio, fecha_fin_estimada):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_estimada = fecha_fin_estimada
        self._miembros = []
        self._tareas = {}
        self._completado = False
    
    def obtener_tipo(self):
        raise NotImplementedError("Las subclases deben implementar obtener_tipo()")
    
    def agregar_miembro(self, empleado):
        if empleado not in self._miembros:
            self._miembros.append(empleado)
    
    def agregar_tarea(self, nombre_tarea, responsable=None):
        self._tareas[nombre_tarea] = {
            'responsable': responsable,
            'completada': False
        }
    
    def marcar_tarea_completada(self, nombre_tarea):
        if nombre_tarea in self._tareas:
            self._tareas[nombre_tarea]['completada'] = True
            if all(tarea['completada'] for tarea in self._tareas.values()):
                self._completado = True
    
    def obtener_progreso(self):
        if not self._tareas:
            return 0
        completadas = sum(1 for t in self._tareas.values() if t['completada'])
        return (completadas / len(self._tareas)) * 100
    
    def __str__(self):
        estado = "✅ Completado" if self._completado else f"🔄 {self.obtener_progreso():.1f}% completado"
        return f"Proyecto: {self.nombre} ({self.obtener_tipo()}) - {estado}"