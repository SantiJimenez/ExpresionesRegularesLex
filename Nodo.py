from Pila import *

class Nodo():
	
	def __init__(self, valor, izq = None, der = None):
		self.valor = valor
		self.izq = izq
		self.der = der

class Tabla():
	variables = {}
	operadores = []
	numeros = []

def evaluar(arbol):
	if arbol.valor == '+': 
		Tabla.operadores.append(arbol.valor)
		return int(evaluar(arbol.izq)) + int(evaluar(arbol.der))		

	if arbol.valor == '-':
		Tabla.operadores.append(arbol.valor)
		return int(evaluar(arbol.izq)) - int(evaluar(arbol.der))
	
	if arbol.valor == '/':
		Tabla.operadores.append(arbol.valor)
		return int(evaluar(arbol.izq)) / int(evaluar(arbol.der))

	if arbol.valor == '*':
		Tabla.operadores.append(arbol.valor)
		return int(evaluar(arbol.izq)) * int(evaluar(arbol.der))

	if arbol.valor == '=':
		Tabla.operadores.append(arbol.valor)
		valor = evaluar(arbol.izq)
		Tabla.variables[arbol.der.valor] = valor
		return valor
	
	if Tabla.variables.has_key(arbol.valor) == True:
		return Tabla.variables[arbol.valor]
	elif Tabla.variables.has_key(arbol.valor) == False:
		Tabla.numeros.append(arbol.valor)
		return int(arbol.valor)
			
def imprimirDatos():
	print "Variables almacenadas:"
	print Tabla.variables
	print "Operadores almacenados:"
	print Tabla.operadores
	print "Valores almacenados:"	
	print Tabla.numeros	


