dictionary  = {
    "agua":"water", 
    "telefono":"33339292", 
    "mascota":"tortuga"  #aquí ya no lleva coma :))
    }

words = ["agua", "dirección", "clave"] #Por alguna razón esto me recuerda al modelo lógico relacional (hmmm)
#(Creamos una lista intermedia)

for word in words: #for element in list
    if word in dictionary: #if the element of the list in dictionary
        print(word, "....", dictionary[word]) #en este caso leemos el elemento del diccionario
    else:
        print(word, "no está en el diccionario")