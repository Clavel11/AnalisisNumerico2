#Métodos de la serie de Taylor
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

for i in range(0,n):
	t = a + i*h
	xp = f(val,t)
	xp2 = 2*val*xp + 3*t**2
	xp3 = 2*xp**2 + 2*val*xp2 + 6*t
	xp4 = 6*xp*xp2 + 2*val*xp3 + 6
	val = val + h*xp + (h**2)*xp2/2 + (h**3)*xp3/6 + (h**4)*xp4/24
	print('{:4.4f}{:20.10f}'.format(t+h, val))
