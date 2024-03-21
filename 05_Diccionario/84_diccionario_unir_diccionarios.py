d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for elementos in (d1, d2):
    d3.update(elementos)

print(d3)


#Convertir una tupla de tuplas en diccionario, usando el método dict(tupla):
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

#Copia de un diccionario usando el método copy():
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)

#Imprimir items:
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)