""" modulo paragenerar recetas de cocina 

    vamos a definir unas funciones, un objeto _recetas_secretas     
"""


# corchetes [] - 
# llaves {}
_recetas_secretas = {
    "mole_poblano":{
        "ingredientes": ["chile poblano", "chocolate", "especias"],
        "tiempo_de_preparacion": 321,
        "dificultad": "alta"
    },
    "tacos_al_pastor":{
        "ingredientes": ["cerdo", "piña", "achiote"],
        "tiempo_de_preparacion": 45,
        "dificultad": "media"        
    },
    "tacos_de_suadero":{
        "ingredientes": ["carne", "sal"],
        "tiempo_de_preparacion": 120,
        "dificultad": "media"
    }
}


def obtener_receta(nombre_platillo):
    #obtiene una receta del recetario
    return _recetas_secretas.get(nombre_platillo, "Receta no encontrada")

def get_listado_recetas():
    return list(_recetas_secretas.keys())

# def calcula_tiempo_total(platillos):
#     return sum(_recetas_secretas[platillo]["tiempo_de_preparacion"])


CHEF_PRINCIPAL = "Doña Mari"