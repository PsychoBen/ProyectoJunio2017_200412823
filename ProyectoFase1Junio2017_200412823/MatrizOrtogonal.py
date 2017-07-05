#-------------------------------------------------------------------------------
# Name:        clase matriz ortogonal
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoMatriz
import subprocess
import os.path
import errno
import os

class MatrizOrtogonal:

    def __init__(self):
        self.inicio = None
        self.actual = None
        self.nodoinsertado = None
        self.auxcab = None
        self.tamanio = 0
        self.Path = "C:/Proyecto/EDDVacasJunio/"

    def leerArchivoMatrizActual(self, padre):
##        self.GenerarDot()
        filename = padre +"_matrizOrtogonal_actual.dot"
        ArchivoABB = open(filename,'r')
        contenido = ArchivoABB.read()
        return contenido

    def leerArchivoMatrizInicial(self, padre):
##        self.GenerarDot()
        filename = padre +"_matrizOrtogonal_inicial.dot"
        ArchivoABB = open(filename,'r')
        contenido = ArchivoABB.read()
        return contenido

    def buscarDimension(self, cabeceraDimension, dimen):
        auxCabecera = None
        cabEncontrada = None
        encontrado = False
        auxCabecera = cabeceraDimension
        while (auxCabecera != None and encontrado!=True):
            if (auxCabecera.dimension == dimen):
                cabEncontrada = auxCabecera
                encontrado = True
            auxCabecera = auxCabecera.atras
        return cabEncontrada

    def buscarNodo3Dimensiones(self, nodoDimen, matriz, valo):
        colu = None
        filla = None
        nEncontrado = None
        encontrado = False
        colu = nodoDimen
        while (colu!= None and encontrado != True):
            filla = colu
            while (filla != None):
                if(filla.valor == valo):
                    nEncontrado = filla
                    encontrado = True
                filla = filla.abajo
            colu = colu.derecha
        return nEncontrado

    def insertarEnMatrizOrtogonal3Dimensiones(self, matriz, fil, col, dim, val, cad):
        nCol = None
        nFil = None
        nDim = None
        nuevo = NodoMatriz.nodoMatrizOrtogonal()
        nuevo.inicializarNodoMatrizOrtogonal_1(fil , col ,dim , val, "path image")
        nuevo.ocupado = False
        if(self.inicio == None):
            self.inicio =NodoMatriz.nodoMatrizOrtogonal()
            self.inicio.inicializarNodoMatrizOrtogonal_1(0,0,0,-1, "cabecera" );
            self.inicio.ocupado = True
            nDimCreada = self.buscarDimension(self.inicio, dim)
            if(nDimCreada ==None):
                self.crearDimension(dim, nuevo, matriz)
                nDimCreada = self.buscarDimension(self.inicio, dim)
            else:
                pass
            self.crearColumna2(col, nDimCreada, nuevo, matriz)
            self.crearFila2(fil, nDimCreada, nuevo, matriz)
##si el inicio de la matriz ya existe
## buscamos la dimension, columna y fila para insertar
        else:
            nDim = self.buscarDimension(self.inicio,dim)
            nodoEve = self.buscarNodo3Dimensiones(nDim, matriz,val)
            if(nodoEve != None):
                print "Existe el nodo"
            else:
                if (nDim == None): ## no existe la dimension
                    self.crearDimension(dim, nuevo, matriz)
                    nDim = self.buscarDimension(self.inicio, dim)
                    self.crearColumna2(col, nDim, nuevo, matriz)
                    self.crearFila2(fil, nDim, nuevo, matriz)
                else:
                    nCol = self.BuscarColumna2(nDim, self.inicio, col)
                    nFil = self.BuscarFila2(nDim, self.inicio, fil)
                    if(nCol == None):
                        self.crearColumna2(col,nDim, nuevo, matriz)
                    else:
                        self.insertarEnColumna2(nuevo, nCol, matriz, val)
                    if (nFil == None):
                        self.crearFila2(fil, nDim, nuevo, matriz)
                    else:
                        self.insertarEnFila2(nuevo, nFil, matriz, val)

