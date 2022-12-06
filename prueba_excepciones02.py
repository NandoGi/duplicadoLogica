def divide():

	try:

		op1=(float(input("introduce el primer numero Pablo: ")))
		op2=(float(input("introduce el segundo numero: ")))
		print("la division es: " + str(op1/op2))

	except ValueError:
		print("el valor introducido es erroneo")

	except ZeroDivisionError:
		print("no se puede divir algun numero entre cero")

#la clausula (finally:) siempre se va ejecutar aunque el programa presente un error
	print("Calculo finalizado")

divide()



