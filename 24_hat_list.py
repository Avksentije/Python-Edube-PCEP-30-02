hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

numero_usuario = int(input("Agreguemos un número entero: "))
# reemplazar el número de en medio con un número entero ingresado por el usuario.

hat_list[2] = numero_usuario
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

del hat_list[-1]
print("Los elementos contenidos en esta lista son ", len(hat_list))
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print(hat_list)


hat_list.append(934) #Colocar un elemento al final de la lista
print("El nuevo número de elementos en la lista es:", len(hat_list))
print(hat_list)

hat_list.insert(0, 222)
print("El número final de elementos en la lista es: ", len(hat_list))
print(hat_list)

