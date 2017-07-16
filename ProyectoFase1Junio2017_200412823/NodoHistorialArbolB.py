#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/07/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class NodoHistorialArbolB:

    def __init__(self, cordX, cordY, tipoShoot, resu, tipoNaveGolp, emisr, receptr, fech, timeResta, numeroShoot):
        self.coordenadaX = cordX
        self.coordenadaY = cordY
        self.tipoTiro = tipoShoot
        self.resultado = resu
        self.tipoNaveGolpeada = tipoNaveGolp
        self.emisor = emisr
        self.receptor = receptr
        self.fecha = fecha
        self.tiempoRestante = timeResta
        self.numeroTiro = numeroShoot

    def __init__(self):
        self.coordenadaX
        self.coordenadaY
        self.tipoTiro
        self.resultado
        self.tipoNaveGolpeada
        self.emisor
        self.receptor
        self.fecha
        self.tiempoRestante
        self.numeroTiro

    def inicializarNodoHistorial(self, cordX, cordY, tipoShoot, resu, tipoNaveGolp, emisr, receptr, fech, timeResta, numeroShoot):
        self.coordenadaX = cordX
        self.coordenadaY = cordY
        self.tipoTiro = tipoShoot
        self.resultado = resu
        self.tipoNaveGolpeada = tipoNaveGolp
        self.emisor = emisr
        self.receptor = receptr
        self.fecha = fecha
        self.tiempoRestante = timeResta
        self.numeroTiro = numeroShoot
