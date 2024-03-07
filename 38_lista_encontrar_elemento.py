#Encontrar la ubcación de un elemento dado dentro de una lista

lista = ["agua", "peces", "pulpo", "anémona", "lirios", "hojas"]
encontrar = "lirios"
found = False #Inicia el ciclo

for i in range(len(lista)):
    found = lista [i] == encontrar #Si se cumple la comparación, found cambia su valor a True
    if found: #If evalúa una expresión y ejecuta elbloque de código dentro del if, si la expresión se evalúa como true. Si "False", el bloque no se ejecuta.
        break #En este caso, si "True", se ejecuta el break
              #En este punto, found ya tiene un valor de "True", lo cual indica que se encontró el elemento
    
if found: #Por lo tanto, al verificar el valor de found ("True"), podemos emplearlo en líneas fuera del bucle
    print("Elemento encontrado en el índice", i)
else:
    print("Ausente")