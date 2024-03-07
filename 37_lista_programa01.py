lista = [17, 3, 11, 5, 1, 9, 75, 15, 13]
largest = lista[0]

for i in range(1, len(lista)):
    if lista[i] > largest: #compara el elemento actual con el elemento de referencia
        largest = lista[i] #si la comparación es True (el elemento actul es mayor que "largest", ahora lista[i] actual se convierte en el "largest")

print(largest)


#Otra manera de escribilo es:
lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = lista[0]

for i in lista[1:]: #Recorre todos los elementos a partir de lista[1]
    if i > largest: #Comparación entre el elemeto "i" actual y el valor de "largest"
        largest = i #Si la comparación es True, ahora "largest" se iguala con "i" actual

print(largest)

