my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list) #al elemento 2 no le pasa nada, se queda igual al estar en el centro



#Cuando la lista es grande:

my_list = [10, 1, 8, 3, 5, 12, 35, 17, 39, 22]
length = len(my_list)

for i in range(length // 2): 
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)