

def my_function(my_list_1):
    print("Print #1:", my_list_1, hex(id(my_list_1)))
    print("Print #2:", my_list_2, hex(id(my_list_2)))
    del my_list_1[0]  # Se elimina elemento 0 de la lista, por lo tanto será solo [3]
    print("Print #3:", my_list_1, hex(id(my_list_1)))
    print("Print #4:", my_list_2, hex(id(my_list_2))) #Se pasa ahora la lista modificada, que corresponde a la misma posición en la memoria


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2, hex(id(my_list_2)))



#La razón por la que se modifica my_list_2 aunque sea una variable global es porque, en Python, las listas son mutables. 
#Al pasar una lista a una función y modificarla DENTRO de esa función, 
#se modifica la lista original, no una copia de ella. 
#Esto se debe a que las variables en Python son solo referencias a objetos en memoria, 
#y al pasar una lista como argumento a una función, se está pasando esa referencia.

#Entonces, al eliminar un elemento de my_list_1 dentro de la función my_function, 
#se modifica la lista original referenciada por my_list_2, 
#ya que ambas variables apuntan a la misma lista en la memoria.


