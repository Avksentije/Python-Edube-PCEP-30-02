#Existe un método especial en Python el cual puede extender el alcance de una variable 
#incluyendo el cuerpo de las funciones 
#para poder no solo leer los valores de las variables sino también modificarlos.


# global name
# global name1, name2, ...

#Ejemplo 01:

def my_function():
   # global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)


#Ejemplo 02:

def my_function():
    global variable
    variable = 2
    print("¿Conozco a aquella variable?", variable)


variable = 1
my_function()
print(variable) #Se ha "sobre-escrito" dado que variable = 2 actúa ahora como global dentro y fuera de la función.


#Ejemplo 03:

global_var = 10

def modify_global_var():
    global global_var
    lst = []
    for i in range(0, 50, 5):
        global_var = i
        lst.append(global_var)
        print("Valores incrementales de global_var = ", lst)

print("Valor inicial de global_var:", global_var)
modify_global_var()
print("Valor modificado de global_var:", global_var)


#Ejemplo 03_modificado; no se imprime el tamaño de paso, sino la lista final:

global_variable = "TEXTO"

def modify_global_var():
    global global_variable #Al definir global, ocurre la sobre-escritura de la variable con el mismo nombre fuera de la función.
    lst_02 = []
    for i in range(3, 60, 3):
        global_variable = i
        lst_02.append(global_variable)
    if global_variable == 57:
        print("Valores incrementales de global_variable = ", lst_02)

print("Valor inicial de global_variable:", global_variable)
modify_global_var()
print("Valor modificado de global_variable:", global_variable)