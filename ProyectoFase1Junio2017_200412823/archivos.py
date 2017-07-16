#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     21/06/2017
# Copyright:   (c) Ben Cotto 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##
import MatrizOrtogonal
import arbolAVLContactos
import ArbolABBPlayer
import NodoPlayer
import NodoArbolB
import ArbolB
import ArbolBPruebas
import NodoPruebas
import otros


def modificarUsuario(arbolGeneralUsuarios, nickLoguear_sent, nickNuevo_sent, passwLoguear_sent):
    print nickLoguear_sent + "    " + passwLoguear_sent
    userModificar = arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(nickLoguear_sent)

    estaCon = userModificar.estaConectado
    yaexiste = userModificar.yaExisteEnJugadores
    listaUsuarios = userModificar.listaGamesUser
    matrizOrto = userModificar.matrizOrtogonalUser
    matrizOrtoActual = userModificar.matrizOrtogonalUserActual
    avlContactos = userModificar.arbolAvlContactosPlayer
    maxGan = userModificar.maxGanados
    efecti = userModificar.efectividad
    facto = userModificar.factorBalance

    arbolGeneralUsuarios.eliminarUsuarioArbolNodoPlayer(nickLoguear_sent)

    arbolGeneralUsuarios.insertarPlayerArbolJugadores(nickNuevo_sent, passwLoguear_sent, estaCon)

    recienIngresado = arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(nickNuevo_sent)
    recienIngresado.estaConectado = estaCon
    recienIngresado.yaExisteEnJugadores = yaexiste
    recienIngresado.listaGamesUser = listaUsuarios
    recienIngresado.matrizOrtogonalUser = matrizOrto
    recienIngresado.matrizOrtogonalUserActual = matrizOrtoActual
    recienIngresado.arbolAvlContactosPlayer = avlContactos
    recienIngresado.maxGanados = maxGan
    recienIngresado.efectividad = efecti
    recienIngresado.factorBalance = facto

    return  "success"

def main():
    vectorOtros = [otros.pepe]
    vectorOtros.append("hola")
    vectorOtros.append("mundo")

##    miArbol_B = ArbolBPruebas.ArbolB(3, None)
##
##    miArbol_B.insertarNodoArbolB(2)
##    miArbol_B.insertarNodoArbolB(3)
##    miArbol_B.insertarNodoArbolB(6)
##    miArbol_B.insertarNodoArbolB(8)
##    miArbol_B.insertarNodoArbolB(5)
##    miArbol_B.insertarNodoArbolB(15)
##    miArbol_B.insertarNodoArbolB(20)
##    miArbol_B.insertarNodoArbolB(23)
##    miArbol_B.insertarNodoArbolB(9)
##    miArbol_B.insertarNodoArbolB(11)
##    miArbol_B.insertarNodoArbolB(14)
##    miArbol_B.insertarNodoArbolB(25)
##    miArbol_B.insertarNodoArbolB(7)
##    miArbol_B.insertarNodoArbolB(1)
##    miArbol_B.insertarNodoArbolB(10)
##    miArbol_B.insertarNodoArbolB(13)
##    miArbol_B.insertarNodoArbolB(12)
##    miArbol_B.insertarNodoArbolB(30)
##    miArbol_B.insertarNodoArbolB(21)




##    miArbol_B = ArbolB.ArbolB(5)
##
##    miArbol_B.insertarArbolB(2)
##    miArbol_B.insertarArbolB(3)
##    miArbol_B.insertarArbolB(6)
##    miArbol_B.insertarArbolB(8)
##    miArbol_B.insertarArbolB(5)
##    miArbol_B.insertarArbolB(15)
##    miArbol_B.insertarArbolB(20)
##    miArbol_B.insertarArbolB(23)
##    miArbol_B.insertarArbolB(9)
##    miArbol_B.insertarArbolB(11)
##    miArbol_B.insertarArbolB(14)
##    miArbol_B.insertarArbolB(25)
##    miArbol_B.insertarArbolB(7)
##    miArbol_B.insertarArbolB(1)
##    miArbol_B.insertarArbolB(10)
##    miArbol_B.insertarArbolB(13)
##    miArbol_B.insertarArbolB(12)
##    miArbol_B.insertarArbolB(30)
##    miArbol_B.insertarArbolB(21)



