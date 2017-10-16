class Pila():
	def __init__(self):
		self.pila = []

	def agregarElemento(self, elemento):
		self.pila.append(elemento)

	def sacarElemento(self):
		try:
			return self.pila.pop()
		except IndexError:
			return 

	def pilaVacia(self):
		return self.pila == []

	def longitudPila(self):
		return len(self.pila)
