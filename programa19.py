#Problema de valor inicial para una ecuación dierencial ordinaria de primer orden
#Método de Euler

from math import*

def x(s):
	return eval(xs)
	
def t(s):
	return eval(ts)
	
def metodo_euler(xh,th):
	return xh + h*(x(xh) + t(th))
	
xs = input('x prima, sólo términos x = ')
ts = input('x prima, sólo términos t = ')
a  = eval(input('Tiempo inicial = '))
b  = eval(input('Tiempo final = '))
n  = eval(input('Número de pasos = '))
x  = eval(input('Valor inicial de x = '))
print ('   t		x')
print('{:4.0f}{:20.15f}'.format(a, x))

h = (a-b)/n

for i in range(1,101):
	t = i*h
	xh = metodo_euler(x, a+t)
	print('{:4.0f}{:20.15f}'.format(a+t, x))
	x = xh