##metodo para insertar en la dimension hallada
    def insertarEnDimension(self, nodoInsertar, nodoDim, matriz, val):
        anterior = None
        nuevo = nodoInsertar
        if(nodoDim == None):
            nodoDim = nuevo
        else:
            anterior = nodoDim
            matriz.actual = nodoDim
            while(matriz.actual != None and matriz.actual.dimension < nodoInsertar.dimension):
                anterior = matriz.actual
                matriz.actual = matriz.actual.atras
            if(matriz.actual == None):
                anterior.atras = nuevo
                nuevo.adelante = anterior
            else:
                if(matriz.actual.adelante == None):
                    nuevo.atras = nodoDim
                    nodoDim = nuevo
                    matriz.actual.adelante = nuevo
                else:
                    nuevo.atras = matriz.actual.adelante.atras
                    matriz.actual.adelante.atras = nuevo
                    nuevo.adelante = matriz.actual.adelante
                    matriz.actual.adelante = nuevo

    def crearDimension(self, dim, nodoInsertado, matriz):
        anterior = None
        aux = None
        nuevo = NodoMatriz.nodoMatrizOrtogonal()
        nuevo.inicializarNodoMatrizOrtogonal_1(0,0,dim, -1, "dimension")
        nuevo.ocupado = True
        if (matriz.inicio == None):
            matriz.inicio = nuevo
        else:
            matriz.actual = matriz.inicio
            anterior = matriz.inicio
            while(matriz.actual !=None and matriz.actual.dimension <= dim):
                anterior = matriz.actual;
                matriz.actual = matriz.actual.atras
            if (matriz.actual ==None):
                anterior.atras = nuevo
                nuevo.adelante = anterior
            else:
                if(matriz.actual.adelante == None):
                    nuevo.atras = matriz.inicio
                    matriz.inicio = nuevo
                    matriz.actual.adelante = nuevo
                else:
                    nuevo.atras = matriz.actual.adelante.atras
                    matriz.actual.adelante.atras = nuevo
                    nuevo.adelante =  matriz.actual.atras
                    matriz.actual.adelante = nuevo

    def escribirArchivoDot2(self, matriz):
        pass

    def mostrarElementosMatriz2(self):
        nCol = None
        nFil = None
        nDim = self.inicio
        conta = 1
        print "empiezan datos de matriz dispersa"
        while(nDim!=None):
            nFil = nDim
            print "?mpiezan dimension"
            while (nFil!=None):
                nCol = nFil
                while(nCol!=None):
                    print "valor: " + str(nCol.valor) + " fila: "+ str(nCol.fila)+" columna: " + str(nCol.columna) + " dimension: " + str(nCol.dimension)
                    nCol = nCol.derecha
                print ""
                nFil = nFil.abajo
            conta = conta + 1
            print "Final de la dimension"
            nDim = nDim.atras
        print "****************************************"
        print " Finalizan datos de la matriz otrogonal "
        print "****************************************"

    def crearColumna2(self, col, nodoDime, nodoInsertado, matriz):
        anterior = None
        nuevo = NodoMatriz.nodoMatrizOrtogonal()
        nuevo.inicializarNodoMatrizOrtogonal_1(0,col,nodoDime.dimension,0,"col")
        nuevo.ocupado = True
        nuevo.abajo = nodoInsertado
        nodoInsertado.arriba = nuevo
        if(matriz.inicio ==None):
            matriz.inicio = nuevo
        else:
            matriz.actual = nodoDime
            anterior = nodoDime
            while(matriz.actual !=None and matriz.actual.columna <=col):
                anterior = matriz.actual
                matriz.actual = matriz.actual.derecha
            if matriz.actual == None:
                anterior.derecha = nuevo
                nuevo.izquierda = anterior
            else:
                if matriz.actual.izquierda ==None:
                    nuevo.derecha = nodoDime
                    nodoDime = nuevo
                    matriz.actual.izquierda = nuevo
                else:
                    nuevo.derecha = matriz.actual.izquierda.derecha
                    matriz.actual.izquierda.derecha = nuevo
                    nuevo.izquierda = matriz.actual.izquierda
                    matriz.actual.izquierda = nuevo

    def crearFila2(self, fil, nodoDime, nodoInsertado, matriz):
        anterior = None
        nuevo = NodoMatriz.nodoMatrizOrtogonal()
        nuevo.inicializarNodoMatrizOrtogonal_1(fil,0, nodoDime.dimension, 0,"FILA")
        nuevo.ocupado = True
        nuevo.derecha = nodoInsertado
        nodoInsertado.izquierda = nuevo
        if(matriz.inicio == None):
            matriz.inicio = nuevo
        else:
            matriz.actual = nodoDime
            anterior = nodoDime
            while(matriz.actual!=None and matriz.actual.fila <=fil):
                anterior = matriz.actual
                matriz.actual = matriz.actual.abajo
            if (matriz.actual == None):
                anterior.abajo = nuevo
                nuevo.arriba = anterior
            else:
                if(matriz.actual.arriba == None):
                    nuevo.abajo = nodoDime
                    nodoDime = nuevo
                    matriz.actual.arriba = nuevo
                else:
                    nuevo.abajo =  matriz.actual.arriba.abajo
                    matriz.actual.arriba.abajo = nuevo
                    nuevo.arriba = matriz.actual.arriba
                    matriz.actual.arriba = nuevo

    def BuscarColumna2(self,nodoDime, cabeceraCol, col):
        auxCabecera =None
        CabEncontrada = None
        encontrado = False
        auxCabecera = nodoDime
        while(auxCabecera != None and encontrado != True):
            if(auxCabecera.columna == col):
                CabEncontrada = auxCabecera
                encontrado = True
            auxCabecera = auxCabecera.derecha
        return CabEncontrada

    def BuscarFila2(self, nodoDime, cabeceraFila, fila):
        auxCabecera = None
        CabEncontada = None
        encontrado = False
        auxCabecera = nodoDime
        while(auxCabecera !=None and encontrado!= True):
            if(auxCabecera.fila == fila):
                CabEncontada = auxCabecera
                encontrado = True
            auxCabecera = auxCabecera.abajo
        return CabEncontada

    def vaciarMatrizOrtogonal(self, matriz):
        matriz = None
        return matriz

    def buscarElemento(self, mat, dim, fi, co):
        auxDim = None
        auxFil = None
        auxCol = None
        encon = None
        auxDim = self.buscarDimension(mat.inicio, dim)
        auxFil = self.BuscarFila2(auxDim,mat.inicio, fi)
        encontrado = False
        auxCol = auxFil
        while(auxCol!=None and encontrado != None):
            if(auxCol.columna ==co):
                encon = auxCol
                encontrado = True
            auxCol = auxCol.derecha
        return encon

    def crearCarpeta(self):
        try: os.makedirs(self.Path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def escribirArchivoDot666Inicial(self, matriz, padre):
        self.crearCarpeta()
##        filename =self.Path +"matrizOrtogonal.dot"                                  ##aca hay cambios
        filename =padre +"_matrizOrtogonal_inicial.dot"
        archivoMatriz = open(filename,'w')
        col = None
        fil = None
        nDimme = None
        nDimme = matriz.inicio

        di=0;
        archivoMatriz.write("digraph MatrizOrtogonal_200412823 {\n")
        archivoMatriz.write("    rankdir = LR\n")
        archivoMatriz.write("    graph [ranksep=0.25 nodesep=0.25] \n")
        archivoMatriz.write("    node[shape= box style = filled color = limegreen] \n")
        archivoMatriz.write("    edge[color= black] \n")

        while(nDimme != None):
            if nDimme.dimension > 0:
                self.escribirDimensionDot666Inicial(di , nDimme, archivoMatriz)
            di = di + 1
            nDimme = nDimme.atras
        archivoMatriz.write('\n')
        archivoMatriz.write("   label = \" Matriz Ortogonal Inicial " + padre +"  \"  \n ")
        archivoMatriz.write('\n}')
        archivoMatriz.close()


    def escribirDimensionDot666Inicial(self, dimeens, diimmens, archivoMatriz):
        col = None
        fil = None
        archivoMatriz.write("\n")
        archivoMatriz.write("    subgraph cluster_Dimension" + str(dimeens) +" { \n")
        archivoMatriz.write("        graph [ranksep=0.25 nodesep=0.25] \n")
        archivoMatriz.write("        node[shape= box style = filled color = limegreen ] \n")
        archivoMatriz.write("        edge[color= black] \n")
        fil = diimmens
        while(fil!=None):

            col = fil

            while(col!=None):
                coluu= col.columna
                filaa= col.fila
                diimee = col.dimension
                datoo = col.valor
                val= col.valor
##            std::string val= col->valor

                archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+"[label ="+ self.getEtiquetaContenidoNodo(coluu, filaa,diimee, datoo,val)+"] \n")

                if(col.izquierda!=None):
                    archivoMatriz.write("           "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+ self.getEtiqueta666(col.izquierda.columna, col.izquierda.fila,col.izquierda.dimension, col.izquierda.valor,col.izquierda.valor)+"\n")

                if(col.derecha!=None):
                    archivoMatriz.write("           "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+self.getEtiqueta666(col.derecha.columna, col.derecha.fila,col.derecha.dimension, col.derecha.valor,col.derecha.valor)+"\n")

                archivoMatriz.write('\n')
                archivoMatriz.write("        rank = same {\n")

                if(col.arriba!=None):
                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+ self.getEtiqueta666(col.arriba.columna, col.arriba.fila,col.arriba.dimension, col.arriba.valor,col.arriba.valor)+"\n")

                if(col.abajo!=None):
                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+"->" + self.getEtiqueta666(col.abajo.columna, col.abajo.fila,col.abajo.dimension, col.abajo.valor,col.abajo.valor) + "\n")

                archivoMatriz.write("        };\n")
                archivoMatriz.write("\n")

