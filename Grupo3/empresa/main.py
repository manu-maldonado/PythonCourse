# main.py
from datetime import datetime
from empleados.desarrollador import Desarrollador
from empleados.manager import Manager
from empleados.disenanador import Disenador
from proyectos.proyecto_software import ProyectoSoftware

def demostrar_polimorfismo(empleados):
    print("\n" + "="*50)
    print("DEMOSTRACIÓN DE POLIMORFISMO")
    print("="*50)
    for emp in empleados:
        print(f"\n {emp}")
        print(f"   Rol: {emp.obtener_rol()}")
        print(f"   Salario: ${emp.calcular_salario():,.2f}")
        print(f"   Antigüedad: {emp.obtener_antiguedad()} años")
        if hasattr(emp, 'escribir_codigo'):
            print(f"  {emp.escribir_codigo()}")
        elif hasattr(emp, 'liderar_reunion'):
            print(f" {emp.liderar_reunion()}")
        elif hasattr(emp, 'disenar'):
            print(f" {emp.disenar('nuevo prototipo')}")

def main():
    print("SISTEMA DE GESTIÓN EMPRESARIAL")
    
    # Crear empleados
    dev1 = Desarrollador("Ana", "García", datetime(2020,5,15), 45000, "Python", 4)
    dev1.agregar_tecnologia("Django")
    dev1.agregar_tecnologia("PostgreSQL")
    
    dev2 = Desarrollador("Carlos", "López", datetime(2022,8,1), 38000, "JavaScript", 2)
    dev2.agregar_tecnologia("React")
    
    manager = Manager("María", "Rodríguez", datetime(2018,3,10), 60000, "Tecnología")
    
    disenador = Disenador("Laura", "Martínez", datetime(2021,6,20), 42000, "UX/UI", ["Figma", "Adobe XD"])
    disenador.agregar_proyecto_portafolio("App Móvil")
    
    # Crear proyecto
    proyecto = ProyectoSoftware(
        "Sistema de Ventas",
        datetime(2024,1,15),
        datetime(2024,6,30),
        "Python",
        "Scrum"
    )
    
    # Asignar al proyecto
    for emp in [dev1, dev2, manager, disenador]:
        proyecto.agregar_miembro(emp)
    
    proyecto.agregar_tarea("Diseñar interfaz", disenador)
    proyecto.agregar_tarea("Desarrollar backend", dev1)
    proyecto.agregar_tarea("Implementar frontend", dev2)
    
    print("\nEMPLEADOS:")
    for emp in [dev1, dev2, manager, disenador]:
        print(emp)
    
    print("\nPROYECTO:")
    print(proyecto)
    
    # Polimorfismo
    demostrar_polimorfismo([dev1, dev2, manager, disenador])
    
    # Avance del proyecto
    proyecto.marcar_tarea_completada("Diseñar interfaz")
    proyecto.marcar_tarea_completada("Desarrollar backend")
    print(f"\nProgreso del proyecto: {proyecto.obtener_progreso():.1f}%")
    print(proyecto.publicar_version("1.0.0"))
    
    print("\n Sistema funcionando!")

main()