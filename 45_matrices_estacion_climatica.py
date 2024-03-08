#Edube:

#Crea una matriz de 1 medición por hora, durante un mes completo

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

highest = -100.0 #Primer temperatura de comparación

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)