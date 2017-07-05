#-------------------------------------------------------------------------------
# Name:        Clase nodo matriz ortogonal
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoNaveEnMatriz
import NodoDisparo


class nodoMatrizOrtogonal:

    def __init__(self):
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
        self.adelante = None
        self.atras = None
        self.fila = 0
        self.columna = 0
        self.dimension = 0
        self.valor = 0
        self.ocupado = False
        self.rutaimagen = ""
        self.cadenaextra = ""
        self.nave = NodoNaveEnMatriz.NodoNave()
        self.disparo = NodoDisparo.NodoDisparo()

    def inicializarNodoMatrizOrtogonal_1(self, x , y ,z , dat, rutaIm):
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
        self.adelante = None
        self.atras = None
        self.fila = x
        self.columna = y
        self.dimension = z
        self.valor = dat
        self.ocupado = False
        self.rutaimagen = rutaIm
        self.cadenaextra = ""

    def inicializarNodoMatrizOrtogonal_2(self, x , y ,z , dat, rutaIm, valorr):
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None
        self.adelante = None
        self.atras = None
        self.fila = x
        self.columna = y
        self.dimension = z
        self.valor = dat
        self.ocupado = False
        self.rutaimagen = rutaimagen
        self.cadenaextra = valorr
