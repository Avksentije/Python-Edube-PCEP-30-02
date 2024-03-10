def find_element_in_list(element, lst):
    if element in lst:
        return element
    else:
        return None

my_list = [1, 2, 3, 4, 5]
request = int(input("¿Qué número estás buscando? "))
result = find_element_in_list(request, my_list)

if result is None:
    print("El elemento no se encuentra en la lista")
else:
    print("El elemento se encuentra en la lista:", result)