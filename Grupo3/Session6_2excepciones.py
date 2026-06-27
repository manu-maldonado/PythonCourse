try:
    numero = int(input("ingresa un número"))
    resultado = 10 / numero
    print(resultado)
except ValueError: #controlar excepcione try - except
    print("Error: no ingresaste un numero válido")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")



#execpione multiples y genericas
try:
    pass

except (ValueError, ZeroDivisionError) as error:
    print(f"Error controlado: {error}")

except Exception as e:
    print("Error controlado: error inesperado")


#raise custom exception(excepciones personalizadsa)
class SaldoInsuficienteError(Exception):
    pass

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(f"Tu saldo{saldo} es menor al monto {monto}")
    
    return saldo - monto

retirar(500, 1000)