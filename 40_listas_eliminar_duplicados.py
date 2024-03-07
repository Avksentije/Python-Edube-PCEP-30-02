lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_02 = []

for elemento in lista:
    if elemento not in lista_02:
        lista_02.append(elemento)
        
print("La lista con elementos únicos:")
print(lista_02)