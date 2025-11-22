#Fonda doña Maria

print("Fonda doña Maria")
print("Menú del día")

##Decrementar contador -= Itera sobre todos los elementos del arreglo y nos retorna del ultimo al primero
##LIFO
menu = ["Pozole", "Enchiladas", "Chiles en nogada"]
print(len(menu))
contador = len(menu) -1
while(contador >= 0):
	print(f"El menu ordenado del ultimo al primero es: {menu[contador]}") 
	contador -=1;

longitudMenu =  len(menu) #3 longitud total del arreglo de menu

print("-------- Menu inverso---------")

##Incrementar contadores += Itera sobre todos los elementos del arreglo y nos retorna del primero al ultimo
##FIFO
contadorOrdenado = 0
while(contadorOrdenado < longitudMenu):
	print(f"El menu ordenado del primero al ultimo es: {menu[contadorOrdenado]}") #0
	contadorOrdenado +=1 #1

#Output
#0 < 3
#1 < 3
#2 < 3

print("Presione . si desea salir de la pantalla de menu")
totalCuenta = 0
ordenActiva = True

while ordenActiva:
	opcion = input("Quieres ordenar algo, ingresa el número de la opción del menu(1,3)")
	if opcion == "1":
		print("pozole agregado a la compra")
		totalCuenta +=80
	elif opcion == "2":
		print("Enchiladas agregadas a la compra")
		totalCuenta +=70
	elif opcion == "3":
		print("Chiles en nogada agregadas a la compra")
		totalCuenta +=120
	elif(opcion == "."):
		ordenActiva = False
	else:
		print("No existe esa opción")

	print(f"Total hasta ahora es: {totalCuenta}")

	if totalCuenta > 0:
		propina = totalCuenta * 0.10
		totalFinal = totalCuenta + propina		
		print("Resumen de cuenta:")
		print(f"Subtotal: ${totalCuenta}")
		print(f"Propina: {propina}")
		print(f"Total: {totalFinal}")
		print("Gracias por comprar con nosotros")		