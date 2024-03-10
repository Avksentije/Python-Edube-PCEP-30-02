#return sin una expresión

#"transporta" el valor de la expresión al lugar donde se invoca la función

def funcion_expresion():
    return 123

x = funcion_expresion()

print("La función ha devuelto su resultado. Es:", x)

#La expresión del return también puede ser pasado por alto
def funcion_expresion():
    print("Saltando el return")
    return 123

print("Omitiendo el resultado...")
funcion_expresion()
print("Se ha saltado")


