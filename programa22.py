#Programa Runge-Kutta orden 4
#Es más exacto que el método Runge-Kutta de orden 2 

from math import*

def f(t,x):
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
	K1 = h*f(t,val)
	K2 = h*f(t+h/2, val+K1/2)
	K3 = h*f(t+h/2, val+K2/2)
	K4 = h*f(t+h, val+K3)
	val = val + (K1 + 2*K2 + 2*K3 + K4)/6
	print('{:4.4f}{:20.10f}'.format(t+h, val))
