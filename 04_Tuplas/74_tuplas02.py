tupla_vacía = ()

print(tupla_vacía)

elemento_01 = (1,)
elemento_01_01 = 1.,

#Colocar la coma distingue al elemento de un valor entero ordinario,
#Esto permite interpretar ese valor como tupla, no como variable.

#Desempaquetar elementos:

tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

#Contador
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # salida: 4