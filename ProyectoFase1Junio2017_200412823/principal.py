#-------------------------------------------------------------------------------
# Name:        Clase principal del Proyecto
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     15/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import json
import uuid
import copy
import random
import NodoJuego
import NodoPlayer
import NodoMatriz
import ArbolABBPlayer
import MatrizOrtogonal
import ListaDobleDeJuegos
import NodoJuegoListaDoble

from flask import Flask, session, request, render_template, jsonify, Response, redirect, url_for

##APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask("WebServiceBattleship")


miArbolUsuario = ArbolABBPlayer.arbolABBPlayer()

miJuego = NodoJuego.NodoJuego()


@app.route("/subirArchivoUsuario", methods=["POST"])
def upload():
     f = request.files('file')
     folder = os.path.realpath(__file__).replace("\\","/").split("/")[0:-1]
     f.save("/".join(folder) + "/archivos/usuario/" + f.filename )


@app.route('/hola')
def he():
    return "hola Mundo"


@app.route('/welcome')
def saludarme():
    return redirect("index.jsp")


@app.route('/loginAdmin', methods=['POST'])
def loguearAdministrador():
    nickLoguear_sent = request.form['Nick']
    passwLoguear_sent = request.form['Passw']
    app.logger.info(nickLoguear_sent)
    app.logger.info(passwLoguear_sent)
    if nickLoguear_sent == 'ben' and passwLoguear_sent == 'ben':
       return  "success"
    else:
        return  "fail"


@app.route('/loginUsuario', methods=['POST'])
def loguearUsuario():
    nickLoguear_sent = request.form['Nick']
    passwLoguear_sent = request.form['Passw']
    if miJuego.arbolGeneralUsuarios.loguearJugador(nickLoguear_sent, passwLoguear_sent)==True:
       return  "success"
    else:
        return  "fail"

@app.route('/eliminarPlayer', methods=['POST'])
def eliminarUsuario():
    nickLoguear_sent = request.form['Nick']
    miJuego.arbolGeneralUsuarios.eliminarUsuarioArbolNodoPlayer(nickLoguear_sent)
    return  "success"

@app.route('/modificarPlayer', methods=['POST'])
def modificarUsuario():
    nickLoguear_sent = request.form['Nick']
    passwLoguear_sent = request.form['Passw']
    print nickLoguear_sent + "    " + passwLoguear_sent
    userModificar = miJuego.arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(nickLoguear_sent)
    userModificar.password = passwLoguear_sent
    return  "success"

@app.route('/crearUsuario', methods=['POST'])
def crearUsuario():
    nickLoguear_sent = request.form['Nick']
    passwLoguear_sent = request.form['Passw']
    coneLoguear_sent = request.form['Conec']
    if miJuego.arbolGeneralUsuarios.insertarPlayerArbolJugadores(nickLoguear_sent, passwLoguear_sent, coneLoguear_sent)==True:
        app.logger.info("User creado: nick: " + nickLoguear_sent + " password: " + passwLoguear_sent)

        return  "success"
    else:
        app.logger.info("User no creado: nick: " + nickLoguear_sent + " password: " + passwLoguear_sent)
        return  "fail"

##metodo para obtener la matriz inicial del player 1  ACTUAL
@app.route('/mostrarMatrizPlayer1Actual', methods=['GET'])
def mostrarMatrizPlayer1Actual():
    padre = miJuego.usuarioActual1.nickname
    miJuego.usuarioActual1.matrizOrtogonalUser.escribirArchivoDot666(miJuego.usuarioActual1.matrizOrtogonalUser, padre)
    cadena = miJuego.usuarioActual1.matrizOrtogonalUser.leerArchivoMatrizActual(padre)
    app.logger.info(cadena)
    return  str(cadena)

##metodo para obtener la matriz inicial del player 2  ACTUAL
@app.route('/mostrarMatrizPlayer1Inicial', methods=['GET'])
def mostrarMatrizPlayer1Inicial():
    padre = miJuego.usuarioActual1.nickname
    miJuego.usuarioActual1.matrizOrtogonalUser.escribirArchivoDot666Inicial(miJuego.usuarioActual1.matrizOrtogonalUser, padre)
    cadena = miJuego.usuarioActual1.matrizOrtogonalUser.leerArchivoMatrizInicial(padre)
    app.logger.info(cadena)
    return  str(cadena)

##metodo para obtener la matriz inicial del player 2  ACTUAL
@app.route('/mostrarMatrizPlayer2Actual', methods=['GET'])
def mostrarMatrizPlayer2Actual():
    padre = miJuego.usuarioActual2.nickname
    miJuego.usuarioActual2.matrizOrtogonalUser.escribirArchivoDot666(miJuego.usuarioActual2.matrizOrtogonalUser, padre)
    cadena = miJuego.usuarioActual2.matrizOrtogonalUser.leerArchivoMatrizActual(padre)
    app.logger.info(cadena)
    return  str(cadena)

