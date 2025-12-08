from modulo_cocina import recetas, ingredientes
from modulo_clientes import gestion
from modulo_ventas import facturacion, pedidos

import datetime

def main():
    print("Sistema para restaurante")

    #configuracion incial
    #if
    #for - while 
    #corchetes [] - array
    #llaves {} - objetos o diccionarios
    #array[0]
    #len


    print(f"Chef principal {recetas.CHEF_PRINCIPAL}")
    print(f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y')}")
    
    #mostrar recetas disponibles
    print("Recetas Disponibles")

    for receta in recetas.get_listado_recetas():
        detalles = recetas.obtener_receta(receta)
        print(f"{receta}: {detalles['dificultad']} tiempo de preparacion - {detalles['tiempo_de_preparacion']}")

    #crear cliente
    cliente = "Doctor CHapatin"
    if gestion.registrar_cliente(cliente, "12312-121", "chapatin@chapata.com"):
        print(f"cliente registrado exitosamente {cliente}")

    #crear pedido
    orden_platillos = ["mole_poblano" , "tacos_al_pastor"]
    nuevo_pedido = pedidos.crear_pedido(cliente, orden_platillos)
    
    #\n salto de linea
    print(f"\n Pedido creado: {nuevo_pedido}")
    
    
    gestion.actualizar_pedido_cliente(cliente)


    #facturacion
    factura = facturacion.generar_factura(nuevo_pedido)
    print("\n Factura:")
    print(f"Cliente: {cliente}")
    print(f"Platillos: {', '.join(factura['platillo'])}")
    print(f"Factura: Subtotal{factura['subtotal']}")
    print(f"Total{factura['total']}")
    #recuerden si presionan f12 en vs los manda a las referencias orignales

    
main()