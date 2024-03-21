while True:
    try:
        number = int(input("Ingresa un número entero: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError): #múltiples excepciones integradas dentro de un solo bloque except
        print("Valor incorrecto o se ha roto la regla de división entre cero.")
    except:
        print("Lo siento, algo salió mal...")


 #Algunas de las excepciones integradas más útiles de Python son: 
        # ZeroDivisionError, ValueError, TypeError, AttributeError, y SyntaxError. 
 # Una excepción más que, en nuestra opinión, merece tu atención es la excepción KeyboardInterrupt, 
        # que se genera cuando el usuario presiona la tecla de interrupción (CTRL-C o Eliminar). 
 
 # Ejecuta el código anterior y presiona la combinación de teclas para ver qué sucede 