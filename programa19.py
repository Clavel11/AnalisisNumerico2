#Problema de valor inicial para una ecuación dierencial ordinaria de primer orden
#Método de Euler

from math import*

def f(x,t):
	return eval(fs)
	
def metodo_euler(x,t):
	return x + h*f(x,t)
	
fs = input('x prima = ')
a  = eval(input('Tiempo inicial = '))
b  = eval(input('Tiempo final = '))
n  = eval(input('Número de pasos = '))
val  = eval(input('Valor inicial de x = '))
print ('   t		x')
print('{:4.4f}{:20.10f}'.format(a, val))

h = (b-a)/n

for i in range(1,101):
	tiempo = a + i*h
	xh = metodo_euler(val, tiempo)
	print('{:4.4f}{:20.10f}'.format(tiempo, xh))
	val = xh
