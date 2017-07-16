#-------------------------------------------------------------------------------
# Name:        clase arbolAVLContactos
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     05/07/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoPlayer
import subprocess
import os.path
import errno
import os

class arbolAVLContactos:


    def __init__(self):
        self.Raiz=None
        self.cantidad=0
        self.nodito=None
        self.Altur = False
        self.Path="C:/Proyecto/EDDVacasJunio/"
        self.archivoDotDevolver = []


    def getRaiz(self):
        return self.Raiz


    def getNodito(self):
        return self.nodito


    def arbolEstaVacio(self, nodoR):
        return (nodoR==None)


    def setNodito(self,noditor):
        self.nodito=noditor


    ##recibe el nick a buscar y el nodo raiz
    def verificarNick(self, nickname, nodorr):
        Aux=nodorr
        seudonimo=False
##        nickname= nickname.upper()
        while Aux!=None:
            userNombre= Aux.nickname
##            userNombre= userNombre.upper()
            if nickname==userNombre:
                seudonimo=True
                Aux=None
            else:
                if nickname>userNombre:
                    Aux = Aux.derecha
                else:
                    Aux = Aux.izquierda
                    if Aux==None:
                        seudonimo = False
        return seudonimo


    def insertarUsuario(self, nickname, contrasenia, conectado):

        if (self.verificarNick(nickname,self.Raiz)==False):
            info = NodoPlayer.NodoPlayer()
            info.inicializarNodoPlayer(nickname, contrasenia, conectado)
            self.Raiz = self.insertarBalanceado(self.Raiz,info)
            print "Ingresado con exito!!!"
        else:
            print "Error Nickname repetido" ##aca puedo hacer el link si el usuario ya existe


    def insertarBalanceado(self,nodoRaiz, nodoInsertar):
        N1 = None
        info = nodoInsertar
        if self.arbolEstaVacio(nodoRaiz):
            nodoRaiz = info
            print "Se inserto un nuevo Contacto"
            self.Altur = True
        else:
            if nodoInsertar.nickname < nodoRaiz.nickname:
                nodoRaiz.izquierda = self.insertarBalanceado(nodoRaiz.izquierda,nodoInsertar)
                if self.Altur:
                    if nodoRaiz.factorBalance==1:
                        nodoRaiz.factorBalance=0
                        self.Altur = False
                    elif nodoRaiz.factorBalance==0:
                        nodoRaiz.factorBalance=-1
                    ## aca reestructuro porque sino pasaria a valer -2
                    ## y se desequilibra por la izquierda
                    elif nodoRaiz.factorBalance==-1:
                        N1 = nodoRaiz.izquierda
                        if(N1.factorBalance==-1):
                            nodoRaiz = self.RotacionIzquierdaIzquierda(nodoRaiz,N1)
                        else:
                            nodoRaiz = self.RotacionIzquierdaDerecha(nodoRaiz,N1)
                        self.Altur = False
            else:
                if nodoInsertar.nickname > nodoRaiz.nickname:
                    nodoRaiz.derecha = self.insertarBalanceado(nodoRaiz.derecha,nodoInsertar)
                    if self.Altur:
                        if nodoRaiz.factorBalance==-1:
                            nodoRaiz.factorBalance=0
                            self.Altur=False
                        elif nodoRaiz.factorBalance==0:
                            nodoRaiz.factorBalance=1
                        elif nodoRaiz.factorBalance==1:
                            N1 = nodoRaiz.derecha
                            if N1.factorBalance==1:
                                nodoRaiz = self.RotacionDerechaDerecha(nodoRaiz,N1)
                            else:
                                nodoRaiz = self.RotacionDerechaIzquierda(nodoRaiz,N1)
                            self.Altur=False
                else:
                    print "Error: No pueden haber 2 nickname iguales"
                    self.Altur = False
        return nodoRaiz


    def RotacionIzquierdaIzquierda(self, nodoN, nodoN1):

        nodoN.izquierda = nodoN1.derecha
        nodoN1.derecha = nodoN

        if nodoN1.factorBalance==-1:
            nodoN.factorBalance =0
            nodoN1.factorBalance=0
        else:
            nodoN.factorBalance=-1
            nodoN1.factorBalance=1

        nodoN = nodoN1

        return nodoN


    def RotacionDerechaDerecha(self, nodoN, nodoN1):

        nodoN.derecha = nodoN1.izquierda
        nodoN1.izquierda = nodoN

        if nodoN1.factorBalance==1:
            nodoN.factorBalance =0
            nodoN1.factorBalance=0
        else:
            nodoN.factorBalance=1
            nodoN1.factorBalance=-1

        nodoN = nodoN1

        return nodoN


    def RotacionIzquierdaDerecha(self, nodoN, nodoN1):

        nodoN2 = None
        nodoN2 = nodoN1.derecha
        nodoN.izquierda = nodoN2.derecha
        nodoN2.derecha = nodoN
        nodoN1.derecha = nodoN2.izquierda
        nodoN2.izquierda = nodoN1

        if nodoN2.factorBalance==1:
            nodoN1.factorBalance=-1
        else:
            nodoN1.factorBalance=0
        if nodoN2.factorBalance==-1:
            nodoN.factorBalance=1
        else:
            nodoN.factorBalance=0

        nodoN2.factorBalance =0
        nodoN=nodoN2

        return nodoN


    def RotacionDerechaIzquierda(self, nodoN, nodoN1):

        nodoN2 = None
        nodoN2 = nodoN1.izquierda
        nodoN.derecha = nodoN2.izquierda
        nodoN2.izquierda = nodoN
        nodoN1.izquierda = nodoN2.derecha
        nodoN2.derecha = nodoN1

        if nodoN2.factorBalance==1:
            nodoN.factorBalance=-1
        else:
            nodoN.factorBalance=0
        if nodoN2.factorBalance==-1:
            nodoN1.factorBalance=1
        else:
            nodoN1.factorBalance=0

        nodoN2.factorBalance =0
        nodoN=nodoN2

        return nodoN


    def CantidadNodosAvl(self, nodoA):
        cont = 0
        if nodoA==None:
            cont=0
        else:
            cont = cont + 1 + self.CantidadNodosAvl(nodoA.izquierda) + self.CantidadNodosAvl(nodoA.derecha)
        return cont


    def AlturaArbol(self, nodoRaiz):
        if nodoRaiz==None:
            return 0
        else:
            return 1 + max(self.AlturaArbol(nodoRaiz.izquierda),self.AlturaArbol(nodoRaiz.derecha))


    def PreOrdenAvl(self,Nodo):
        if Nodo==None:
            return
        else:
            ##aca lo puedo meter en un arraylist
            print Nodo.nickname + " \n"
            self.PreOrdenAvl(Nodo.izquierda)
            self.PreOrdenAvl(Nodo.derecha)


    def InordenAvl(self, Nodo):
        if Nodo==None:
            return
        else:
            self.InordenAvl(Nodo.izquierda)
            print Nodo.nickname +" \n"
            ##aca lo puedo meter en un arraylist
            self.InordenAvl(Nodo.derecha)


    def PostOrdenAvl(self,Nodo):
        if Nodo==None:
            return
        else:
            self.PostOrdenAvl(Nodo.izquierda)
            self.PostOrdenAvl(Nodo.derecha)
            print Nodo.nickname +" \n"
            ##aca lo puedo meter a u arraylist


    def LocalizarUsuario(self, nodoRaiz, nickk):
