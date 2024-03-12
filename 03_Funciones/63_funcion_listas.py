def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


var = 1
my_function(var) #En este punto, el valor que se asigne a "var" será el valor del argumento "n".
print(var)



def my_function(my_list_1):   #Argumento de entrada es my_list_2 [2, 3]
    print("Print #1:", my_list_1) #[2, 3], imprime el contenido de la varible my_list_1 (argumento), en este caso "ese contenido" es my_list_2 = [2, 3]
    print("Print #2:", my_list_2) #[2, 3], imprime directamente el contenido de la variable my_list_2
    my_list_1 = [0, 1] #creo una variable local dentro de la función
    print("Print #3:", my_list_1) #[0, 1], ahora, la variable local "oculta" a la variable my_list_1 que se había pasado como argumento de función, SIN CAMBIAR LA VARIABLE ORIGINAL my_list_1
    print("Print #4:", my_list_2) #[2, 3], hace referencia a la variable my_list_2 (mismo caso que Print#2)


my_list_2 = [2, 3] #esta variable se considera global por defecto
my_function(my_list_2)
print("Print #5:", my_list_2) #[2, 3] imprime directamente my_list_2 desde "fuera" de la función


