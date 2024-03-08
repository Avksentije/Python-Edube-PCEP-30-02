# El código crea una estructura de datos llamada rooms, que representa un hotel con tres edificios
# cada uno con 15 pisos y 20 habitaciones por piso. 
# Esta estructura de datos es un arreglo tridimensional que almacena valores booleanos (True o False)
# para indicar si una habitación está ocupada o desocupada.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#Reserva en el segundo edificio, en el décimo piso, habitación 14:
rooms[1][9][13] = True

#Desocupar el segundo cuarto, en el quinto piso del primer edificio:
rooms[0][4][1] = False


#Verificar si hay disponibilidad en el piso 15, del tercer edificio:

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
        
        #La variable vacancy contiene 0 si todas las habitaciones están ocupadas,
        #o, en dado caso, el número de habitaciones disponibles.


# Cubo - un arreglo tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

for row in cube:
    print(row)
    
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'