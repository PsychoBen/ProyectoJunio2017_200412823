#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     12/07/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class NodoHistorial:

    def __init__(self, t):
        self.claves = []
        self.hijos = []
        self.hoja =True
        self._t = t
