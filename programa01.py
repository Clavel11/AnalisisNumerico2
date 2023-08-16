# Programa que aproxima la derivada de una funcion

from math import*

# Funcion original
def f(x):
	return eval(s)
	
# Derivada de la funcion
def fp(x):
	return eval(r)

#Imprime la tabla	
def imprimirMatriz(A):
	for f in A:
		for e in f:
			print('{:20.15f}'.format(e), end=' ')
		print()
		
s = input('f(x) = ')
r = input('fp(x) = ')
x = eval(input('x = '))

h = [0]*32
for i in range(len(h)):
	h[i] = 4**(-i-1)

A = []
for i in range(0,32):
	A.append([0]*4)
	
for i in range(0,32):
	A[i][0] = i+1
	A[i][1] = h[i]
	A[i][2] = (f(x+h[i]) - f(x))/h[i]
	A[i][3] = abs(A[i][2] - fp(x))

imprimirMatriz(A)
