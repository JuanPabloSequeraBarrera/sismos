import os 
import main as m 
import modulos.menu as menu
import modulos.regsismo as re
def informe(registmain : list):
    isActive = True
    num = []
    longitud1 = len(registmain[0])
    os.system('cls')
    print(menu.titulo)
    try:
        for sublist in registmain:
            if(len(sublist) != longitud1):
                print('Para realizar el informe se deben registrar la misma cantidad de movimientos teluricos en todas las ciudad')
                isActive = False
                break
            else:
                for item in sublist[1:]:
                    num.append(item)
    except ValueError:
        pass
    while isActive:
        suma = sum(num)
        longitud = len(num)
        promedio = (suma/longitud)
        if (promedio < 2.5):
            isActive = False
            print('El factor de riesgo es bajo')
            os.system('pause')
        elif (promedio > 2.6) and (promedio < 4.5):
            isActive = False
            print('El factor de riesgo es medio')
            os.system('pause')
        elif (promedio > 4.5):
            isActive = False
            print('El factor de riesgo es alto')
            os.system('pause')    
