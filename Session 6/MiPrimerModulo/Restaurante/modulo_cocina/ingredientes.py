_inventario = {
    "chiles":50,
    "maiz": 100,
    "frijol": 75,
    "carne": 30,
    "sal": 20    
}


def verificar_inventario(ingrediente, cantidad_necesaria):
    return _inventario.get(ingrediente, 0) >= cantidad_necesaria

def actualizar_inventario(ingrediente, candidad_usada):
    if(ingrediente in _inventario):
        _inventario[ingrediente] -= candidad_usada
        return True
    return False
        
def get_inventario():
    #obtiene una copia del inventario actual
    return _inventario.copy()    