##        nickk=nickk.upper()
        nic2 = ""
        nic2 = nodoRaiz.nickname
##        nic2 = nic2.upper()
        if nodoRaiz==None:
            return None
        elif nickk==nic2:
            return nodoRaiz
        elif nickk < nic2:
            return self.LocalizarUsuario(nodoRaiz.izquierda,nickk)
        else:
            return self.LocalizarUsuario(nodoRaiz.derecha,nickk)


    def Buscar(self, nickBuscado):
        dato =""
        dato = nickBuscado
        if self.Raiz==None:
            return None
        else:
            return self.LocalizarUsuario(self.Raiz,dato)


    def eliminarContacto(self, nickEliminar):
##        nickEliminar= nickEliminar.upper()
        valor = nickEliminar
        flag = True
        ##raiz = self.borrarAvl(self.Raiz,valor,flag)
        self.Raiz = self.borrarAvl(self.Raiz,valor,flag)


    def borrarAvl(self, nodoR, clave, cambiarAltura):
        cla =""
        cla = nodoR.nickname
##        cla=cla.upper()
##        clave=clave.upper()
        if nodoR==None:
            print "Nodo no encontrado"
        elif clave < cla:
            izq = self.borrarAvl(nodoR.izquierda, clave, cambiarAltura)
            nodoR.izquierda = izq
            if cambiarAltura:
                nodoR = self.Equilibrar1(nodoR, cambiarAltura)

        elif clave > cla:
            dere = self.borrarAvl(nodoR.derecha,clave,cambiarAltura)
            nodoR.derecha = dere
            if cambiarAltura:
                nodoR = self.Equilibrar2(nodoR,cambiarAltura)
        else: ##nodo encontrado
            nodoQ = nodoR
            if nodoQ.izquierda==None: ##solo tiene rama derecha
                nodoR=nodoQ.derecha
                cambiarAltura = False
            elif nodoQ.derecha==None: ##solo tiene rama izquierda
                nodoR = nodoQ.izquierda
                cambiarAltura = False
            else: ##si tiene rama izquierda y derecha
                iz = self.Reemplazar(nodoR,nodoR.izquierda,cambiarAltura)
                nodoR.izquierda = iz
                if cambiarAltura:
                    nodoR = self.Equilibrar1(nodoR,cambiarAltura)
            nodoQ = None
        return nodoR


    def Reemplazar(self, N, actual, cambiarAltur):
        if actual.derecha!=None:
            de = self.Reemplazar(N, actual.derecha,cambiarAltur)
            actual.derecha = de
            if cambiarAltur:
                actual = self.Equilibrar2(actual,cambiarAltur)
        else:
            N.nickname = actual.nickname
            N = actual
            actual = actual.izquierda
            N = None
            cambiarAltur =False
        return actual


    def Equilibrar1(self, N, cambiaAlturr):

        N1 = None
        if N.factorBalance==-1:
            N.factorBalance=0

        elif N.factorBalance==0:
            N.factorBalance =1
            cambiaAlturr=False

        elif N.factorBalance==1:
            N1 = N.derecha
            if N1.factorBalance>=0:
                if N1.factorBalance==0:
                    cambiaAlturr=True
                N = self.RotacionDerechaDerecha(N,N1)
            else:
                N = self.RotacionDerechaIzquierda(N,N1)
        return N


    def Equilibrar2(self, N,cambioAlturrr):
        N1=None
        if N.factorBalance ==-1:
            N1 = N.izquierda
            if N1.factorBalance<=0:
                if N1.factorBalance==0:
                    cambioAlturrr=False
                N=self.RotacionIzquierdaIzquierda(N,N1)
            else:
                N=self.RotacionIzquierdaDerecha(N,N1)
        elif N.factorBalance==0:
            N.factorBalance=-1
            cambioAlturrr=True
        elif N.factorBalance==1:
            N.factorBalance=0
        return N


    def loguearUsuario(self, nickn, clavee):
        seEncontro=False
        datoss = nickn
        if self.Raiz==None:
            seEncontro=False
        else:
            nodoooo = self.LocalizarUsuarioLoguear(self.Raiz,datoss,clavee)
            if nodoooo==None:
               seEncontro=False
            else:
                seEncontro=True
        if seEncontro==False:
            print "No se pudo loguear con los datos nickname: "+ nickn +" Password:" +clavee
        else:
            print "Felicidades se a podido loguear con user: "+nickn + " y Password: " + clavee

        return seEncontro


    def LocalizarUsuarioLoguear(self, nodoRaiz, nickk, claveee):

        if nodoRaiz==None:
            return None
        else:
            nic2 = nodoRaiz.nickname
            codd = nodoRaiz.password
        if nodoRaiz==None:
            return None
        elif nickk==nic2 and claveee==codd:
            print "*************************************************************************************"
            print "*************Felicidades aca se comprobo el nickname y la clave**********************"
            print "**** Te logueaste con NickName:  "+nickk+"  y Password: "+claveee +"  ***************"
            print "*************************************************************************************"
            return nodoRaiz
        elif nickk < nic2:
            return self.LocalizarUsuarioLoguear(nodoRaiz.izquierda,nickk,claveee)
        else:
            return self.LocalizarUsuarioLoguear(nodoRaiz.derecha,nickk,claveee)


    def devolverListadoUsuarios(self, Nodo,lista666):
        if Nodo==None:
            return
        else:
            self.devolverListadoUsuarios(Nodo.izquierda,lista666)
            ##print "id "+Nodo.IdUnico+"llega a: "+Nodo.LugarLlegada + " Lugar salida "+ Nodo.LugarSalida + " \n"
            lista666.append(Nodo)
            ##aca lo puedo meter en un arraylist
            self.devolverListadoUsuarios(Nodo.derecha,lista666)
        return lista666


    def ObtenerTodosUsuarios(self):
        lista2=[]
        del lista2[:]
        lista2 = self.devolverListadoUsuarios(self.Raiz, lista2)
        return lista2


    def GenerarArbolAVL(self, Nodo, ArchivoAVL):
        if(Nodo != None):

            ArchivoAVL.write("       "+ Nodo.nickname.replace(" ","_") + "       [label= \"<f0> Izq |<f1> "+ "Nickname: "+ Nodo.nickname+ " \\n Password: " + Nodo.password + " \n |<f2> Der\" color=blue fillcolor = red style=\"rounded,filled\" ];\n")

            if(Nodo.izquierda != None):
                ArchivoAVL.write("       "+ Nodo.nickname.replace(" ","_")+":f0 -> "+ Nodo.izquierda.nickname.replace(" ","_")+":f1;\n")

            if(Nodo.derecha != None):
                ArchivoAVL.write("       "+ Nodo.nickname.replace(" ","_") +":f2 -> " + Nodo.derecha.nickname.replace(" ","_")+":f1;\n")

            self.GenerarArbolAVL(Nodo.izquierda, ArchivoAVL)
            self.GenerarArbolAVL(Nodo.derecha, ArchivoAVL)



    def GenerarDotAVL(self, padre):
        filename =self.Path + padre.replace(" ","_")+"_" +"arbolAVLUsuarios.dot"
        ArchivoAVL = open(filename,'w')
        ArchivoAVL.write("digraph Arbol {\n")
        ArchivoAVL.write("      node [shape= \"record\" style=filled, fillcolor=bisque color=blue ];\n")
        ArchivoAVL.write("      edge[color= black];\n")

        self.GenerarArbolAVL(self.Raiz, ArchivoAVL)

        altura = self.AlturaArbol(self.Raiz)
        cantidadNodos = self.CantidadNodosAvl(self.Raiz)
        niveles = altura - 1
        hojas = 0
        ramas = 0
        hojas = self.cantidadNodosHoja()
        ramas = cantidadNodos - hojas - 1
        ArchivoAVL.write("      info666[ color=blue label = \"Datos del Arbol \\n " +" Altura: "+ str(altura) + "\\n " + "Niveles: " + str(niveles) +"\\n " +"# de Nodos: " +str(cantidadNodos)  + "\\n " + "# de Hojas: " + str(hojas) +"\\n " + "# de Ramas: " + str(ramas) +"\" fontsize=\"12.0\" ] \n")
        ArchivoAVL.write(" \n         label = \" Arbol AVL de Contactos de "+padre +" \"  \n ")
        ArchivoAVL.write('}')
        ArchivoAVL.close()


    def verImagenAVL(self, padre):
        miComandooo = 'dot -Tgif '+ self.Path+ padre.replace(" ","_")+"_" +'arbolAvlUsuarios.dot -o '+self.Path+ padre.replace(" ","_")+"_"+'arbolAvlUsuarios.jpg'
        os.system(miComandooo)
        os.popen(self.Path+padre.replace(" ","_")+"_" +'arbolAvlUsuarios.jpg')


    def leerArchivoDotAVL(self, padre):
        del self.archivoDotDevolver[:]
        miDot = open(self.Path+padre.replace(" ","_")+"_"+"arbolAvlUsuarios.dot",'r')
        for line in miDot:
            self.archivoDotDevolver.append(line)
            print(line)
        for m in self.archivoDotDevolver:
            print "Esto tiene mi linea "+m
        return self.archivoDotDevolver


    def crearCarpeta(self):
        try: os.makedirs(self.Path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def cantidadNodosHoja(self):
        cant = 0
        cant = self.cantidadNodosHojas(self.Raiz,cant);
        return cant;


    def cantidadNodosHojas(self, nRaiz,cant):
        if (nRaiz != None):
            if(nRaiz.izquierda == None and nRaiz.derecha == None):
                cant = cant + 1
            cant = self.cantidadNodosHojas(nRaiz.izquierda,cant)
            cant = self.cantidadNodosHojas(nRaiz.derecha,cant)
        return cant

    def GenerarDotAVLCompleto(self, padre, ArchivoAVL):
        if self.arbolEstaVacio(self.Raiz):
            print "Usuario: " + padre + " No tiene arbol de contactos"
            return
##        filename =self.Path +"arbolAVLUsuarios.dot"
##        ArchivoAVL = open(filename,'w')
        else:
            ArchivoAVL.write("subgraph Arbol {\n")
            ArchivoAVL.write("      node [shape= \"record\" style=filled, fillcolor=bisque color=blue ];\n")
            ArchivoAVL.write("      edge[color= black];\n")
            ArchivoAVL.write(padre.replace(" ","_") + "->" +padre.replace(" ","_") +"_"+self.Raiz.nickname.replace(" ","_")+ "\n")

            self.GenerarArbolAVLCompleto(self.Raiz, ArchivoAVL, padre)

            altura = self.AlturaArbol(self.Raiz)
            cantidadNodos = self.CantidadNodosAvl(self.Raiz)
            niveles = altura - 1
            hojas = 0
            ramas = 0
            hojas = self.cantidadNodosHoja()
            ramas = cantidadNodos - hojas - 1
            ArchivoAVL.write("      info666[ color=blue label = \"Datos del Arbol \\n " +" Altura: "+ str(altura) + "\\n " + "Niveles: " + str(niveles) +"\\n " +"# de Nodos: " +str(cantidadNodos)  + "\\n " + "# de Hojas: " + str(hojas) +"\\n " + "# de Ramas: " + str(ramas) +"\" fontsize=\"12.0\" ] \n")
            ArchivoAVL.write(" \n         label = \" Arbol AVL de Contactos de "+padre +" \"  \n ")
            ArchivoAVL.write('}')

    def GenerarArbolAVLCompleto(self, Nodo, ArchivoAVL, padre):
        if(Nodo != None):

            ArchivoAVL.write("       "+ padre.replace(" ","_")+"_"+ Nodo.nickname.replace(" ","_") + "       [label= \"<f0> Izq |<f1> "+ "Nickname: "+ Nodo.nickname+ " \\n Password: " + Nodo.password + " \n |<f2> Der\" color=blue fillcolor = gray style=\"rounded,filled\" ];\n")

            if(Nodo.izquierda != None):
                ArchivoAVL.write("       "+ padre.replace(" ","_")+"_"+ Nodo.nickname.replace(" ","_")+":f0 -> "+ padre.replace(" ","_")+"_"+ Nodo.izquierda.nickname.replace(" ","_")+":f1;\n")

            if(Nodo.derecha != None):
                ArchivoAVL.write("       "+ padre.replace(" ","_")+"_"+ Nodo.nickname.replace(" ","_") +":f2 -> " + padre.replace(" ","_")+"_"+ Nodo.derecha.nickname.replace(" ","_")+":f1;\n")

            self.GenerarArbolAVLCompleto(Nodo.izquierda, ArchivoAVL, padre)
            self.GenerarArbolAVLCompleto(Nodo.derecha, ArchivoAVL, padre)


    def GenerarDotAVLUnitario(self, padre):
        if self.arbolEstaVacio(self.Raiz):
            print "Usuario: " + padre + " No tiene arbol de contactos"
            return
        else:
            filename =self.Path +padre.replace(" ","_")+"_" +"arbolAVLUsuarios.dot"
            ArchivoAVL = open(filename,'w')
            ArchivoAVL.write("subgraph Arbol {\n")
            ArchivoAVL.write("      node [shape= \"record\" style=filled, fillcolor=bisque color=blue ];\n")
            ArchivoAVL.write("      edge[color= black];\n")
            ArchivoAVL.write(padre.replace(" ","_") + "->" +padre.replace(" ","_") +"_"+self.Raiz.nickname.replace(" ","_")+ "\n")

            self.GenerarArbolAVLUnitario(self.Raiz, ArchivoAVL, padre)

            altura = self.AlturaArbol(self.Raiz)
            cantidadNodos = self.CantidadNodosAvl(self.Raiz)
            niveles = altura - 1
            hojas = 0
            ramas = 0
            hojas = self.cantidadNodosHoja()
            ramas = cantidadNodos - hojas - 1
            ArchivoAVL.write("      info666[ color=blue label = \"Datos del Arbol \\n " +" Altura: "+ str(altura) + "\\n " + "Niveles: " + str(niveles) +"\\n " +"# de Nodos: " +str(cantidadNodos)  + "\\n " + "# de Hojas: " + str(hojas) +"\\n " + "# de Ramas: " + str(ramas) +"\" fontsize=\"12.0\" ] \n")
            ArchivoAVL.write(" \n         label = \" Arbol AVL de Contactos de "+padre +" \"  \n ")
            ArchivoAVL.write('}')

    def GenerarArbolAVLUnitario(self, Nodo, ArchivoAVL, padre):
        if(Nodo != None):

            ArchivoAVL.write("       "+ padre.replace(" ","_")+"_"+ Nodo.nickname.replace(" ","_") + "       [label= \"<f0> Izq |<f1> "+ "Nickname: "+ Nodo.nickname+ " \\n Password: " + Nodo.password + " \n |<f2> Der\" color=blue fillcolor = gray style=\"rounded,filled\" ];\n")

            if(Nodo.izquierda != None):
                ArchivoAVL.write("       "+ padre.replace(" ","_")+"_"+ Nodo.nickname.replace(" ","_")+":f0 -> "+ padre.replace(" ","_")+"_"+ Nodo.izquierda.nickname.replace(" ","_")+":f1;\n")

            if(Nodo.derecha != None):
                ArchivoAVL.write("       "+ padre.replace(" ","_")+"_"+ Nodo.nickname.replace(" ","_") +":f2 -> " + padre.replace(" ","_")+"_"+ Nodo.derecha.nickname.replace(" ","_")+":f1;\n")

            self.GenerarArbolAVLUnitario(Nodo.izquierda, ArchivoAVL, padre)
            self.GenerarArbolAVLUnitario(Nodo.derecha, ArchivoAVL, padre)

    def leerArchivoDotContactosAVL(self, padre):
##        self.GenerarDot()
        filename =self.Path +padre.replace(" ","_")+"_" +"arbolAVLUsuarios.dot"
        ArchivoABB = open(filename,'r')
        contenido = ArchivoABB.read()
        return contenido