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

class NodoArbolB(object):

    def __init__(self, tam):
        self.claves = []
        self.hijos = []
        self.hoja =True
        self._tam = tam

    def __str__(self):
      cadena=str(self.claves)
      cadena2=str(self.hijos)
      cadena3 = cadena + cadena2
      return cadena3

    #este metodo sirve para separar y reasignar las claves hijas
    def dividir(self, padre, payload):

      nodo_nuevo = self.__class__(self._tam)
      temporal = [self.tamanio]  ##agregado
      temporal = self.claves   ##agregado
      temporal.append(payload)  ##agregado
      temporal.sort()
      punto_medio = self.tamanio//2
      valor_separar = temporal[punto_medio]  ##agregado
##      valor_separar = self.claves[punto_medio]  ##solo comentario
      if (padre._esta_lleno):
        print "aca llamo a separar al padre"

##        padre = padre.dividir(padre, valor_separar)

      padre.agregar_clave(valor_separar)
      # agrega claves y los hijos a los nodos apropiados
      nodo_nuevo.hijos = self.hijos[punto_medio + 1:]
      self.hijos = self.hijos[:punto_medio + 1]
      nodo_nuevo.claves = self.claves[punto_medio+1:]
      self.claves = self.claves[:punto_medio]

    #si el nodo_nuevo tiene hijos, lo coloca como un nodo interno
      if len(nodo_nuevo.hijos) > 0:
        nodo_nuevo.hoja = False

      padre.hijos = padre.agregar_hijo(nodo_nuevo)
##      if(len(padre.claves) == self._tam):
####        temporal.
##        print " 55555 "
##        nuevoVal  = padre.claves.pop(punto_medio)
##        padre = padre.dividir(padre, nuevoVal)
##        return
      if payload < valor_separar:
        return self
      else:
        return nodo_nuevo

    @property
    def tamanio(self):
        return len(self.claves)

    @property
    def _esta_lleno(self):
        return self.tamanio==self._tam - 1

    ##agrega una clave a un nodo
    def agregar_clave(self, valor):
        self.claves.append(valor)
        self.claves.sort()

    ##agrega un hijo al nodo y lo ordena, por si lo tenemos que separar
    ##ya jale el valor del centro, regresa una lista ordenada de nodos
    def agregar_hijo(self, nuevo_nodo):
        i = len(self.hijos) - 1
        while i >= 0 and self.hijos[i].claves[0] > nuevo_nodo.claves[0]:
            i -= 1
        return self.hijos[:i + 1] + [nuevo_nodo] + self.hijos[i + 1:]








