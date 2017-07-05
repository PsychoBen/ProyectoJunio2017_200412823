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
##import MatrizOrtogonal
##
##import ArbolABBPlayer
##import NodoPlayer

def main():
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
    futbolistasTup = [(1.1, "Casillas"), (1.5, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"), (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
    futbolistasTup.append((5.5,"Tu Padre"))
    futbolistasTup.sort(key=lambda futbolista: futbolista[0], reverse=True)
    print "Imprimimos las lista ordenada por dorsal:"
    print futbolistasTup


if __name__ == '__main__':
    main()

