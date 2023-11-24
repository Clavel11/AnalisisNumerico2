#Cuadratura Gaussiana
from math import*

def f(x):
	return eval(fs)

def cuadratura(a,b):
	suma = 0
	for i in range(3):
		suma = suma + A[i]*f((b-a)*t[i]/2 + (b+a)/2)
	return (b-a)*suma/2

n  = eval(input('Número de subintervalos = '))
fs = input('f(x) = ')
a  = eval(input('Límite inferior = '))
b  = eval(input('Límite superior = '))

integral = 0
p = (b-a)/n
A = [5/9, 8/9, 5/9]
t = [-sqrt(3/5), 0, sqrt(3/5)]

for i in range (n):
	x0 = a + i*p
	x4 = x0 + p
	integral = integral + cuadratura(x0, x4)
	
print(f"Valor de la integral = {integral:5.15f}")
