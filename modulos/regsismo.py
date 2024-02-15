import os 
import modulos.regcity as c
import main as m
import modulos.menu as menu
def regsis(registmain : list):
    os.system('cls')
    print(menu.titulo)
    print('Bienvenido al registro de sismos por ciudad, porfavor seleccione la ciudad a la que quiere registrar el sismo')
    print(registmain)
    op =  str (input(':)_ ')).upper()
    try:
        for i in (registmain):
            if (op in i):
                print(f'Ingrese la magnitud de el movimiento telurico registrado en {op}')
                telur = float (input(':)_ '))
                i.append(telur)
                os.system('pause')
                break
        else:
            print('Ciudad seleccionada no registrada, vuelva a intentarlo')
            os.system('pause')
            regsis(registmain)
    except ValueError:
        print('Error de digitacion')
        regsis(registmain)

