dictionary = {
    "orquidea" : "$400.00", 
    "albahaca" : "$35.00", 
    "salvia" : "$45.00"}

#Modificar un valor
dictionary['orquidea'] = 'Desc 15%, $340.00'
print(dictionary)

#Agregar un elemento
dictionary['magnolia (árbol chico)'] = '$1,700.00'
print(dictionary)

#Agregar un elemento mediante método .update()
dictionary.update({"cerezo (árbol 1 año)": "$1,850.00"})
print(dictionary)

#Eliminando una clave
del dictionary['cerezo (árbol 1 año)']
dictionary.update({"ciruelo (árbol 1 año)": "$1,850.00"})
print(dictionary)

#Eliminar el último elemento
dictionary.popitem()
print(dictionary)