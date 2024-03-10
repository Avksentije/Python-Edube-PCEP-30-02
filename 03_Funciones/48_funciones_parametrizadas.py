#Un parámetro es una variable, con dos factores diferentes:
#a) Los parámetros solo existen dentro de las funciones en donde han sido definidos
#b) La asignación de un valor a un parámetro se hace en el momento en que la función se invoca, especificando el argumento correspondiente.

def mensaje(numero):
    print("El numero es:", numero)

numero_usuario = input("Ingresa un número: ")

mensaje(numero_usuario)