##metodo para obtener la matriz inicial del player 2  ACTUAL
@app.route('/mostrarMatrizPlayer2Inicial', methods=['GET'])
def mostrarMatrizPlayer2Inicial():
    padre = miJuego.usuarioActual2.nickname
    miJuego.usuarioActual2.matrizOrtogonalUser.escribirArchivoDot666Inicial(miJuego.usuarioActual2.matrizOrtogonalUser, padre)
    cadena = miJuego.usuarioActual2.matrizOrtogonalUser.leerArchivoMatrizInicial(padre)
    app.logger.info(cadena)
    return  str(cadena)


@app.route('/mostrarABB', methods=['GET'])
def mostrarABB():
    miJuego.arbolGeneralUsuarios.GenerarDotArreglado()
    cadena = miJuego.arbolGeneralUsuarios.leerArchivoDot()
    app.logger.info(cadena)
    return  str(cadena)


@app.route('/mostrarABBEspejo', methods=['GET'])
def mostrarABBEspejo():
    espejo = miJuego.arbolGeneralUsuarios.arbolEspejo(miJuego.arbolGeneralUsuarios.raiz)
    miJuego.arbolGeneralUsuarios.GenerarDotEspejo(espejo)
    cadena = miJuego.arbolGeneralUsuarios.leerArchivoDotEspejo()
    app.logger.info(cadena)
    return  str(cadena)

@app.route('/insertarJuegoPlayer', methods=['POST'])
def insertarJuegoPlayer():
    nick_buscar = request.form['nick_base']
    oponente_buscar = request.form['oponente']
    TRealiz_buscar = request.form['TRealizados']
    TAcert_buscar = request.form['TAcertados']
    TFail_buscar = request.form['TFallados']
    ganador_buscar = request.form['win']
    danio_buscar = request.form['danio']
    miUserActual = miJuego.arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(nick_buscar)
    miUserActual.listaGamesUser.insertarListaDeJuegosFinalizados(oponente_buscar, TRealiz_buscar, TAcert_buscar, TFail_buscar, ganador_buscar, danio_buscar)

    return  "success"


@app.route('/crearjuegoactual', methods=['POST'])
def crearjuegoactual():
    user1 =  request.form['user1']
    user2 =  request.form['user2']
    tamx =  request.form['tamX']
    tamy =  request.form['tamY']
    vari =  request.form['variante']
    tiemp =  request.form['tiempo']
    shoot =  request.form['disparo']
    type_shoot =  request.form['tpo_disparo']
    miJuego.inicializarJuego(user1,user2,tamx,tamy,vari,tiemp,shoot,type_shoot)
    print "*********************************************************************************"
    print "*********************************************************************************"
    print "***** Usuario 1: "+ user1+" Usuario 2:"+user2 +"  *************"
    print "*********************************************************************************"
    print "*********************************************************************************"
    userAct1 = miJuego.arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(user1)
    userAct2 = miJuego.arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(user2)
    miJuego.usuarioActual1 = userAct1
    miJuego.usuarioActual2 = userAct2
    if(userAct1!=None and userAct2!=None):
        print("Usuario 1 : " + userAct1.nickname)
        print("Usuario 2 : " + userAct2.nickname)
        print("success")
        return "success"
    else:
        return "fail"


@app.route('/crearNaves', methods=['POST'])
def crearNaves():
    user = request.form['user']
    fil = request.form['fila']
    colu = request.form['columna']
    dimens = request.form['dimension']
    valor = request.form['valor']
    path = request.form['path']
    app.logger.info("************************************************************")
    app.logger.info("************************************************************")
    if(miJuego.usuarioActual1.nickname ==user):
        miJuego.usuarioActual1.matrizOrtogonalUser.insertarEnMatrizOrtogonal3Dimensiones(miJuego.usuarioActual1.matrizOrtogonalUser,fil, colu, dimens, valor, path)
        primerUser = miJuego.arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(user)
        if(primerUser!=None):
            primerUser.matrizOrtogonalUser = miJuego.usuarioActual1.matrizOrtogonalUser
##            primerUser.matrizOrtogonalUser = miJuego.usuarioActual1
        return "success"
    elif(miJuego.usuarioActual2.nickname ==user):
        miJuego.usuarioActual2.matrizOrtogonalUser.insertarEnMatrizOrtogonal3Dimensiones(miJuego.usuarioActual2.matrizOrtogonalUser,fil, colu, dimens, valor, path)
        secondUser = miJuego.arbolGeneralUsuarios.buscarUsuarioUsuarioEnArbol(user)
        if(secondUser!=None):
            secondUser.matrizOrtogonalUser = miJuego.usuarioActual2.matrizOrtogonalUser
        return "success"
    else:
        return "fail"


@app.route('/bestWinners', methods=['GET'])
def verMejoresWinners():
    cadenita = miJuego.arbolGeneralUsuarios.obtenerListadoPlayersBestWinner()
    return cadenita

@app.route('/bestShooters', methods=['GET'])
def verMejoresShooters():
    cadenita = miJuego.arbolGeneralUsuarios.obtenerListadoPlayersBestShooter()
    return cadenita

##
##if __name__ == '__main__':
##    app.run(debug = True, port=8081)

if __name__ == '__main__':
    app.run(host='192.168.56.101', port ='5555')

