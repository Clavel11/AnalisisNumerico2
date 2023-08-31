#Regla recursiva del trapecio
from math import*
def f(x):
	return eval(fs)
	
fs = input('f(x) = ')
a = eval(input('Límmite inferior = '))
b = eval(input('Límmite superior = '))
n = eval(input('Número de subintervalos = '))

h = (b - a)
R = [0]*n
R[0] = (b-a)*(f(a)+f(b))/2
print('{:5.15f}'.format(R[0]))
for i in range(1,n):
	suma = 0
	h = (b-a)/2**i
	for k in range(1, 2**(i-1)):
		suma = suma + h*f(a + (2*k - 1)*h)
	R[i] = R[i-1]/2 + suma
	print('{:5.15f}'.format(R[i]))