##    miArbol_B.insertarArbolB(8)
##    miArbol_B.insertarArbolB(4)
##    miArbol_B.insertarArbolB(7)
##    miArbol_B.insertarArbolB(15)
##    miArbol_B.insertarArbolB(23)
##    miArbol_B.insertarArbolB(30)
##    miArbol_B.insertarArbolB(42)
##    miArbol_B.insertarArbolB(1)
##    miArbol_B.insertarArbolB(17)
##    miArbol_B.insertarArbolB(99)
##    miArbol_B.insertarArbolB(50)
##    miArbol_B.insertarArbolB(32)
##    miArbol_B.insertarArbolB(25)
##    miArbol_B.insertarArbolB(2)
##    miArbol_B.insertarArbolB(10)
##    miArbol_B.insertarArbolB(6)
##    miArbol_B.insertarArbolB(35)
##    miArbol_B.insertarArbolB(37)



##    miArbol_B.ObtenerDotArbolB()

##    miArbol = ArbolABBPlayer.arbolABBPlayer()
##    miArbol.insertarPlayerArbolJugadores("J","hola", False)
##    miArbol.insertarPlayerArbolJugadores("G","hola", False)
##    miArbol.insertarPlayerArbolJugadores("X","hola", False)
##    miArbol.insertarPlayerArbolJugadores("A","hola", False)
##    miArbol.insertarPlayerArbolJugadores("I","hola", False)
##    miArbol.insertarPlayerArbolJugadores("M","mama", False)
##    miArbol.insertarPlayerArbolJugadores("Y","mama", False)
##    miArbol.insertarPlayerArbolJugadores("Z","hola", False)
##    miArbol.insertarPlayerArbolJugadores("hla","hola", False)
##    miArbol.insertarPlayerArbolJugadores("pepa","hola", False)
##    user = miArbol.buscarUsuarioUsuarioEnArbol("X")
##    user.listaGamesUser.insertarListaDeJuegosFinalizados("tut", 150, 70, 80, False, 25)
##    user.listaGamesUser.insertarListaDeJuegosFinalizados("opt", 150, 70, 80, False, 25)
##    user.listaGamesUser.insertarListaDeJuegosFinalizados("majst", 150, 70, 80, False, 25)
##    miArbol.eliminarUsuarioArbolNodoPlayer("G")
##    miArbol.GenerarDotArreglado()
##    miArbol.verImagenCompleta()
##    modificarUsuario(miArbol,"X", "Nena","nena")


##    user = miArbol.buscarUsuarioUsuarioEnArbol("A")
##    user.arbolAvlContactosPlayer.insertarUsuario("R","guate","online")
##    user.arbolAvlContactosPlayer.insertarUsuario("RR","guate","online")
##    user.arbolAvlContactosPlayer.insertarUsuario("PP","guate","online")
##    user.arbolAvlContactosPlayer.insertarUsuario("AA","guate","online")
##    user.arbolAvlContactosPlayer.insertarUsuario("MM","guate","online")

##    user2 = miArbol.buscarUsuarioUsuarioEnArbol("M")
##    user2.arbolAvlContactosPlayer.insertarUsuario("R","guate","online")
##    user2.arbolAvlContactosPlayer.insertarUsuario("RR","guate","online")
##    user2.arbolAvlContactosPlayer.insertarUsuario("PP","guate","online")
##    user2.arbolAvlContactosPlayer.insertarUsuario("AA","guate","online")
##    user2.arbolAvlContactosPlayer.insertarUsuario("MM","guate","online")
##    miArbol.GenerarDotArreglado()
##    miArbol.verImagenCompleta()


