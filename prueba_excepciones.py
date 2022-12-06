#!/usr/bin/python
# -*- coding: latin-1 -*-

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1, num2):

	try:
		return(num1/num2)
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "operacion erronea"

while True:
	try:

		op1=(int(input("Introduce el primer n�mero Gianina: ")))

		op2=(int(input("Introduce el segundo n�mero Cacherota: ")))

		break

	except ValueError:
		print("Los valores introducidos no son correctos, porfavor vuelve a intentar")

opcion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

operacion=opcion.lower()

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operaci�n no contemplada")


print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n del programa ")