##                con esto puedo modificar para no mostrar las cabeceras
##                y solo mostrar los nodos o cambiar los colores de estas
##                era cabecera de dimension
                if(col.columna==0 and col.fila==0 and col.dimension >=1 and col.valor==-1):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+" [fillcolor=brown] \n ")

                ##era columna
                elif(col.columna!=0 and col.fila==0 and col.dimension >=1 and col.valor==0):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+" [fillcolor=orange] \n ")

            ##  era fila
                elif(col.columna==0 and col.fila!=0 and col.dimension>=1 and col.valor==0):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) +" [fillcolor=orange] \n ")

            ##  era nodo interno
                else:
                    print "era nodo interno"

                col = col.derecha


            fil =fil.abajo

        archivoMatriz.write("        "+"label = \"Nivel de "+ self.obtenerEtiquetaTipoDimension(diimmens.dimension) +" \"\n }")


    def escribirArchivoDot666(self, matriz, padre):
        self.crearCarpeta()
##        filename =self.Path +"matrizOrtogonal.dot"                                  ##aca hay cambios
        filename =padre +"_matrizOrtogonal_actual.dot"
        archivoMatriz = open(filename,'w')
        col = None
        fil = None
        nDimme = None
        nDimme = matriz.inicio

        di=0;
        archivoMatriz.write("digraph MatrizOrtogonal_200412823 {\n")
        archivoMatriz.write("    rankdir = LR\n")
        archivoMatriz.write("    graph [ranksep=0.25 nodesep=0.25] \n")
        archivoMatriz.write("    node[shape= box style = filled color = limegreen] \n")
        archivoMatriz.write("    edge[color= black] \n")

        while(nDimme != None):
            if nDimme.dimension > 0:
                self.escribirDimensionDot666(di , nDimme, archivoMatriz)
            di = di + 1
            nDimme = nDimme.atras
        archivoMatriz.write('\n')
        archivoMatriz.write("   label = \" Matriz Ortogonal Actual " + padre +"  \"  \n ")
        archivoMatriz.write('\n}')
        archivoMatriz.close()


    def escribirDimensionDot666(self, dimeens, diimmens, archivoMatriz):
        col = None
        fil = None
        archivoMatriz.write("\n")
        archivoMatriz.write("    subgraph cluster_Dimension" + str(dimeens) +" { \n")
        archivoMatriz.write("        graph [ranksep=0.25 nodesep=0.25] \n")
        archivoMatriz.write("        node[shape= box style = filled color = limegreen ] \n")
        archivoMatriz.write("        edge[color= black] \n")
        fil = diimmens
        while(fil!=None):

            col = fil

            while(col!=None):
                coluu= col.columna
                filaa= col.fila
                diimee = col.dimension
                datoo = col.valor
                val= col.valor
