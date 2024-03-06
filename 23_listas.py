numbers = [10, 5, 7, 2, 1]

print(numbers)
print(numbers[2])

print(len(numbers))
print("Mis números favoritos son: ", numbers[2], "y ", numbers[1])


numbers[2] = "voy a cambiar este número"
print(numbers)
numbers[2] = 17
print("Nueva lista: ", numbers)
print("\n")


list = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", list)  # Imprimiendo contenido de la lista original.

list[0] = 111
print("\nPrevio contenido de la lista:", list)  # Imprimiendo contenido de la lista anterior.

list[1] = list[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("\nNuevo contenido de la lista:", list)  # Imprimiendo el contenido de la lista actual.

print(list[3])
del list[3]
print(list)
print(list[3])