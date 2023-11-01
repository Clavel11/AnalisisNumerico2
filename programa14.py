# Metodo adaptativo de la regla de Simpson
# Se grafican los subintervalos 
from math import*

def f(x):
	return eval(fs)
	
def regla_recursiva(a,b,e):
	S1 = (b-a)*(f(a) + 4*f((a+b)/2) + f(b))/6
	c = (a + b)/2
	S2 = (c-a)*(f(a) + 4*f((a+c)/2) + f(c))/6 + (b-c)*(f(c) + 4*f((c+b)/2) + f(b))/6
	
	print(c, "     ", 0.0)
	print(c, "     ", f(c), "\n")
	
	if abs((S2 - S1)/15) < e:
		return S2 + (S2 - S1)/15
	else:
		c = (a + b)/2
		return regla_recursiva(a,c,e/2) + regla_recursiva(c,b,e/2)

fs = "cos(2*x)/exp(x)"
a  = 0
b  = 5*pi/4
e  = 0.00005
integral = regla_recursiva(a,b,e)

# Correr el programa como: python3 programa14.py > datos.txt
# En la terminal escribir: plot [0:3.93] cos(2*x)/exp(x), 'datos.txt' with lines
# Para salir de gnuplot escribimos: quit
