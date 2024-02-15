import os 
lstopc = [1,2,3,4,5]
titulo =  """ 
    +++++++++++++++++++++++++++++++++
    +Registro de sismos Colombia CPS+
    +++++++++++++++++++++++++++++++++
"""
opciones = ('1.Registro de ciudad\n2.Registro de sismos\n3.Sistema de busqueda por ciudad\n4.Informe de riesgo\n5.Salir')
def menuop():
    os.system('cls')
    print(titulo)
    try:
        print(opciones)
        op = int(input(':)_ '))
        if not (op in lstopc):
            print('opcion no valida')
            os.system('pause')
            menuop()
    except ValueError:
        print('Value invalida')
        os.system('pause')
        menuop()
    return (op)


    



