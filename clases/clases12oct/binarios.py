# Solicitar al usuario una entrada entera

while True:
	try:
		numero_entero = int(input("Ingresa un número entero: "))
		
		# Convertir el número entero a binario y eliminar el
		numero_binario = bin(numero_entero)[2:]

		# Imprimir el resultado
		print(f"El número {numero_entero} en binario es: {numero_binario}")
		break	
	except ValueError:
		print('Introduzca un entero')


