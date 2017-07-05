#-------------------------------------------------------------------------------
# Name:        Clase Arbol de jugadores
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import NodoPlayer
import subprocess
import os.path
import errno
import os


class arbolABBPlayer:

    def __init__(self):
        self.raiz = None
        self.cantidad = 0
        self.Path = "C:/Proyecto/EDDVacasJunio/"


    def inorden2(self, nodo):
        if(nodo == None):
            print "Se acaba de podar"
        else:
            self.inorden(nodo.izquierda)
##            print nodo.nickname
            print nodo.verNodoPlayer()
            self.inorden(nodo.derecha)


    def inorden(self, nodo):
        if(nodo == None):
            return
        else:
            self.inorden(nodo.izquierda)
##            print nodo.nickname
            print nodo.verNodoPlayer()
            self.inorden(nodo.derecha)


    def preorden(self, nodo):
        if(nodo == None):
            return
        else:
##            print nodo.nickname
            print nodo.verNodoPlayer()
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)


    def postorden(self, nodo):
        if(nodo == None):
            return
        else:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print nodo.verNodoPlayer()
##            print nodo.nickname


    def estaVacio(self):
        if (self.raiz == None):
            return True
        else:
            return False


    def existeNickName(self, nickBusca):
        if (self.estaVacio()):
            return False
        else:
            return self.buscandoNick(self.raiz, nickBusca)


    def buscandoNick(self,nodoRaiz, nickSearch):
        nickAct = ""
        if (nodoRaiz != None):
            nickAct = nodoRaiz.nickname
        if(nodoRaiz == None):
            return False
        elif (nickSearch == nickAct):
            return True
        elif (nickSearch < nickAct):
            return self.buscandoNick(nodoRaiz.izquierda, nickSearch)
        else:
            return self.buscandoNick(nodoRaiz.derecha, nickSearch)


    def insertarPlayerArbolJugadores(self, nicknam, passwo, conec):
        seInserto = False;
        if (self.estaVacio()):
            nuevoPlayer = NodoPlayer.NodoPlayer()
            nuevoPlayer.nickname =  nicknam
            nuevoPlayer.password = passwo
            nuevoPlayer.estaConectado = conec
            self.raiz = nuevoPlayer
            self.cantidad = self.cantidad + 1
            seInserto = True
            print "Ingresado con exito"

        else:
            if (self.existeNickName(nicknam)==True):
                print "Usuario ya existe"
                return self.raiz
            else:
                nodo = self.insertando(self.raiz, nicknam, passwo , conec, seInserto)
                if(nodo!=None):
                    seInserto = True
        return seInserto


    def insertando(self, nodoRaiz, nicknam, passwo , conec, seInserto):
        if(nodoRaiz == None):
            nuevoPlayer = NodoPlayer.NodoPlayer()
            nuevoPlayer.nickname =  nicknam
            nuevoPlayer.password = passwo
            nuevoPlayer.estaConectado = conec
            nodoRaiz = nuevoPlayer
            self.cantidad = self.cantidad + 1
            seInserto = True
            return nodoRaiz
        elif (nicknam < nodoRaiz.nickname):
            nodoRaiz.izquierda = (self.insertando(nodoRaiz.izquierda,nicknam, passwo , conec ,seInserto))
            return nodoRaiz
        else:
            nodoRaiz.derecha = self.insertando(nodoRaiz.derecha, nicknam,passwo , conec,  seInserto)
            return nodoRaiz


    def loguearJugador(self, nickn, passw):
        seEncontro = False
        if(self.estaVacio()):
            print "Arbol vacio"
        else:
            aux = self.raiz
            nodoooo = self.logueandoPlayer(self.raiz, nickn, passw)
            if nodoooo==None:
               seEncontro=False
            else:
                seEncontro=True
        if seEncontro==False:
            print "No se pudo loguear con los datos nickname: "+ nickn +" Password: " +passw
        else:
            print "Felicidades se a podido loguear con user: "+nickn + " y Password: " + passw
        return seEncontro


    def logueandoPlayer(self, nodoRaiz, nickn, passw):
        if (nodoRaiz==None):
            return None
        else:
            nicAct = nodoRaiz.nickname
            passAct = nodoRaiz.password
            if (nodoRaiz == None):
                return None
            elif (nickn == nicAct and passw == passAct):
                print "*************************************************************************************"
                print "*************Felicidades aca se comprobo el nickname y la clave**********************"
                print "**** Te logueaste con NickName:  "+nickn+"  y Password: "+ passw +"  ***************"
                print "*************************************************************************************"
                nodoRaiz.estaConectado = True
                return nodoRaiz
            elif (nickn < nicAct):
                return self.logueandoPlayer(nodoRaiz.izquierda, nickn , passw)
            else:
                return self.logueandoPlayer(nodoRaiz.derecha, nickn , passw)


    def buscarUsuarioUsuarioEnArbol(self, nick):
        if (self.estaVacio() == True):
            return None
        else:
            return self.searchJugador(self.raiz, nick)


    def searchJugador(self, nodoRaiz, nickn):
        if (nodoRaiz==None):
            return None
        else:
            nicAct = nodoRaiz.nickname
            if (nodoRaiz == None):
                return None
            elif (nickn == nicAct):
                return nodoRaiz
            elif (nickn < nicAct):
                return self.searchJugador(nodoRaiz.izquierda, nickn)
            else:
                return self.searchJugador(nodoRaiz.derecha, nickn)


    def podarArbolUsuarioEnArbol(self, nodoRaiz):
        if(nodoRaiz):
            nodoRaiz.izquierda = self.podarArbolUsuarioEnArbol(nodoRaiz.izquierda)
            nodoRaiz.derecha = self.podarArbolUsuarioEnArbol(nodoRaiz.derecha)
            nodoRaiz = None


    def podarArbolUsuarioEnArbolCompleto(self):
        if(estaVacio()):
            print "No hay elemento en el arbol"
        else:
            self.podarArbolUsuarioEnArbol(self.raiz)
            self.raiz = None


    def GenerarArbolUsuarios(self, Nodom, archivo):
        if Nodom!=None:
            archivo.write((Nodom.nickname.replace(" ","_")+"[label=\"Nickname: "+ Nodom.nickname.replace(" ","_")+ " \n Password: " + Nodom.password +"\" color=blue fillcolor = red style=\"rounded,filled\" ]\n"))
            if Nodom.izquierda!=None:
                archivo.write((Nodom.nickname.replace(" ","_")+"->"+Nodom.izquierda.nickname.replace(" ","_")+"\n"))
            if Nodom.derecha!=None:
                archivo.write((Nodom.nickname.replace(" ","_")+"->"+Nodom.derecha.nickname.replace(" ","_")+"\n"))
            self.GenerarArbolUsuarios(Nodom.izquierda,archivo)
            self.GenerarArbolUsuarios(Nodom.derecha,archivo)


    def GenerarArbolUsuariosCompleto(self, Nodom, archivo):
        if Nodom!=None:
            archivo.write((Nodom.nickname.replace(" ","_")+"[label=\"Nickname: "+ Nodom.nickname.replace(" ","_")+ " \n Password: " + Nodom.password +"\" color=blue fillcolor = red style=\"rounded,filled\" ]\n"))
            if (Nodom.listaGamesUser != None):
                Nodom.listaGamesUser.escribirListaDobleDeJuegos2(Nodom.nickname, archivo)
            if Nodom.izquierda!=None:
                archivo.write((Nodom.nickname.replace(" ","_")+"->"+Nodom.izquierda.nickname.replace(" ","_")+"\n"))
            if Nodom.derecha!=None:
                archivo.write((Nodom.nickname.replace(" ","_")+"->"+Nodom.derecha.nickname.replace(" ","_")+"\n"))
            self.GenerarArbolUsuariosCompleto(Nodom.izquierda,archivo)
            self.GenerarArbolUsuariosCompleto(Nodom.derecha,archivo)
