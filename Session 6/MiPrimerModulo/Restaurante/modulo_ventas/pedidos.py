"""
módulo para gestionar pedidos
"""

#anotaciones de tipo - typing
from typing import List, Dict, Optional
from datetime import datetime

pedidos_activos = []
_contador_pedidos = 1

class Pedido:
    def __init__(self, cliente, platillos):
        global _contador_pedidos
        self.numero = _contador_pedidos
        self.cliente = cliente
        self.platillo = platillos
        self.estado = "pendiente"
        _contador_pedidos += 1

    def marcar_completado(self):
        return f"Pedido #{self.numero}: {self.cliente} - {self.estado}"

    def _generar_numero(self) -> int:
        #genera un numero de pedido emulando a Autoincrement
        return len(pedidos_activos)+1
    
    def __str__(self):
        return f"El # pedido es {self.numero} - {self.cliente} - estado de la orden: {self.estado}"
def crear_pedido(cliente, platillos):
    pedido = Pedido(cliente, platillos)
    pedidos_activos.append(pedido)
    return pedido

def obtener_pedidos_pendientes():
    pedidos_pendientes = 0
    for pedido in pedidos_activos:
        if pedido.estado == "pendiente":
            pedidos_pendientes += 1
    return pedidos_pendientes
    # return [pedido for in pedidos_activos if pedido.estado== "pending"]