#Se busca una palabra clave (key) y se obtiene un valor de vuelta.

#Es decir, un diccionario es un conjunto de palabras claves y valores.

#1) Cada clave debe ser única, no es posible tener clave duplicada.
#2) Una clave puede ser un tipo de dato de cualquier tipo (enteros, flotantes, cadenas...)
#3) Un diccionario no es una lista, sino que almacena _pares de valores_
#4) La función len() aplica también para diccionarios, y regresa la cantidad de pares.
#5) Un diccionario es una herramienta de un solo sentido: clave----valor, mas no a la inversa.

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)