#Regla del trapecio
from math import*
def f(x):
	return eval(fs)
	
fs = input('f(x) = ')
a = eval(input('Límmite inferior = '))
b = eval(input('Límmite superior = '))

h = (b - a)/2
integral = h*(f(a) + 4*f(a + h) + f(a + 2*h))/3
	
print(f"Valor de la integral = {integral:5.15f}")
