import pyautogui as pg
import time

matriz = []
while True:
    cont = 1
    fila = list(input(f'Fila {cont}: '))
    cont +=1
    enteros = []

    for n in fila:
        enteros.append(int(n))
    matriz.append(enteros)

    if len(matriz) == 9:
        break
    print(f'Fila {str(len(matriz))} Completa')


time.sleep(3)

def box(x,y):
    if x<3:
        if y<3:
            caja = 1
        elif y<6:
            caja = 2
        else:
            caja=3

    elif x<6:
        if y<3:
            caja = 4
        elif y<6:
            caja = 5
        else:
            caja= 6

    else:
        if y<3:
            caja = 7
        elif y<6:
            caja = 8
        else:
            caja= 9
    
    return caja

def reducir(caja,matriz):
    lista = []
    if caja == 1:
        x = 0
        y = 0
    elif caja == 2:
        x = 0
        y = 3
    elif caja == 3:
        x = 0
        y = 6
    elif caja == 4:
        x = 3
        y = 0
    elif caja == 5:
        x = 3
        y = 3
    elif caja == 6:
        x = 3
        y = 6
    elif caja == 7:
        x = 6
        y = 0
    elif caja == 8:
        x = 6
        y = 3
    elif caja == 9:
        x = 6
        y = 6

    for I in range(x,x+3):
        for X in range(y,y+3):
            lista.append(matriz[I][X])
    
    return lista

def verificador(x,y,n):
    lista = []
    for i in range(0,9): #verifica en x
        if matriz[i][x] == n and i != y:
            return False

    for i in range(0,9): #verifica en y
        if matriz[y][i] == n and i != x:
            return False
    
    caja = box(y,x)
    lista = reducir(caja,matriz)

    if n in lista:
        return False

    return True

def Print(matrix):
    resuelto = []
    resuelto_cadena = []

    for i in range(len(matrix)):
        resuelto.append(matrix[i])
    
    for listas in resuelto:
        for num in listas:
            resuelto_cadena.append(str(num))
    
    contador = 0
    
    for num in resuelto_cadena:
        pg.press(num)
        pg.hotkey('right')
        contador +=1
        if contador%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

def resolver():
    global matriz
    for y in range(9):
        for x in range(9):
            if matriz[y][x] == 0:
                for n in range(1,10):
                    if verificador(x,y,n):
                        matriz[y][x] = n
                        resolver()
                        matriz[y][x] = 0
                return
    
    Print(matriz)
    
resolver()