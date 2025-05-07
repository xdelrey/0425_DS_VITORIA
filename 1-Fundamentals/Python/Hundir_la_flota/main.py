from utils import *
import variables as vr

#crear tableros vacíos
#Tablero 1 Jugador (barcos Jug con disparos Rival)
tablero_barcos_jugador = utils.crear_tablero()
#Tablero 2 Jugador (disparos Jug)
tablero_disparos_jugador
#Tablero 1 Rival (barcos Rival con disparos Jug)
tablero_barcos_rival
#Tablero 2 Rival (disparos Rival)
tablero_disparos_rival
'''
tablero_jugador = utils.crear_tablero()
tablero_rival = utils.crear_tablero()
print("-"*10)

tablero_jugador = utils.colocar_barco(vr.barco_jugador, tablero_jugador)
print(tablero_jugador)

#tablero_rival = utils.colocar_barco(vr.barco_rival, tablero_rival)
#print(tablero_rival)

print("-"*10)

utils.disparar((0,2), tablero_jugador)
print(tablero_jugador)

utils.validar_casilla_inicial()
'''