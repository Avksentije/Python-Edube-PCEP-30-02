my_tuple = (1, 10, 100, 1000)

#Las tuplas y listas tienen similitudes, como la lectura de los elementos:
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
    

#Sin embargo, al tratar la tupla con instrucciones de lista, se generan errores de ejecución:
my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10

#Otras propiedades de las tuplas
#Indexación:
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(my_tuple[3])    # salida: [3, 4]

#Inmutabilidad
my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
my_tuple[2] = "guitarra"    # La excepción TypeError será lanzada.

#Eliminar una tupla completa
my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined

#Crear tuplas completas con la función integrada de Python tuple()
my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # salida: [2, 4, 6]
print(type(my_list))    # salida: <class 'list'>

tup = tuple(my_list)
print(tup)    # salida: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'> #acá convertimos una lista en una tupla :))

tup = 1, 2, 3, 
my_list = list(tup)
print(type(my_list))    # salida: <class 'list'> #y acá lo hicimos a la inversa :))