##            std::string val= col->valor

                archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+"[label ="+ self.getEtiquetaContenidoNodo(coluu, filaa,diimee, datoo,val)+"] \n")

                if(col.izquierda!=None):
                    archivoMatriz.write("           "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+ self.getEtiqueta666(col.izquierda.columna, col.izquierda.fila,col.izquierda.dimension, col.izquierda.valor,col.izquierda.valor)+"\n")

                if(col.derecha!=None):
                    archivoMatriz.write("           "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+self.getEtiqueta666(col.derecha.columna, col.derecha.fila,col.derecha.dimension, col.derecha.valor,col.derecha.valor)+"\n")

                archivoMatriz.write('\n')
                archivoMatriz.write("        rank = same {\n")

                if(col.arriba!=None):
                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+ self.getEtiqueta666(col.arriba.columna, col.arriba.fila,col.arriba.dimension, col.arriba.valor,col.arriba.valor)+"\n")

                if(col.abajo!=None):
                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+"->" + self.getEtiqueta666(col.abajo.columna, col.abajo.fila,col.abajo.dimension, col.abajo.valor,col.abajo.valor) + "\n")

                archivoMatriz.write("        };\n")
                archivoMatriz.write("\n")

##                con esto puedo modificar para no mostrar las cabeceras
##                y solo mostrar los nodos o cambiar los colores de estas
##                era cabecera de dimension
                if(col.columna==0 and col.fila==0 and col.dimension >=1 and col.valor==-1):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+" [fillcolor=brown] \n ")

                ##era columna
                elif(col.columna!=0 and col.fila==0 and col.dimension >=1 and col.valor==0):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+" [fillcolor=orange] \n ")

            ##  era fila
                elif(col.columna==0 and col.fila!=0 and col.dimension>=1 and col.valor==0):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) +" [fillcolor=orange] \n ")

            ##  era nodo interno
                else:
                    print "era nodo interno"

                col = col.derecha


            fil =fil.abajo

        archivoMatriz.write("        "+"label = \"Nivel de "+ self.obtenerEtiquetaTipoDimension(diimmens.dimension) +" \"\n }")


    def escribirDimensionDot999(self, dimeens, diimmens, archivoMatriz):
        col = None
        fil = None
        archivoMatriz.write("\n")
        archivoMatriz.write("    subgraph cluster_Dimension" + str(dimeens) +" { \n")
        archivoMatriz.write("        graph [ranksep=0.25 nodesep=0.25] \n")
        archivoMatriz.write("        node[shape= box style = filled color = limegreen ] \n")
        archivoMatriz.write("        edge[color= black] \n")
        fil = diimmens
        while(fil!=None):

            col = fil

            while(col!=None):
                coluu= col.columna
                filaa= col.fila
                diimee = col.dimension
                datoo = col.valor
                val= col.valor
