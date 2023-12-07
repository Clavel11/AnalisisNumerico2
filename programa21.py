#Programa Runge-Kutta orden 2
from math import*

def f(x,t):
	return eval(fs)
	
fs = input('x prima = ')
a  = eval(input('Tiempo inicial = '))
b  = eval(input('Tiempo final = '))
n  = eval(input('Número de pasos = '))
val  = eval(input('Valor inicial de x = '))
print ('   t		x')
print('{:4.4f}{:20.10f}'.format(a, val))

h = (b-a)/n

for i in range(n):
	t = a + i*h
	K1 = h*f(val,t)
	K2 = h*f(val+K1, t+h)
	val = val + (K1 + K2)/2
	print('{:4.4f}{:20.10f}'.format(t+h, val))
