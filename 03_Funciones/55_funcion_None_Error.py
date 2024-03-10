def strange_function(n):
    if(n % 2 == 0):
        return True

request = int(input("Ingresa un numero: "))

print(strange_function(request))


#Al imprimir en consola, aparece None
#Esto se debe a que en la función hay un ligero error, solamente se considera el resultado cuando es True
#Es decir, si False, la función no hace "nada" y al invocarla nos mostrará None puesto que no está programada para generar un resultado ante un False.