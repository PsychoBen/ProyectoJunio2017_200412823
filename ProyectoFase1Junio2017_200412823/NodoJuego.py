#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     25/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoNave
import NodoPlayer
import NodoMatriz
import NodoDisparo
import ArbolABBPlayer
import NodoJuegoListaDoble


class NodoJuego:

    def __init__(self):
        self.arbolGeneralUsuarios = ArbolABBPlayer.arbolABBPlayer()
        self.arbolGeneralUsuariosEspejo = ArbolABBPlayer.arbolABBPlayer()
        self.usuarioActual1 = NodoPlayer.NodoPlayer()
        self.usuarioActual2 = NodoPlayer.NodoPlayer()
        self.user1 =""
        self.user2 = ""
        self.tamX = 0
        self.tamY = 0
        self.variante = ""
        self.tiempo = ""
        self.disparos = ""
        self.rafaga = ""

    def inicializarJuego(self, us1, us2, tax, tay, vari, tiem, disp, rafag):
        self.user1 = us1
        self.user2 = us2
        self.tamX = tax
        self.tamY = tay
        self.variante = vari
        self.tiempo = tiem
        self.disparos = disp
        self.rafaga = rafag






