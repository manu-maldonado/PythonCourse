#cuenta bancaria 
class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.movimiento = ""

    def depositar(self, cantidad):
        self.saldo += cantidad
        self.movimiento = "deposito"
        return self.saldo

    def retirar(self, cantidad):
        self.saldo -= cantidad
        self.movimiento = "retiro"
        return self.saldo

    def mostrar_saldo(self):
        return f"Tu saldo es: {self.saldo} hiciste un {self.movimiento}"
    

# input_usuario_saldo = int(input("Ingresa la cantidad deseada"))
cuenta_a = Cuenta("Laura Mendoza")

while True:
    input_usuario = input("Ingresa tipo de operacion (r: retirar, d: depositar, .: salir): ")
    if input_usuario == ".":
        print("Gracias por su visita")
        break

    if input_usuario == "r" or input_usuario == "d":
        cantidad = int(input("ingresa la cantidad deseada: "))        
    
        if input_usuario == "r":
            cuenta_a.retirar(cantidad)
        elif input_usuario == "d":
            cuenta_a.depositar(cantidad)    
            
        print(cuenta_a.mostrar_saldo())
    
    else:
      print("Operación no válida. Intenta de nuevo.")
        
    