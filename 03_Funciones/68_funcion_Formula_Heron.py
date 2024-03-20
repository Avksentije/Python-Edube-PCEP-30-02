def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))

#Un triángulo rectángulo la mitad de un cuadrado y con un lado igual a 1. 
#Esto significa que su área debe ser igual a 0.5.

#En consola aparece 0.49999999999983, debido a los cálculos de valores punto flotantes.