# A una clave, un valor:
my_dictionary = {
    "key1": "value1",
    "key2": "value2"
    }

#Si se desea acceder a un elemento del diccionario
#se puede referir su clave colocándola dentro de corchetes, o usando el método get()
pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }

item_1 = pol_esp_dictionary["gleba"]    # Ejemplo 1.
print(item_1)    # salida: tierra

item_2 = pol_esp_dictionary.get("woda")    # Ejemplo 2.
print(item_2)    # salida: agua


#Cambiar el valor asociado a una clave específica
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]    
print(item)  # salida: cerradura

#Modificar el contenido eliminando o agregando elementos; métodos update(), popitem():
phonebook = {}    # un diccionario vacío

phonebook["Tania"] = 3456782343   # crear/agregar un par clave-valor
print(phonebook)    # salida: {'Tania': 3456783958}

phonebook.update({"Tania casa": 23423492394 })
print(phonebook)

del phonebook["Tania"]
print(phonebook)    # salida: {}

phonebook.update({"Tania cel": 55434522394 })
print(phonebook)

phonebook.popitem()
print("Directorio telefónico final:", phonebook)


#Iterar empleando el bucle for
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

for item in pol_esp_dictionary:
    print(item) 

#Examinar los elementos clave-valor, por método items()
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

for key, value in pol_esp_dictionary.items():
    print("Pol/Esp ->", key, ":", value)


#Palabra reservada in, para comprobar si una clave existe en el diccionario:
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in pol_esp_dictionary: #medium :)
    print("Si")
else:
    print("No")
    




