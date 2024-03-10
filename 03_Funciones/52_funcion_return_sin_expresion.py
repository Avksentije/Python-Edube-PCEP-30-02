#return sin una expresión

#provoca la terminación inmediata de la jecución de la función
#y un retorno instantáneo al punto de invocación


def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:  #recuerda, un not True es un False :)
        return
    
    print("¡Feliz año nuevo!")

happy_new_year(False)