##            std::string val= col->valor

                archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+"[label ="+ self.getEtiquetaContenidoNodo(coluu, filaa,diimee, datoo,val)+"] \n")

                if(col.arriba!=None):
                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+ self.getEtiqueta666(col.arriba.columna, col.arriba.fila,col.arriba.dimension, col.arriba.valor,col.arriba.valor)+"\n")

                if(col.abajo!=None):
                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+"->" + self.getEtiqueta666(col.abajo.columna, col.abajo.fila,col.abajo.dimension, col.abajo.valor,col.abajo.valor) + "\n")

                archivoMatriz.write('\n')
                archivoMatriz.write("        rank = same {\n")

                if(col.izquierda!=None):
                    archivoMatriz.write("           "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+ self.getEtiqueta666(col.izquierda.columna, col.izquierda.fila,col.izquierda.dimension, col.izquierda.valor,col.izquierda.valor)+"\n")

                if(col.derecha!=None):

                    archivoMatriz.write("           "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) + "->"+self.getEtiqueta666(col.derecha.columna, col.derecha.fila,col.derecha.dimension, col.derecha.valor,col.derecha.valor)+"\n")

                archivoMatriz.write("        };\n")
                archivoMatriz.write("\n")

##                con esto puedo modificar para no mostrar las cabeceras
##                y solo mostrar los nodos o cambiar los colores de estas
##                era cabecera de dimension
                if(col.columna==0 and col.fila==0 and col.dimension >=1 and col.valor==-1):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+" [fillcolor=brown] \n ")

                ##era columna
                elif(col.columna!=0 and col.fila==0 and col.dimension >=1 and col.valor==0):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val)+" [fillcolor=orange] \n ")

            ##  era fila
                elif(col.columna==0 and col.fila!=0 and col.dimension>=1 and col.valor==0):

                    archivoMatriz.write("        "+self.getEtiqueta666(coluu, filaa,diimee, datoo,val) +" [fillcolor=orange] \n ")

            ##  era nodo interno
                else:
                    print "era nodo interno"

                col = col.derecha


            fil =fil.abajo

        archivoMatriz.write("        "+"label = \"Nivel de "+ self.obtenerEtiquetaTipoDimension(diimmens.dimension) +" \"\n }")

    def obtenerEtiquetaTipoDimension(self, dimm):
        cade = ""
        if(str(dimm)=="1"):
            cade = "Satelites"
        elif (str(dimm)=="2"):
            cade = "Aviones"
        elif (str(dimm)=="3"):
            cade = "Barcos"
        elif (str(dimm)=="4"):
            cade = "Submarinos"
        return cade

