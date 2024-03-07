#1. Mismo punto de memoria:

vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one) # salida: [carro', 'bicicleta', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # elimina 'carro'
print(vehicles_two) # salida: ['bicicleta', 'motor']


#2. Rebanadas:
colors = ['rojo', 'verde', 'naranja']

copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista

#3. Índices negativos:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

#4.Parámetros start and end:
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # salida: [3, 4, 5]
print(slice_two)  # salida: [1, 2]
print(slice_three)  # salida: [4, 5]

#5. Eliminar rebanadas (del):
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # salida: [3, 4, 5]

del my_list[:]
print(my_list)  # delimina el contenido de la lista, genera: []

#6. Comparar si existen elementos (in, not in):
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # salida: True
print("C" not in my_list)  # salida: True
print(2 not in my_list)  # salida: False

#7. Ejercicio 01:
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

#8. Ejercicio 02:
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)

#9. Ejercicio 03:
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)

#10. Ejercicio 04:
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)

#11. Ejercicio 05:
my_list = [1, 2, "in", True, "ABC"]

#Inserta in o not in en lugar de ??? para que el código genere el resultado esperado.
#print(1 ??? my_list)  # salida True
#print("A" ??? my_list)  # salida True
#print(3 ??? my_list)  # salida True
#print(False ??? my_list)  # salida False

print(1 in my_list)  # salida True
print("A" not in my_list)  # salida True
print(3 not in my_list)  # salida True
print(False in my_list)  # salida False