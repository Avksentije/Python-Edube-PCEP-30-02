lista = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(lista) - 1):  # necesitamos (5 - 1) comparaciones
    if lista[i] > lista[i + 1]:  # compara elementos adyacentes
        lista[i], lista[i + 1] = lista[i + 1], lista[i] #aún faltan intercambios, solo mueve el primer elemento mayor detectado
print(lista)


        

numeros = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora, estamos fuera del bucle
    
    for i in range(len(numeros) - 1): #entramos a las evaluaciones de cada elemento
        if numeros[i] > numeros[i + 1]: #nos encontramos evaluando y se confirma la condición
            swapped = True  # entramos al bucle y se ejecuta la siguiente instrucción (es como "unir" esta condición con el while inicial para que el ciclo comience de nuevo, y en el inter, realizar el cambio de variables)
            numeros[i], numeros[i + 1] = numeros[i + 1],  numeros[i]

print(numeros)