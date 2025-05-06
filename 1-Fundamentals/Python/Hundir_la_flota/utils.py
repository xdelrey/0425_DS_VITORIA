import numpy as np

def crear_tablero():
    tablero = np.full((10,10), "_")
    return tablero

#barco_jugador = [[[0,3], [0,4], [0,5], [0,6]], [[4,7], [5,7], [6,7]], [[8,8], [8,9]], [[1,7]]]

def colocar_barco(tablero, barco):
    for i in barco:
        for j in i:
            tablero[j[0], j[1]] = 'O'
    return(tablero)