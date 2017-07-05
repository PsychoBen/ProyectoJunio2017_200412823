#-------------------------------------------------------------------------------
# Name:        Clase nodo juego lista doble
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class NodoJuegoListaDoble:

    def __init__(self):
        self.Contrincante = None
        self.tirosRealizados = 0
        self.tirosAcertados = 0
        self.tirosFallados = 0
        self.gano = False
        self.danioRecibido = 0
        self.siguienteGame = None
        self.anteriorGame = None

    def obtenerCadenaResultadoJuego(self):
        if (self.gano == True):
            return " Gano "
        else:
            return " Perdio "

    def verDatosNodoJuegoListaDoble(self):
        gano = ""
        if(self.gano == True):
            gano = "Gano"
        else:
            gano = "Perdio"
        return {'Contrincante': self.Contrincante, "Tiros Realizados": str(self.tirosRealizados),"Tiros Acertados": str(self.tirosRealizados), "Tiros Fallados": str(self.tirosFallados), "Gano": gano,"Da?o recibido": str(self.danioRecibido) }
