#Regla de Boole
from math import*

def f(x):
	return eval(fs)

def Regla_boole(a,b):
	p = (b-a)/4
	return 2*p*(7*f(a) + 32*f(a+p) + 12*f(a+2*p) + 32*f(a+3*p) + 7*f(b))/45

n  = eval(input('Número de subintervalos = '))
fs = input('f(x) = ')
a  = eval(input('Límite inferior = '))
b  = eval(input('Límite superior = '))

integral = 0
p = (b-a)/n

for i in range (n):
	x0 = a + i*p
	x4 = x0 + p
	integral = integral + Regla_boole(x0, x4)
	
print(f"Valor de la integral = {integral:5.15f}")
