from matrix import Matrix
print("Tarea #2")
print("Ingrese el numero de acuerdo a la opcion que desee:")
print("0. Mapeo por filas")
print("1. Mapeo por columnas")
choice = raw_input()
try:
	choice = int(choice)
except:
	print("El la opcion ingresada no es un numero.")
	print("Se tomara la opcion por default.")
	print("Default option: Mapeo por filas.")
	choice = 0
if(choice != 0 and choice != 1):
	print("El numero ingresado no corresponde a una opcion valida.")
	print("Se tomara la opcion por default.")
	print("Default option: Mapeo por filas.")
	choice = 0
print("Definicion de la Matriz a mapear.")
print("Ingrese la primer dimension del arreglo (x) : ")
x = raw_input()
def is_int(subject):
	try:
		subject = int(subject)
		return True
	except: 
		return False
while(not is_int(x)):
	print("La entrada NO es un numero.")
	print("Vuelva a intentar:")
	x = raw_input()	
x =  int(x)
print("Ingrese la segunda dimension del arreglo (y) : ")
y = raw_input()
while(not is_int(y)):
	print("La entrada NO es un numero.")
	print("Vuelva a intentar:")
	y = raw_input()
y =  int(y)
print("Ingrese i de la posicion que desea linealizar:")
true_x = raw_input()
while(not is_int(true_x)):
	print("La entrada NO es un numero.")
	print("Vuelva a intentar:")
	true_x = raw_input()
true_x = int(true_x)
print("Ingrese j de la posicion que desea linealizar:")
true_y = raw_input()
while(not is_int(true_y)):
	print("La entrada NO es un numero.")
	print("Vuelva a intentar:")
	true_y = raw_input()		
true_y = int(true_y)
if(choice == 0):
	matriz = Matrix(x,y)
	pos = matriz.to_lineal(true_x,true_y,True)
	print("Resultado = Posicion {}".format(pos))
	matriz.graph()
else:
	matriz = Matrix(x,y)
	pos = matriz.to_lineal(true_x,true_y,False)
	print("Resultado = Posicion {}".format(pos))
	matriz.graph()
