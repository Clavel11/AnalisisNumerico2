#Cálculo de sumas superiores e inferiores para
#la aproximación de la integral de exp(-x**2)

from math import *
n = eval(input('Número de particiones = '))
x0 = 0
#xn = 1
#h = (xn - x0)/n
h = 1/n
L = 0
U = 0

#Sumas inferiores y superiores
for i in range(n):
	L = L + h*exp(-(i*h+h)**2)
	U = U + h*exp(-(i*h)**2)
promedio = (U+L)/2

print(f"Suma inferior = {L:5.15f}")
print(f"Suma superior = {U:5.15f}")
print(f"Promedio = {promedio:5.15f}")

