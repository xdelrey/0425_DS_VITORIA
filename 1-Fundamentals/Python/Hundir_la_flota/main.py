import utils
import variables as vr

#crear tablero
tablero_jugador = utils.crear_tablero()
tablero_rival = utils.crear_tablero()
print("-"*10)

#crear barcos
barco_1 = crear_barco(2)
barco_2 = crear_barco(2)
barco_3 = crear_barco(2)
barco_4 = crear_barco(3)
barco_5 = crear_barco(3)
barco_6 = crear_barco(4)

tablero_modificado = utils.colocar_barco(vr.barco_jugador, tablero_jugador)
print(tablero_jugador)

print("-"*10)

utils.disparar((0,2), tablero_modificado)
print(tablero_jugador)

utils.validar_casilla_inicial()