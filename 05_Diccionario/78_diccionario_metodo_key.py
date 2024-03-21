#Esta parte de acá es interesante:

#Un diccionario no es un tipo de dato secuencial, el bucle for no es útil aquí.
# Sin embargo, se puede adaptar a los requerimientos del bucle

#Se construye un enlace intermedio entre el diccionario y una entidad secuencial _temporal_




#Método 1 - Método keys()
# Es parte de todo diccionario. Retorna o regresa una lista de todas las claves dentro del diccionario.
# Al tener una lista de claves, se puede acceder a todo el diccionario de una manera fácil y útil:

dictionary  = {
    "agua":"water", 
    "telefono":"33339292", 
    "mascota":"tortuga"  
    }

for key in dictionary.keys():  #acá ya podemos usar el for, empleando el método keys()
    print(key, "->", dictionary[key])