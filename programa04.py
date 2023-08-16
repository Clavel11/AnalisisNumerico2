#Tercer metodo para calcular la derivada
from math import*
def f(x):
	return eval(fs)
def fp(x):
	return eval(fps)	
def phi(x,h):
	return (f(x+h) - f(x-h))/(2*h)
def Phi(x,h):
	return 4*phi(x,h/2)/3 - phi(x,h)/3 
	
fs = input('f(x) = ')
fps = input("f'(x) = ")
x = eval(input('x = '))
print ('   i		h		 fp		  error')

#primera itereacion
h = 4**(-1)

aprox = 16*Phi(x,h/2)/15 - Phi(x,h)/15
error = abs(aprox-fp(x))
print('{:4.0f}{:25.20f}{:25.20f}{:25.20f}'.format(1, h, aprox, error))
minimo = error
mejor_aprox = aprox
valor_indice = 1

#iteraciones restantes
for i in range(2,33):
	h = 4**(-i)
	aprox = 16*Phi(x,h/2)/15 - Phi(x,h)/15
	error = abs(aprox-fp(x))
	print('{:4.0f}{:25.20f}{:25.20f}{:25.20f}'.format(i, h, aprox, error))
	if error <= minimo:
		minimo = error
		mejor_aprox = aprox
		valor_indice = i
		
print("Mejor aproximacion para f' = ", mejor_aprox)
print("Indice correspondiente = ", valor_indice)
