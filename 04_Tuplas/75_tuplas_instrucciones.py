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