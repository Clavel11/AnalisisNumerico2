#Algoritmo de Romberg
from math import*


def f(x):
	return eval(fs)

def imprimirMatriz(A):
	for f in A:
		for e in f:
			print('{:10.15f}'.format(e), end=' ')
		print()
		
def crear_matriz(A):
	"""Función que crea una matriz llena de ceros
	de tamaño NxN"""
	for i in range(N+1):
		A.append([0]*(N+1))
	
fs = input('f(x) = ')
a = eval(input('Límmite inferior = '))
b = eval(input('Límmite superior = '))
v = eval(input('Valor de la integral = '))
N = eval(input('Número de subintervalos = '))

#Matriz R
R = []
crear_matriz(R)
	
#Matriz de errores
E = []
crear_matriz(E)

#Cálculo de R[0][0]
h = (b - a)
R[0][0] = (b-a)*(f(a)+f(b))/2

#Cálculo de R[n][0]
for i in range(1,N):
	suma = 0
	h = (b-a)/2**i
	for k in range(1, 2**(i-1)):
		suma = suma + h*f(a + (2*k - 1)*h)
	R[i][0] = R[i-1][0]/2 + suma

#Cálculo de R(n,m) 1<m<n	
for m in range(1,N+1):
	for n in range(m,N+1):
		R[n][m] = (4**m)*R[n][m-1]/(4**m - 1) - R[n-1][m-1]/(4**m - 1)
		
#Cálculo de matriz de errores
minimo = abs(R[0][0]-v)
mejor_aprox = R[0][0]
fila = 0
columna = 0
for m in range(0,N+1):
	for n in range(m,N+1):
		E[n][m] = abs(R[n][m]-v)
		if E[n][m] <= minimo:
			minimo = E[n][m]
			mejor_aprox = R[n][m]
			fila = n
			columna = m
		
print("Matriz de aproximación de la integral de f")		
imprimirMatriz(R)

print("Mejor aproximacion para la integral de f = ", mejor_aprox)
print(f"Indice correspondiente = {fila},{columna}")


