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
import arbolAVLContactos


class NodoPlayer:

    def __init__(self):
        self.nickname = ""
        self.password=""
        self.estaConectado = False
        self.yaExisteEnJugadores = False
        self.listaGamesUser = ListaDobleDeJuegos.ListaDobleDeJuegos()
        self.matrizOrtogonalUser = MatrizOrtogonal.MatrizOrtogonal()
        self.matrizOrtogonalUserActual = MatrizOrtogonal.MatrizOrtogonal()
        self.arbolAvlContactosPlayer = arbolAVLContactos.arbolAVLContactos()
        self.maxGanados = 0
        self.efectividad = 0
        self.izquierda = None
        self.derecha = None
        self.factorBalance=0
        self.Siguiente=None
        self.Anterior=None

    def inicializarNodoPlayer(self, nic, pas, conec):
        self.nickname = nic
        self.password = pas
        self.estaConectado = conec


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

    def verNodoUsuasxrio(self):
        return {"NameUsuario": self.NameUsuario, "Contrasenia": str(self.Contrasenia), "Direccion": self.Direccion, "DireccionActual": self.DireccionActual}


