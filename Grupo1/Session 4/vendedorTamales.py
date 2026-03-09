#vendedor de tamales 
print("Vendedor de tamales automatico")

#products o tipos de tamales en existencia 
sabores = ["Verde","Mole","Rajas","Dulce"]
precios = {"Verde":25, "Mole":28, "Rajas":26, "Dulce":22}

#cliente
dinero = int(input("¿Cuánto dinero traes?"))
saborDeseado = input("¿De qué sabor gusta?")

#verificar disponibilidad y dinero
if saborDeseado in sabores:
	precio = precios[saborDeseado]

	if dinero >= precio:
		cambio = dinero - precio
		print(f"Aqui tienes tu tamal deseado {saborDeseado} y tu cambio es {cambio}")
	
		if cambio >= 5:
			print("tengo chicles también")
	else:
		falta = precio - dinero
		print(f"no te alcanza, carnal, Te faltan {falta}")
else:
	print("ese sabor no existe jefe, ponga atención, solo tenemos de:")
	for sabor in sabores:
		print(f" {sabor}")

		
#{} - objecto - key - value