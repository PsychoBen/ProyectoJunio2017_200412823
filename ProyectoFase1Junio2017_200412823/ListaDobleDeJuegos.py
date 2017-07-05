#-------------------------------------------------------------------------------
# Name:        Clase lista doble de juegos del usuario
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoJuegoListaDoble

class ListaDobleDeJuegos:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
        self.ganados = 0
        self.shooter = 0.00

    def estaVacia(self):
        if(self.primero == None):
            return True
        else:
            return False

    def insertarListaDeJuegosFinalizados(self, nameOponente, realizados, acertados, fallados, gano, danio):
        nuevoNodoGame = NodoJuegoListaDoble.NodoJuegoListaDoble()
        nuevoNodoGame.Contrincante = nameOponente
        nuevoNodoGame.tirosRealizados = realizados
        nuevoNodoGame.tirosAcertados = acertados
        nuevoNodoGame.tirosFallados = fallados
        nuevoNodoGame.gano = gano
        nuevoNodoGame.danioRecibido = danio
        if(self.estaVacia()):
            self.primero = nuevoNodoGame
            self.ultimo = nuevoNodoGame
            self.tamanio = self.tamanio + 1
        else:
            self.ultimo.siguienteGame = nuevoNodoGame
            nuevoNodoGame.anteriorGame = self.ultimo
            self.ultimo = nuevoNodoGame
            self.tamanio = self.tamanio + 1
            print "Insertado juego finalizado"

    def mostrarListaDobleDeJuegosUsuarioAdelante(self):
        cadena = ""
        if (self.primero == None):
            print "Lista vacia"
        else:
            aux = self.primero
            while (aux != None):
                if (aux == self.primero):
                    cadena = cadena + aux.verDatosNodoJuegoListaDoble() + " "
                else:
                    cadena = cadena + aux.verDatosNodoJuegoListaDoble() + " "
                    print (aux.verDatosNodoJuegoListaDoble())
                aux = aux.sguienteGame
        print "***************************************************"
        print "***************************************************"
        print cadena
        print "***************************************************"
        print "***************************************************"
        return cadena

    def eliminarNodoJuegoListaDoble(self):
        pass

    def obtenerPorcentajeTirosAcertados(self):
        porcent = 0.00
        sumaAcer = 0
        sumaRealiz = 0
        aux = self.primero
        while(aux!=None):
            sumaRealiz = sumaRealiz + int(aux.tirosRealizados)
            sumaAcer = sumaAcer + int(aux.tirosAcertados)
            aux = aux.siguienteGame
        if(sumaRealiz==0):
            return porcent
        else:
            porcent = (sumaAcer * 100) / sumaRealiz
        return porcent


    def obtenerCantidadJuegosGanados(self):
        ganados = 0
        aux = self.primero

        while(aux!=None):
            if(aux.gano=="1"):
                ganados = ganados + 1
            aux = aux.siguienteGame
        return ganados

    def definirEstadisticasPlayer(self):
        gana = self.obtenerCantidadJuegosGanados()
        shoots = self.obtenerPorcentajeTirosAcertados
        self.ganados = gana
        self.shooter = shoots


    def escribirListaDobleDeJuegos2(self, namePadre, archivo):
        if self.estaVacia():
            print "User " + namePadre + " no  tiene lista de juegos"
            return
        else:
            aux = self.primero
            k = -1
            archivo.write("subgraph Games" +" "+ " { \n ")
            archivo.write("rankdir = LR; \n ");
            archivo.write(namePadre + "-> "+ namePadre +"_game0 \n")
            while(aux != None):
                k = k + 1
                if(aux.anteriorGame != None):
                    pass
                archivo.write(namePadre+"_game"+str(k)+"[shape=box fillcolor = bisque2 style=\"rounded,filled\" fontsize=\"10.0\" ];")
                imaggenn =""
                archivo.write(namePadre+"_game"+str(k)+"[label = \"Oponente: "+" "+ aux.Contrincante + " \n TR: "+ str(aux.tirosRealizados) + " TA: "+ str(aux.tirosAcertados)+ " TF: "+ str(aux.tirosFallados) + "\n Resultado: " + aux.obtenerCadenaResultadoJuego() + "\n Damage: " + str(aux.danioRecibido)  + "\"]; ")
                if(aux.siguienteGame != None):
                    archivo.write(namePadre+"_game"+str(k)+" -> "+namePadre+"_game"+ str(k+1) + ";")
                    archivo.write(namePadre+"_game"+str(k + 1)+" -> "+namePadre+"_game"+  str(k) + ";");
                aux = aux.siguienteGame
            archivo.write("\n }")