##     miMatrizOrtogonal = MatrizOrtogonal.MatrizOrtogonal()
##
##     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,1,"a", 3, "Subma_Fi_12_Co_R_Di_4", "path")
##     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,1,"b", 4, "Ship_Fi_12_Co_R_Di_4", "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,1,"x", 1, 505, "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,5,"b", 2, 7, "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,7,"b", 4, 880, "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,2,"x", 3, 55, "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,8,"x", 4, "po", "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,1,"f", 3, 560, "path")
####     miMatrizOrtogonal.insertarEnMatrizOrtogonal3Dimensiones(miMatrizOrtogonal,1,"g", 2, 810, "path")
####     miMatrizOrtogonal.mostrarElementosMatriz2()
##     miMatrizOrtogonal.escribirArchivoDot666(miMatrizOrtogonal, "Tu_Padre")
##     miMatrizOrtogonal.verImagenCompletaMatrizActual("Tu_Padre")

##    miArbolUsuario = arbolAVLContactos.arbolAVLContactos()
##    miArbolUsuario.insertarUsuario("rata","guate","online")
##    miArbolUsuario.insertarUsuario("ratas","guate","online")
##    miArbolUsuario.insertarUsuario("ratia","guate","online")
##    miArbolUsuario.insertarUsuario("ratiA","guate","online")
##    miArbolUsuario.insertarUsuario("ratIa","guate","online")
##    miArbolUsuario.insertarUsuario("ratAn","guate","online")
##    miArbolUsuario.insertarUsuario("rato","guate","online")
##    miArbolUsuario.insertarUsuario("zapo","guate","online")
##    miArbolUsuario.insertarUsuario("Zapo","guate","online")
##    miArbolUsuario.insertarUsuario("vaca","guate","online")
##    miArbolUsuario.insertarUsuario("psycho","guate","offline")
##    miArbolUsuario.insertarUsuario("pesta","guate","online")
##    miArbolUsuario.insertarUsuario("pasto","guate","online")
##    miArbolUsuario.insertarUsuario("una tarde","guate","online")
##    miArbolUsuario.insertarUsuario("meses pa yupe","guate","offline")
##    miArbolUsuario.insertarUsuario("rataT","guate","online")
##    nodoUser= miArbolUsuario.Buscar("rato")
##    print "**********************************"
##    print "*******Empiezan los logueos*******"
##    miArbolUsuario.loguearUsuario("ratan","guate")
##    print "**********************************"
##    miArbolUsuario.loguearUsuario("ratAn","guate")
##    print "**********************************"
##    miArbolUsuario.loguearUsuario("ratAn","guate")
##    print "**********************************"
##    miArbolUsuario.loguearUsuario("rataT","guate")
##    print "**********************************"
##    miArbolUsuario.loguearUsuario("rataT","guate")
##    print "Este es el nodo buscado"
##    print nodoUser.verNodoPlayer()
##    print " antes de eliminar"
##    miArbolUsuario.PostOrdenAvl(miArbolUsuario.Raiz)
##    miArbolUsuario.InordenAvl(miArbolUsuario.Raiz)
##    miArbolUsuario.PreOrdenAvl(miArbolUsuario.Raiz)
##    print "Esta es la cantidad de nodos: " +str(miArbolUsuario.CantidadNodosAvl(miArbolUsuario.Raiz))
##    print "Esta es la Altura del arbol: " +str(miArbolUsuario.AlturaArbol(miArbolUsuario.Raiz))
####    miArbolUsuario.eliminarContacto("ratan")
##    print "Despues de eliminar"
## ## miArbolUsuario.PostOrdenAvl(miArbolUsuario.Raiz)
## ## miArbolUsuario.InordenAvl(miArbolUsuario.Raiz)
##    miArbolUsuario.PreOrdenAvl(miArbolUsuario.Raiz)
##    print "Esta es la cantidad de nodos: " +str(miArbolUsuario.CantidadNodosAvl(miArbolUsuario.Raiz))
##    print "Esta es la Altura del arbol: " +str(miArbolUsuario.AlturaArbol(miArbolUsuario.Raiz))
##    miArbolUsuario.GenerarDotAVL()
##    miArbolUsuario.verImagenAVL()
##    miarchivoporlineas=miArbolUsuario.leerArchivoDotAVL()
##    for lineea in miarchivoporlineas:
##        print "esto tiene  ahora que regreso:  "+lineea
##    miArbolUsuario.verImagen2()



if __name__ == '__main__':
    main()

