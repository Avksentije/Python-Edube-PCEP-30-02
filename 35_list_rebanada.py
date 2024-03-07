#Al asignar una lista a otra lista en Python utilizando la sintaxis list_2 = list_1, no se está copiando el contenido de la lista, sino que se están creando dos nombres que apuntan a la misma ubicación en la memoria.
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)


#Esto se soluciona con el método rebanar lista
list_1 = [1]
list_2 = list_1[:] #crea una copia de toda la lista
list_1[0] = 2
print(list_2)


#También se pueden copiar ciertos elementos indexados de la lista
my_list = [25, 8, 6, 17, 233]
new_list = my_list[1:3] #1,2,3 (solo selecciona 1 y 2), es n-1
print(new_list)

#my_list[start:end]
#start = ínice del primer elemento incluido en la rebanada
#end = índice del primer elemento no-incluido en la rebanada

my_list = [10, 8, 6, 4, 2, 17, 13, 111]
new_list = my_list[1:-1]
print("Cantidad de elementos:", len(my_list))
print("Rebanada 01:", new_list)
new_list = my_list[1:-5]
print("Rebanada 02:", new_list)
new_list = my_list[-1:1]
print("Elementos más allá del end:", new_list)
new_list = my_list[:5]
print("Rebanada desde elemento 0:", new_list)
new_list = my_list[0:]
print("Rebanada hasta elemento -1:", new_list) #aquí sí se incluye el elemento final, -1

#Eliminar varios elementos de la lista
lista = [10, 8, 6, 4, 2]
print(lista)
del lista[1:3]
print(lista)
del lista[:]
print(lista)

#Eliminar una lista, no su contenido
lista = [10, 8, 6, 4, 2]
del lista
print(lista) #Aparece en la consola "name 'lista' is not define"