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