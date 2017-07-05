#-------------------------------------------------------------------------------
# Name:        Clase nodo player
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoJuegoListaDoble
import ListaDobleDeJuegos
import MatrizOrtogonal
import NodoMatriz


class NodoPlayer:

    def __init__(self):
        self.nickname = ""
        self.password=""
        self.listaGamesUser = ListaDobleDeJuegos.ListaDobleDeJuegos()
        self.estaConectado = False
        self.matrizOrtogonalUser = MatrizOrtogonal.MatrizOrtogonal()
        self.matrizOrtogonalUserActual = MatrizOrtogonal.MatrizOrtogonal()
        self.maxGanados = 0
        self.efectividad = 0
        self.izquierda = None
        self.derecha = None


    def verNodoPlayer(self):
        return {"Nickname": self.nickname, "Password": self.password}

    def getMatrizOrtogonalUser(self):
        return self.matrizOrtogonalUser

    def obtenerListaDobleDeJuegos(self):
        return self.listaGamesUser

    def getEstaConectado(self):
        return estaConectado

    def setListaDobleDeJuegos(self, listaJuegos):
        self.listaGamesUser = listaJuegos

    def setEstaConectado(self, isConectado):
        self.estaConectado = isConectado


