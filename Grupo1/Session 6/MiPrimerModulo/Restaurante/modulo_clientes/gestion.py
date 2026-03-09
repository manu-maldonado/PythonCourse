#modulo para gestionar clientes

_clientes = {}
def registrar_cliente(nombre, telefono, correo):
    """Registrar clientes por medio del 
        nombre telefono correo"""
    if nombre in _clientes:
        #ya existe ese cliente
        return False
    _clientes[nombre] = {
        "telefono": telefono,
        "correo": correo,
        "pedidos_totales": 0,
        "cliente_frecuente": False
    }
    
    return True

def actualizar_pedido_cliente(nombre):
    if nombre in _clientes:        
        _clientes[nombre]["pedidos_totales"] += 1
    
    #convertir en cliente frecuente despues 5 pedidos
    if _clientes[nombre]["pedidos_totales"] >= 5:
        _clientes[nombre]["cliente_frecuente"] = True

def test_llamada():
    print("hola david estas llamando a la funcion test llamada de manera independiente")

def es_cliente_frecuente(nombre):
    return _clientes.get(nombre, {}).get("cliente_frecuente", False)

# print(es_cliente_frecuente("james"))
# print(test_llamada())