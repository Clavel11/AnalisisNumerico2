#Regla de Simpson Compuesta
from math import*
def f(x):
	return eval(fs)
	
n  = eval(input('Número de subintervalos = '))
fs = input('f(x) = ')
a  = eval(input('Límmite inferior = '))
b  = eval(input('Límmite superior = '))

h = (b - a)/n
integral = 0
for i in range(0,n,2):
	integral = integral + h*(f(a + i*h) + 4*f(a + i*h + h) + f(a + i*h + 2*h))/3
	
print(f"Valor de la integral = {integral:5.15f}")
