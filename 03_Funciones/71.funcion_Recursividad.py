# La recursividad es una técnica donde una función se invoca a si misma.

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2) # :))

# Riesgo:
# Si no se considera una condición que detenga las invocaciones recursivas, el programa puede entrar en un bucle infinito

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))


#Se define la función fib(n) que calcula el n-ésimo término de la secuencia de Fibonacci.
#La función toma un argumento n, que representa el término de la secuencia que se desea calcular.
#Primero, se verifica si n es menor que 1. Si es así, la función devuelve None, ya que no hay términos de la secuencia de Fibonacci para valores de n menores que 1.
#Luego, se verifica si n es menor que 3. Si es así, la función devuelve 1, ya que los primeros dos términos de la secuencia de Fibonacci son 1.
#Si n es mayor o igual a 3, se inicializan las variables elem_1 y elem_2 con 1, ya que los primeros dos términos de la secuencia de Fibonacci son 1.
#Se inicializa the_sum como 0.
#Se realiza un bucle for desde i = 3 hasta n (inclusive). En cada iteración del bucle, se calcula the_sum sumando los valores de elem_1 y elem_2. Luego, se actualizan los valores de elem_1 y elem_2 para la próxima iteración.
#Después de completar el bucle, se devuelve the_sum, que es el n-ésimo término de la secuencia de Fibonacci.
#En el bucle for final, se prueba la función fib(n) para n en el rango de 1 a 9, y se imprime el resultado junto con el valor de n.
#En resumen, la función fib(n) calcula el n-ésimo término de la secuencia de Fibonacci utilizando un bucle for y devuelve el resultado. Luego, se prueba esta función para varios valores de n en el rango de 1 a 9.