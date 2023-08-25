#Regla del trapecio
from math import*
def f(x):
	return eval(fs)
	
fs = input('f(x) = ')
a = eval(input('Límmite inferior = '))
b = eval(input('Límmite superior = '))
n = eval(input('Número de trapecios = '))

h = (b - a)/n
integral = 0
for i in range(1,n):
	integral = integral + h*(f(a + i*h) + f(a + (i+1)*h))/2
	
print(f"Valor de la integral = {integral:5.15f}")
