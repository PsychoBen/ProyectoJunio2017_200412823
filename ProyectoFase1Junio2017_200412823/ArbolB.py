#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     13/07/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoArbolB

class ArbolB(object):

    def __init__(self, tam):

        self.codGraph = "digraph arbol{\n"
        self._tam = tam
        if self._tam <= 1:
          raise ValueError("El grado debe ser mayor a dos")
        self.raiz = NodoArbolB.NodoArbolB(tam)


    def insertarArbolB(self, nuevaClave):
        nodo = self.raiz
        if (nodo._esta_lleno):

            if(len(nodo.hijos) > 0):
                print "tiene hijos"
                while not nodo.hoja:
                    i = nodo.tamanio - 1
                    while i > 0 and nuevaClave < nodo.claves[i]:
                        i -= 1
                    if nuevaClave > nodo.claves[i]:
                        i += 1
                    siguiente = nodo.hijos[i]

                    if (siguiente._esta_lleno): ## aca esta el negocio de esta cosa
##                        nueva_raiz = NodoArbolB.NodoArbolB(self._tam)
##                        nueva_raiz.hijos.append(self.raiz)
##                        nueva_raiz.hoja = False
##                        nodo = nodo.dividir(nueva_raiz, nuevaClave)
                        nodo = siguiente.dividir(nodo, nuevaClave)
##                        self.raiz = nodo
##
                        return
                    else:
                        nodo = siguiente
                nodo.agregar_clave(nuevaClave)

            else:
                "no tiene hijos"
                nueva_raiz = NodoArbolB.NodoArbolB(self._tam)
                nueva_raiz.hijos.append(self.raiz)
                nueva_raiz.hoja = False
                nodo = nodo.dividir(nueva_raiz, nuevaClave)
                self.raiz = nueva_raiz
            return
        while not nodo.hoja:
            i = nodo.tamanio - 1
            while i > 0 and nuevaClave < nodo.claves[i]:
                i -= 1
            if nuevaClave > nodo.claves[i]:
                i += 1
            siguiente = nodo.hijos[i]
            if (siguiente._esta_lleno):
                nodo = siguiente.dividir(nodo, nuevaClave)
                return
            else:
                nodo = siguiente
        nodo.agregar_clave(nuevaClave)

    ## regresa verdadero si el arbol tiene el valor
    def buscarEnArbolB(self, valor, nodo = None):

        if nodo is None:
            nodo = self.raiz
        if valor in nodo.claves:
            return True
        elif nodo.hoja: ##si estamos en una hoja, ya no hay nada que chequear
            return False
        else:
            i = 0
            while i < nodo.tamanio() and valor > nodo.claves[i]:
                i += 1
            return self.buscarEnArbolB(valor, nodo.hijos[i])

    def ObtenerDotArbolB(self):
        dot = "digraph g { node [shape=record];"
##      imprime un nivel
        esteNivel = [self.raiz]
        nivel=0
        while esteNivel:
          siguiente_nivel = []
          output = ""
          pagina=0
          for nodo in esteNivel:
            if nodo.hijos:
              siguiente_nivel.extend(nodo.hijos)

            i = 0
            aux = len(nodo.claves)
            for i in range(0,aux):
              if(i == 0):output += "Nodo%d_%d[label=\"<P0>" %(nivel, pagina)
              output = output +"|"+ str(nodo.claves[i]) + "|<P%d>"% (i+1)
              if(i == aux -1):output += "\"]; "

            pagina += 1
##          print(output)
          dot += output
          esteNivel = siguiente_nivel
          nivel += 1

        esteNivel = [self.raiz]
        nivel=0
        while esteNivel:
          siguiente_nivel = []
          output = ""
          pagina=0
          aux2 = 0
          for nodo in esteNivel:
            if nodo.hijos:
              siguiente_nivel.extend(nodo.hijos)

            i = 0
            aux = len(nodo.hijos)
            for i in range(0,aux):
              output += "Nodo%d_%d:P%d -> Nodo%d_%d; " %(nivel, pagina, i, nivel+1, aux2)
              aux2 +=1

            pagina += 1

##          print(output)
          dot += output
          esteNivel = siguiente_nivel
          nivel += 1

        dot += "}"
        print(dot)
        return dot









