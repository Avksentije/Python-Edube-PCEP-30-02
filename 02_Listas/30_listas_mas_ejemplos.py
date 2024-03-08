#Referenciando los textos de Edube:

#La lista es un tipo de dato en Python que se utiliza para almacenar múltiples objetos. 
#Es una colección ordenada y mutable de elementos separados por comas entre corchetes, por ejemplo:

lista01 = [1, None, True, "Soy una cadena", 256, 0]

#Las listas se pueden indexar y actualizar:
lista02 = [1, None, True, 'Soy una cadena', 256, 0]
print(lista02[3])  # salida: Soy una cadena
print(lista02[-1])  # salida: 0

lista02[1] = '?'
print(lista02)  # salida: [1, '?', True, 'Soy una cadena', 256, 0]

lista02.insert(0, "primero")
lista02.append("último")
print(lista02)  # outputs: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']


#Las listas pueden estar anidadas:
lista03 = [1, 'a', ["lista", 64, [0, 1], False]]

#Los elementos de la lista y las listas se pueden eliminar:

lista04 = [1, 2, 3, 4]
del lista04[2]
print(lista04)  # salida: [1, 2, 4]

del lista04  # borra la lista entera

#Las listas pueden ser iteradas mediante el uso del bucle for:
lista05 = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in lista05:
    print(color)


# La función len() se puede usar para verificar la longitud de la lista:

lista06 = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(lista06))  # salida 5

del lista06[2]
print(len(lista06))  # salida 4

#Ejemplo 07
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)


#Ejemplo 08

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number  #sumatoria del valor de los elementos
    lst_2.append(add) #se almacena en una nueva lista, llamada lst_2

print(lst_2) #este resultado es interesante

#Imprimir listas anidadas
lst_3 = [1, [2, 3], 4]
print(lst_3[1])
print(len(lst_3))