##//metodo para obtener la etiqueta de cada nodo de la matriz
    def getEtiqueta666(self, col,  fil, dim, val,  infoo):

        if(col==0 and fil==0 and dim>=1 and val==-1):
            niv=""
            niv = niv + "Nivel_"
            niv = niv + str(dim)
            return niv

        elif(col!=0 and fil==0 and dim >=1 and val==0):

            cool="";
            cool = cool + "D_"
            cool = cool + str(dim)
            cool = cool + "F_"
            cool = cool + str(fil)
            cool = cool + "C_"
            cool = cool + str(col)
            return cool;

        elif(col==0 and fil!=0 and dim>=1 and val==0):

            fillla="";
            fillla= fillla +"D_"
            fillla= fillla +str(dim)
            fillla= fillla +"F_"
            fillla= fillla +str(fil)
            fillla= fillla +"C_"
            fillla= fillla +str(col)
            return fillla

        else:
            info=""
            info = info + "D_"
            info = info + str(dim)
            info = info + "F_"
            info = info + str(fil)
            info = info + "C_"
            info = info + str(col)
            info = info + "V_"
            info = info + str(infoo)
            return info;

##metodo para obtener la etiqueta de cada nodo de la matriz
    def getEtiquetaContenidoNodo(self, col,  fil, dim, val, infoo):

        if(col==0 and fil==0 and dim>=1 and val==-1):
