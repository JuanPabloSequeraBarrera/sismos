import os
import modulos.regcity  as c
import modulos.regsismo as r
import modulos.menu as m
def searchsis(registmain : list):
    os.system('cls')
    print(m.titulo)
    print('Bienvenido al buscador de sismos por ciudad ')
    print('Seleccione la ciudad de la cual quiere ver los movimientos registrados')
    sercity = str (input(':)_ ')).upper()
    try:
        for i in (registmain):
            if (sercity in i):
                print(f'los movimientos registrados en {sercity} son {i}')
                os.system('pause')
                break
        else:
            print('Ciudad seleccionada no registrada, vuelva a intentarlo')
            os.system('pause')
            searchsis(registmain)
    except ValueError:
        print('Error de digitacion')
        searchsis(registmain)


    