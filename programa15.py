#REgal de Simpson 3/8
from math import*

def f(x):
	return eval(fs)

def Regla_simpson(a,b):
	p = (b-a)/3
	aproxf = (b-a)*(f(a) + 3*f(a+p) + 3*f(a+2*p) + f(b))/8
	return aproxf

n  = eval(input('Número de subintervalos = '))
fs = input('f(x) = ')
a  = eval(input('Límite inferior = '))
b  = eval(input('Límite superior = '))

integral = 0
p = (b-a)/n

for i in range (n):
	x0 = a + i*p
	x3 = x0 + p
	integral = integral + Regla_simpson(x0, x3)
	
print(f"Valor de la integral = {integral:5.15f}")
