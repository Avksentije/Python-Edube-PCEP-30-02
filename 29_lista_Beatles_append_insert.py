# Crea una lista vacia
Beatles = []
print("Paso 1:", Beatles)
a = str("John Lennon")
b = str("Paul McCartney")
c = str("George Harrison")
# Usa el método append() para agregar los nombres de los miembros de la banda
Beatles.append(a)
Beatles.append(b)
Beatles.append(c)
print("Paso 2:", Beatles)

# Bucle for y append para aladir los siguientes nombres:

for i in range(len(Beatles)):
   
    if i == 2:
        print("¿Olvidó Stu Sutcliffe (agrégelo)? ", end="")
        Beatles.append(input())
    
    if i == 2:
        print("¿Olvidó Pete Best(agrégelo)? ", end="")
        Beatles.append(input())
        
print("Paso 3:", Beatles)

# Eliminar Beatles
print("Se decidió mejor eliminarlos")
del Beatles[3]
del Beatles[3]
print("Paso 4:", Beatles)

# paso 5
print("Se agregará otro elemento")

Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))