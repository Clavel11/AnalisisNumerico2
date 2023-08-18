# Algoritmo de extrapoación de Richardson
from math import*
def f(x):
	return eval(fs)
def fp(x):
	return eval(fps)	
def phi(x,h):
	return (f(x+h) - f(x-h))/(2*h)
	
def imprimirMatriz(A):
	for f in A:
		for e in f:
			print('{:20.15f}'.format(e), end=' ')
		print()
	
fs = input('f(x) = ')
fps = input("f'(x) = ")
x = eval(input('x = '))
N = eval(input('N = '))
h = eval(input('h = '))

#Matriz D
D = []
for i in range(N+1):
	D.append([0]*(N+1))
	
#Matriz de errores
E = []
for i in range(N+1):
	E.append([0]*(N+1))
	
#Cálculo de D(n, 0)
for n in range(N+1):
	D[n][0] = phi(x,h/2**n)
#Cálculo de D(n,m) 1<m<n	
for m in range(1,N+1):
	for n in range(m,N+1):
		D[n][m] = (4**m)*D[n][m-1]/(4**m - 1) - D[n-1][m-1]/(4**m - 1)
		
#Cálculo de matriz de errores
minimo = abs(D[0][0]-fp(x))
mejor_aprox = D[0][0]
fila = 0
columna = 0
for m in range(0,N+1):
	for n in range(m,N+1):
		E[n][m] = abs(D[n][m]-fp(x))
		if E[n][m] <= minimo:
			minimo = E[n][m]
			mejor_aprox = D[n][m]
			fila = n
			columna = m
			
print("Matriz de aproximación de f'")		
imprimirMatriz(D)

print("Matriz de errores")
imprimirMatriz(E)

print("Mejor aproximacion para f' = ", mejor_aprox)
print(f"Indice correspondiente = {fila},{columna}")

