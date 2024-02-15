import os 
import modulos.menu as m
import modulos.regcity as r
import modulos.regsismo as reg
import modulos.search as s
import modulos.informe as i
if __name__ == '__main__':
    registmain = []
    isActive = True
    while isActive:
        os.system('cls')
        options = m.menuop()
        if (options == 1):
            r.registcity(registmain)
        elif(options == 2):
            reg.regsis(registmain)
        elif(options == 3):
            s.searchsis(registmain)
        elif(options == 4):
            i.informe(registmain)
        elif(options == 5):
            isActive = False
            print('Muchas gracias por usar el software')