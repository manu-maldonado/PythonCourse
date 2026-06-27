# proyectos/proyecto_software.py
from .proyecto import Proyecto

class ProyectoSoftware(Proyecto):
    def __init__(self, nombre, fecha_inicio, fecha_fin_estimada,
                 lenguaje_principal, metodologia="Agile"):
        super().__init__(nombre, fecha_inicio, fecha_fin_estimada)
        self.lenguaje_principal = lenguaje_principal
        self.metodologia = metodologia
        self._repositorio = f"https://github.com/empresa/{nombre}"
        self._versiones = []
        self._bugs_reportados = []
    
    def obtener_tipo(self):
        return "Desarrollo de Software"
    
    def reportar_bug(self, descripcion, gravedad):
        bug = {'descripcion': descripcion, 'gravedad': gravedad, 'resuelto': False}
        self._bugs_reportados.append(bug)
        return f"Bug reportado: {descripcion} (Gravedad: {gravedad})"
    
    def publicar_version(self, version):
        self._versiones.append(version)
        return f"Versión {version} publicada para {self.nombre}"
    
    def __str__(self):
        return f"{super().__str__()} | Lenguaje: {self.lenguaje_principal} | {len(self._versiones)} versiones"