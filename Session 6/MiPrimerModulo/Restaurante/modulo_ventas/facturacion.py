precios = {
    "mole_poblano": 150,
    "tacos_al_pastor": 80,
    "tacos_de_suadero": 90
}

def calcular_total(platillos):
    sum_precio = 0
    for platillo in platillos:
        sum_precio += precios.get(platillo, 0)
    return sum_precio

def aplicar_impuesto(total, iva = 0.16):
    return total * (1 + iva)

def generar_factura(pedido):
    subtotal = calcular_total(pedido.platillo)
    total = aplicar_impuesto(subtotal)

    factura = {
        "numero_pedido": pedido.numero,
        "cliente": pedido.cliente,
        "platillo": pedido.platillo,
        "subtotal": subtotal,
        "iva": subtotal * 0.16,
        "total": total
    }

    return factura