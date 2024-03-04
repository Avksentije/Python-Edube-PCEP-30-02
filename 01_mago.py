secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

número = int(input("\n...\nadivina el número: "))

while número != secret_number:
    print ("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    número = int(input("\n...\nintenta de nuevo: "))
if número == secret_number:
    print("¡Bien hecho, muggle! Eres libre ahora")
