from circulo import Circulo
from triangulo import Triangulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo

def mostrar_info(figura):
    print(figura)
    print(f"Area de {figura.area()}")

def main():
    print("Implmentacion de herencia poliformismo: de figura geometricas")

    instacia_objecto_circulo = Circulo(5)
    instacia_objecto_cuadrado = Cuadrado(10)
    instacia_objecto_triangulo = Triangulo(4,7)
    instacia_objecto_rectangulo = Rectangulo(4,7)

    # mostrar_info(instacia_objecto_circulo)
    # mostrar_info(instacia_objecto_cuadrado)
    # mostrar_info(instacia_objecto_triangulo)
    # mostrar_info(instacia_objecto_rectangulo)

    # mostrar cada uno de los responses a los mismos metodos
    figuras = [instacia_objecto_circulo, instacia_objecto_cuadrado, instacia_objecto_triangulo, instacia_objecto_rectangulo]
    for figura in figuras:
        print(f"El area de {figura.nombre} es {figura.area()}")

main()