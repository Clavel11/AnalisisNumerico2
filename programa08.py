#Cálculo de sumas superiores e inferiores para
#la aproximación de la integral de exp(cos(x))
#en el intervalo [0, 3pi]

from math import *
def f(x):
	return exp(cos(x))
	
n = eval(input('Número de particiones = '))
x0 = 0
xn = 3*pi
h = (xn - x0)/n
L = 0 
U = 0

#Sumas inferiores y superiores
for i in range(n):
	x = i*h
	if 0 <= x < pi or 2*pi < x <= 3*pi:
		L = L + h*f((i*h+h))
		U = U + h*f((i*h))
	if pi <= x <= 2*pi:
		U = U + h*f((i*h+h))
		L = L + h*f((i*h))
		
promedio = (U+L)/2

print(f"Suma inferior = {L:5.15f}")
print(f"Suma superior = {U:5.15f}")
print(f"Promedio = {promedio:5.15f}")

