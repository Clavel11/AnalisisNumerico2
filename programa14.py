# Metodo adaptativo de la regla de Simpson
from math import*
	
def regla_recursiva(a,b,e):
	S1 = (b-a)*(f(a) + 4*f((a+b)/2) + f(b))/6
	c = (a + b)/2
	S2 = (c-a)*(f(a) + 4*f((a+c)/2) + f(c))/6 + (b-c)*(f(c) + 4*f((c+b)/2) + f(b))/6
	if abs((S2 - S1)/15) < e:
		return S2 + (S2 - S1)/15
	else:
		c = (a + b)/2
		return regla_recursiva(a,c,e/2) + regla_recursiva(c,b,e/2)

def f(x):
	return eval(fs)
	
fs = input('f(x) = ')
a  = eval(input('Límmite inferior = '))
b  = eval(input('Límmite superior = '))
e  = eval(input('Precision = '))
integral = regla_recursiva(a,b,e)
print(f"Valor de la integral = {integral:5.15f}")
