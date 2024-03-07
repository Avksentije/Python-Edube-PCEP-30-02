lista = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista:"))
    lista.append(val)

while swapped:
    swapped = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            swapped = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("\nOrdenada:")
print(lista)
