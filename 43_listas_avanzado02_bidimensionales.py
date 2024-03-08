board = []
EMPTY = "-"

for i in range(8):  
    row = [EMPTY for i in range(8)]
    board.append(row)

for row in board:
    print(row)

#for i in range(8):
    #Este bucle for se ejecuta 8 veces, donde i toma valores de 0 a 7.
    #Representa cada fila del tablero.
    
#row = [Empty for i in range(8)]:
    #Se crea una lista llamada row.
    #El uso de la comprensión de lista "Empty for i in range(8)", donde cada elemento es igual a EMPTY.
    #Previamente, EMPTY se define con el caracter "-", pero puede ser algún otro ("a", "_", "o", etc).

#Entonces, el bucle crea efectivamente 8 listas, donde cada lista contiene (a su vez) 8 elementos iguales a EMTPY.
    
#Como las listas de comprensión pueden ser anidades, se puede acortar a la siguiente expresión:
    
board = [[EMPTY for i in range(8)] for j in range(8)]
for row in board: #Cada elemento es una lista, definida por [EMPTY for i in range(8)]; como se iteró 8 veces (en j), tenemos 8 listas de 8 subelementos cada una.
    print(row)

#Python utiliza los valores del rango range(8) para inicializar las variables i y j en cada iteración del bucle. 
    # En cada iteración del bucle exterior, j toma los valores de 0 a 7, 
    # y en cada iteración del bucle interior, i también toma los valores de 0 a 7. 
    # Esto crea un total de 64 iteraciones (8x8), que son suficientes para crear un tablero de ajedrez de 8x8.