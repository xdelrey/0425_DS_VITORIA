import utils
import variables as vr

tablero_jugador = utils.crear_tablero()
tablero_rival = utils.crear_tablero()
print(tablero_jugador)
print("-"*10)

tablero_modificado = utils.colocar_barco(tablero_jugador, vr.barco_jugador)
print(tablero_jugador)