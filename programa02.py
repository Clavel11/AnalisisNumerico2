#Segundo metodo para calcular la derivada
from math import*
def f(x):
	return eval(fs)
def fp(x):
	return eval(fps)
fs = input('f(x) = ')
fps = input("f'(x) = ")
x = eval(input('x = '))
print ('   i		h		 fp		  error')

#primera itereacion
h = 4**(-1)
aprox = (f(x+h)-f(x-h))/2*h
error = abs(aprox-fp(x))
print('{:4.0f}{:20.15f}{:20.15f}{:20.15f}'.format(1, h, aprox, error))
minimo = error
mejor_aprox = aprox
valor_indice = 1

#iteraciones restantes
for i in range(2,33):
	h = 4**(-i)
	aprox = (f(x+h)-f(x-h))/(2*h)
	error = abs(aprox-fp(x))
	print('{:4.0f}{:20.15f}{:20.15f}{:20.15f}'.format(i, h, aprox, error))
	if error <= minimo:
		minimo = error
		mejor_aprox = aprox
		valor_indice = i
		
print("Mejor aproximacion para f' = ", mejor_aprox)
print("Indice correspondiente = ", valor_indice)
