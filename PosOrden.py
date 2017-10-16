#!/usr/bin/python
# -*- coding: utf-8 -*-
from Nodo import *
from Pila import Pila
from VerificadorLexer import *
import sys

def leerCadena():
    cadena = raw_input('Ingrese la cadena de caracteres a operar:')
    cadenaVerificada = verificarCadena(cadena)
    if cadenaVerificada != None:
        return cadenaVerificada
    else:
        print 'La cadena ha sido ingresada incorrectamente: \n'
        leerCadena()

def crearArbol(lista, pila):
    for i in range(0, len(lista)):
        if lista[i] in '+-*/=':
            der = pila.sacarElemento()
            izq = pila.sacarElemento()
            nodoAux = Nodo(lista[i], izq, der)
            pila.agregarElemento(nodoAux)
        else:
            pila.agregarElemento(Nodo(lista[i], None, None))
    return pila.sacarElemento()


def imprimirArbolPostfijo(arbol):
    if arbol != None:
        imprimirArbolPostfijo(arbol.izq)
        imprimirArbolPostfijo(arbol.der)
        print arbol.valor


def ingresarArbol():
    while True:
        opcion = raw_input('Desea ingresar una expresion matematica en posfijo: (Y/N)')
        if opcion == 'Y' or opcion == 'y':
            cadena = leerCadena()
            print 'cadena' , cadena
            pila = Pila()
            nodo = crearArbol(cadena, pila)
            print 'Resultado operacion: ', evaluar(nodo)
        if opcion == 'N' or opcion == 'n':
            break
    return None


def main():
    ingresarArbol()
    return None


main()

                        
