import os
import main as m
import modulos.menu as menu

def registcity(registrosismos : list):
    os.system('cls')
    try:
        i = 0
        while(i < 6):
            os.system('cls')
            print(menu.titulo)
            print('Bienvenido al registro de ciudad, porfavor indique el nombre de la ciudad que quiera ingresar')
            cityname = str (input(':)_ ')).upper()
            registrosismos.append([cityname])
            i += 1
            decis = str(input('Desea agregar otra ciudad? Si(si) No(no))').upper())
            if ((decis == 'NO')):
             i = 6
             os.system('pause')
    except ValueError:
            print('Nombre de ciudad no valido')
            registcity(registrosismos)

            




