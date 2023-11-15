#5 reglas abiertas de Newton-Cotes
from math import*

def f(x):
	return eval(fs)

def medio_punto(a,b):
	h = (b-a)/2
	return 2*h*f(a+h)
	
def dos_puntos(a,b):
	h = (b-a)/3
	return 3*h*(f(a+h) + f(a+2*h))/2

def tres_puntos(a,b):
	h = (b-a)/4
	return 4*h*(2*f(a+h) - f(a+2*h) + 2*f(a+3*h))/3
	
def cuatro_puntos(a,b):
	h = (b-a)/5
	return 5*h*(11*f(a+h) + f(a+2*h) + f(a+3*h) + 11*f(a+4*h))/24

def cinco_puntos(a,b):
	h = (b-a)/6
	return 6*h*(11*f(a+h) - 14*f(a+2*h) + 26*f(a+3*h)- 14*f(a+4*h) + 11*f(a+5*h))/20

m  = eval(input('Número de subintervalos = '))
fs = input('f(x) = ')
a  = eval(input('Límite inferior = '))
b  = eval(input('Límite superior = '))

integral1 = 0
integral2 = 0
integral3 = 0
integral4 = 0
integral5 = 0
p = (b-a)/m

for i in range (m):
	x0 = a + i*p
	xn = x0 + p
	integral1 = integral1 + medio_punto(x0, xn)
	integral2 = integral2 + dos_puntos(x0, xn)
	integral3 = integral3 + tres_puntos(x0, xn)
	integral4 = integral4 + cuatro_puntos(x0, xn)
	integral5 = integral5 + cinco_puntos(x0, xn)
	
print("Valor de la integral")
print(f"Regla del medio punto = {integral1:5.10f}")
print(f"Regla de 2 puntos = {integral2:5.10f}")
print(f"Regla de 3 puntos = {integral3:5.10f}")
print(f"Regla de 4 puntos = {integral4:5.10f}")
print(f"Regla de 5 puntos = {integral5:5.10f}")