##            self.GenerarArbolUsuarios(Nodom.izquierda,archivo)
##            self.GenerarArbolUsuarios(Nodom.derecha,archivo)


    def GenerarDot(self):
        self.crearCarpeta()
        filename =self.Path +"arbolABBUsuarios.dot"
        ArchivoABB = open(filename,'w')
       ##esta linea es para que el nodo vaya lleno
##       ArchivoAVL.write(("digraph Arbol {node [shape=ellipse style = filled];\n"))
        ArchivoABB.write(("digraph Arbol { \n node[shape=rectangle fontsize=\"12.0\"];\n"))
##        self.GenerarArbolUsuarios(self.raiz, ArchivoABB)
        self.GenerarArbolUsuariosCompleto(self.raiz, ArchivoABB)
        altura = self.AlturaArbolABB(self.raiz)
        cantidadNodos = self.CantidadNodosArbolABB(self.raiz)
        niveles = altura - 1
        ArchivoABB.write("666[ color=blue label = \"Datos del Arbol \n \n " +" Altura: "+ str(altura) + "\n " + "Niveles: " + str(niveles) +"\n " +"# de Nodos: " +str(cantidadNodos)  +"\" fontsize=\"12.0\" ] \n")
        ArchivoABB.write(" \n label = \" Arbol de Usuarios Registrados   \"  \n ")
        ArchivoABB.write('}')
        ArchivoABB.close()


    def verImagenCompleta(self):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ self.Path+'arbolABBUsuarios.dot -o '+self.Path+'arbolABBUsuarios.jpg'
        os.system(miComandooo)
        os.popen(self.Path+'arbolABBUsuarios.jpg')


    def crearCarpeta(self):
        try: os.makedirs(self.Path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise


    def CantidadNodosArbolABB(self, nodoA):
        cont = 0
        if nodoA==None:
            cont=0
        else:
            cont = cont + 1 + self.CantidadNodosArbolABB(nodoA.izquierda) + self.CantidadNodosArbolABB(nodoA.derecha)
        return cont


    def AlturaArbolABB(self, nodoRaiz):
        if nodoRaiz==None:
            return 0
        else:
            return 1 + max(self.AlturaArbolABB(nodoRaiz.izquierda),self.AlturaArbolABB(nodoRaiz.derecha))


    def esHoja(self, nodo):
        if(nodo.izquierda ==None and nodo.derecha ==None):
            return True
        else:
            return False


    def vacio(self, nodo):
        if(nodo ==None):
            return True
        else:
            return False


    def eliminarUsuarioArbolNodoPlayer(self, nick):
        if(self.estaVacio()==True):
            print "Esta Vacio el arbol"
            return None
        else:
            return self.eliminandoUsuarioArbolNodoPlayer(self.raiz, nick)


    def eliminandoUsuarioArbolNodoPlayer(self, nodoRaiz, nick):
        if nodoRaiz == None:
            print "nodo no existe"
            return None
        elif(nick < nodoRaiz.nickname):
            return self.eliminandoUsuarioArbolNodoPlayer(nodoRaiz.izquierda, nick)
        elif(nick > nodoRaiz.nickname):
            return self.eliminandoUsuarioArbolNodoPlayer(nodoRaiz.derecha , nick)
        else:
            quitar = nodoRaiz
            if(quitar.izquierda == None):
                nodoRaiz = quitar.derecha
            elif(quitar.derecha ==None):
                nodoRaiz = quit.izquierda
            else:
                quitar = self.reemplazarNodoEliminando(quitar)
            quitar = None
        return nodoRaiz


    def reemplazarNodoEliminando(self, actQuitar):
        act = None
        temp = None
        temp = actQuitar
        act = actQuitar.izquierda
        while (act.derecha != None):
            temp = act
            act = act.derecha
        actQuitar.nickname = act.nickname
        actQuitar.password = act.password
        actQuitar.listaGamesUser = act.listaGamesUser
        actQuitar.estaConectado = act.estaConectado
        actQuitar.matrizOrtogonalUser = act.matrizOrtogonalUser
        if(temp == actQuitar):
            temp.izquierda = act.izquierda
        else:
            temp.derecha = act.derecha
        return act

    def GenerarDotArreglado(self):
        self.crearCarpeta()
        filename =self.Path +"arbolABBUsuarios.dot"
        ArchivoABB = open(filename,'w')
        ArchivoABB.write("digraph Arbol {\n")
        ArchivoABB.write("      node [shape= \"record\" style=filled, fillcolor=bisque color=blue ];\n")
        ArchivoABB.write("      edge[color= black];\n")

        self.GenerarArbol(self.raiz, ArchivoABB)

        altura = self.AlturaArbolABB(self.raiz)
        cantidadNodos = self.CantidadNodosArbolABB(self.raiz)
        niveles = altura - 1
        hojas = 0
        ramas = 0
        hojas = self.cantidadNodosHoja()
        ramas = cantidadNodos - hojas - 1
        ArchivoABB.write("      info666[ color=blue label = \"Datos del Arbol \\n " +" Altura: "+ str(altura) + "\\n " + "Niveles: " + str(niveles) +"\\n " +"# de Nodos: " +str(cantidadNodos)  + "\\n " + "# de Hojas: " + str(hojas) +"\\n " + "# de Ramas: " + str(ramas) +"\" fontsize=\"12.0\" ] \n")
        ArchivoABB.write(" \n         label = \" Arbol de Usuarios Registrados   \"  \n ")
        ArchivoABB.write('}')
        ArchivoABB.close()


    def GenerarArbol(self, Nodo, ArchivoABB):
        if(Nodo != None):

            ArchivoABB.write("       "+ Nodo.nickname + "       [label= \"<f0> Izq |<f1> "+ "Nickname: "+ Nodo.nickname.replace(" ","_")+ " \\n Password: " + Nodo.password + " \\n" + self.obtenerConectado(Nodo.estaConectado) + " \n |<f2> Der\" color=blue fillcolor = red style=\"rounded,filled\" ];\n")

            if (Nodo.listaGamesUser != None):
                Nodo.listaGamesUser.escribirListaDobleDeJuegos2(Nodo.nickname, ArchivoABB)

            if(Nodo.izquierda != None):
                ArchivoABB.write("       "+ Nodo.nickname+":f0 -> "+ Nodo.izquierda.nickname+":f1;\n")

            if(Nodo.derecha != None):
                ArchivoABB.write("       "+ Nodo.nickname +":f2 -> " + Nodo.derecha.nickname+":f1;\n")

            self.GenerarArbol(Nodo.izquierda, ArchivoABB)
            self.GenerarArbol(Nodo.derecha, ArchivoABB)


    def cantidadNodosHoja(self):
        cant = 0
        cant = self.cantidadNodosHojas(self.raiz,cant);
        return cant;


    def cantidadNodosHojas(self, nRaiz,cant):
        if (nRaiz != None):
            if(nRaiz.izquierda == None and nRaiz.derecha == None):
                cant = cant + 1
            cant = self.cantidadNodosHojas(nRaiz.izquierda,cant)
            cant = self.cantidadNodosHojas(nRaiz.derecha,cant)
        return cant


    def leerArchivoDotEspejo(self):
##        self.GenerarDot()
        filename =self.Path +"arbolEspejoABBUsuarios.dot"
        ArchivoABB = open(filename,'r')
        contenido = ArchivoABB.read()
        return contenido


    def leerArchivoDot(self):
##        self.GenerarDot()
        filename =self.Path +"arbolABBUsuarios.dot"
        ArchivoABB = open(filename,'r')
        contenido = ArchivoABB.read()
        return contenido


    def obtenerConectado(self, conec):
        if(conec == True):
            return "Online"
        else:
            return "Offline"


    def copiarNodoArbol(self, origen):
        nuevo = NodoPlayer.NodoPlayer()
        nuevo.nickname = origen.nickname
        nuevo.password = origen.password
        nuevo.estaConectado = origen.estaConectado
        return nuevo


    def realizarEspejo(self, origen, destino):
        raizEspejo = self.copiarNodoArbol(origen)
        destino = raizEspejo
        self.procesoEspejo(origen, destino)
        return destino


    def arbolEspejo(self, arbolOrigen):
        espejo = NodoPlayer.NodoPlayer()
        espejo.nickname = arbolOrigen.nickname
        espejo.password = arbolOrigen.password
        espejo.estaConectado = arbolOrigen.estaConectado
        espejo  = self.realizarEspejo(arbolOrigen, espejo)
        return espejo


    def procesoEspejo(self, raiz, espejo):
        auxIz = None
        auxDer = None
        if(raiz == None):
            return
        else:
            if(raiz.izquierda!=None):
                auxIz = self.copiarNodoArbol(raiz.izquierda)
            else:
                auxIz = None
            if (raiz.derecha!=None):
                auxDer = self.copiarNodoArbol(raiz.derecha)
            else:
                auxDer = None
            espejo.izquierda = auxDer
            espejo.derecha = auxIz
            self.procesoEspejo(raiz.izquierda, espejo.derecha)
            self.procesoEspejo(raiz.derecha , espejo.izquierda)


    def GenerarDotEspejo(self, arbol):
        self.crearCarpeta()
        filename =self.Path +"arbolEspejoABBUsuarios.dot"
        ArchivoABBEspejo = open(filename,'w')
        ArchivoABBEspejo.write("digraph Arbol {\n")
        ArchivoABBEspejo.write("      node [shape= \"record\" style=filled, fillcolor=bisque color=blue ];\n")
        ArchivoABBEspejo.write("      edge[color= black];\n")

        self.GenerarArbolEspejo(arbol, arbol, ArchivoABBEspejo)

        altura = self.AlturaArbolABB(self.raiz)
        cantidadNodos = self.CantidadNodosArbolABB(self.raiz)
        niveles = altura - 1
        hojas = 0
        ramas = 0
        hojas = self.cantidadNodosHoja()
        ramas = cantidadNodos - hojas - 1
        ArchivoABBEspejo.write("      info666[ color=blue label = \"Datos del Arbol \\n " +" Altura: "+ str(altura) + "\\n " + "Niveles: " + str(niveles) +"\\n " +"# de Nodos: " +str(cantidadNodos)  + "\\n " + "# de Hojas: " + str(hojas) +"\\n " + "# de Ramas: " + str(ramas) +"\" fontsize=\"12.0\" shape=box ] \n")
        ArchivoABBEspejo.write(" \n         label = \" Arbol Espejo de Usuarios Registrados   \"  \n ")
        ArchivoABBEspejo.write('}')
        ArchivoABBEspejo.close()


    def GenerarArbolEspejo(self, arbol, Nodo, ArchivoABBEspejo):
            if(Nodo!=None):
                ArchivoABBEspejo.write(Nodo.nickname + " [label= \"<f0> Izq |<f1> " + "Nickname: "+ Nodo.nickname.replace(" ","_")+ " \\n Password: " + Nodo.password + " \\n" + self.obtenerConectado(Nodo.estaConectado)  + " |<f2> Der\" color=blue fillcolor = red style=\"rounded,filled\"  ];\n")

                if(Nodo.izquierda != None):
                    ArchivoABBEspejo.write(Nodo.nickname + ":f0 -> "+ Nodo.izquierda.nickname+":f1;\n")

                if(Nodo.derecha != None):
                    ArchivoABBEspejo.write(Nodo.nickname+":f2 -> "+Nodo.derecha.nickname+":f1;\n")

                self.GenerarArbolEspejo(arbol,Nodo.izquierda, ArchivoABBEspejo)
                self.GenerarArbolEspejo(arbol,Nodo.derecha, ArchivoABBEspejo)

    def obtenerListadoPlayersBestWinner(self):
        cadena = ""
        lista2=[]
        del lista2[:]
        if(self.raiz==None):
            return "No hay usuarios"
        else:
            self.obteniendoListadoPlayerBestWinners(lista2, self.raiz)
        lista2.sort(key=lambda player: player[0], reverse=True)
        for elem in lista2:
            cadena = cadena + str(elem[0])+ "," + str(elem[1])
        print cadena
        return cadena

    def obteniendoListadoPlayerBestWinners(self, lista666, Nodo):
        if Nodo==None:
            return
        else:
            self.obteniendoListadoPlayerBestWinners(lista666, Nodo.izquierda)
            lista666.append((Nodo.listaGamesUser.obtenerCantidadJuegosGanados(), Nodo.nickname + "__"))
            self.obteniendoListadoPlayerBestWinners(lista666, Nodo.derecha)
        return lista666

    def obtenerListadoPlayersBestShooter(self):
        cadena = ""
        lista2=[]
        del lista2[:]
        if(self.raiz==None):
            return "No hay usuarios"
        else:
            self.obteniendoListadoPlayerBestShooters(lista2, self.raiz)
        lista2.sort(key=lambda player: player[0], reverse=True)
        for elem in lista2:
            cadena = cadena + str(elem[0])+ "," + str(elem[1])
        print cadena
        return cadena

    def obteniendoListadoPlayerBestShooters(self, lista666, Nodo):
        if Nodo==None:
            return
        else:
            self.obteniendoListadoPlayerBestShooters(lista666, Nodo.izquierda)
##            ff = Nodo.listaGamesUser.obtenerPorcentajeTirosAcertados()
##            print ff
            lista666.append((Nodo.listaGamesUser.obtenerPorcentajeTirosAcertados(), Nodo.nickname + "__"))
            self.obteniendoListadoPlayerBestShooters(lista666, Nodo.derecha)
        return lista666






