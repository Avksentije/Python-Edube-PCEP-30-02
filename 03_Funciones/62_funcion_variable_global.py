#Existe un método especial en Python el cual puede extender el alcance de una variable 
#incluyendo el cuerpo de las funciones 
#para poder no solo leer los valores de las variables sino también modificarlos.


# global name
# global name1, name2, ...


def my_function():
   # global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)



def my_function():
    global variable
    variable = 2
    print("¿Conozco a aquella variable?", variable)


variable = 1
my_function()
print(variable) #Se ha "sobre-escrito" dado que variable = 2 actúa ahora como global dentro y fuera de la función.