##        Esta era Cabecera
            niv=""
            niv = niv +"\"Nivel "
            niv = niv +str(dim)
            niv = niv +"\""
            return niv

        elif(col!=0 and fil==0 and dim >=1 and val==0):
            cool="";
            cool = cool + "\""
            cool = cool + "Col: "
            cool = cool + str(col)
            cool = cool + " \""
            return cool

        elif(col==0 and fil!=0 and dim>=1 and val==0):
            fillla="";
            fillla = fillla + "\""
            fillla = fillla + "Fil: "
            fillla = fillla + str(fil)
            fillla = fillla + "\""
            return fillla

        else:
            info="";
            info = info + "\""
            info = info + self.obtenerContenidoDeNave(infoo)
            info = info + "\""
            info = info + " fontsize=\"10.0\""
            return info

    def obtenerContenidoDeNave(self,  infoo):
        cadena = ""
        cadena = infoo
        vecto = cadena.split("_")
        cadena = vecto[0]
        cadena = cadena + " \n "
        cadena = cadena + vecto[1]+":"+vecto[2]+ "-" + vecto[3]+":"+vecto[4]+"-"+vecto[5]+":"+ vecto[6]
        return cadena


##//metodo para insertar en la columna hallada
    def insertarEnColumna2(self, nodoInsertar, nodoCol, matriz, val):
        nuevo = None
        anterior = None
        nuevo = nodoInsertar;

        if(nodoCol ==None):
            nodoCol = nuevo
        else:

            anterior = nodoCol
            matriz.actual = nodoCol
            while(matriz.actual!=None and matriz.actual.fila < nodoInsertar.fila):
                anterior = matriz.actual
                matriz.actual = matriz.actual.abajo

            if (matriz.actual == None):
                anterior.abajo = nuevo
                nuevo.arriba = anterior

            else:
                if (matriz.actual.arriba == None):
                    nuevo.abajo= nodoCol
                    nodoCol = nuevo
                    matriz.actual.arriba = nuevo

                else:

                    nuevo.abajo = matriz.actual.arriba.abajo
                    matriz.actual.arriba.abajo =nuevo
                    nuevo.arriba = matriz.actual.arriba
                    matriz.actual.arriba = nuevo


##//metodo para insertar en la fila hallada
    def insertarEnFila2(self, nodoInsertar, nodoFil, matriz, val):
        nuevo = None
        anterior = None
        nuevo = nodoInsertar

        if(nodoFil ==None):
            nodoFil = nuevo

        else:
            anterior = nodoFil
            matriz.actual = nodoFil
            while(matriz.actual!=None and matriz.actual.columna < nodoInsertar.columna):
                anterior = matriz.actual
                matriz.actual = matriz.actual.derecha

            if (matriz.actual == None):
                anterior.derecha = nuevo
                nuevo.izquierda = anterior

            else:
                if (matriz.actual.izquierda == None):
                    nuevo.derecha= nodoFil
                    nodoFil = nuevo
                    matriz.actual.izquierda = nuevo

                else:
                    nuevo.derecha = matriz.actual.izquierda.derecha
                    matriz.actual.izquierda.derecha =nuevo
                    nuevo.izquierda = matriz.actual.izquierda
                    matriz.actual.izquierda = nuevo

    def verImagenCompletaMatrizActual(self, padre):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ padre+'_matrizOrtogonal_actual.dot -o '+padre+'_matrizOrtogonal_Actual.jpg'
        os.system(miComandooo)
        os.popen(padre+'_matrizOrtogonal_Actual.jpg')

    def verImagenCompletaMatrizInicial(self, padre):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ padre+'_matrizOrtogonal_inicial.dot -o '+ padre+'_matrizOrtogonal_Inicial.jpg'
        os.system(miComandooo)
        os.popen(padre+'_matrizOrtogonal_Inicial.jpg')

