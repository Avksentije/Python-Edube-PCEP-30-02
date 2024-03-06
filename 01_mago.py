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

número_visualaaaa = int(input("\n...\nadivina el número: ")) #VOY A HACER UN CAMBIO AQUI

while número_visual != secret_number:
    print ("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    número_visual = int(input("\n...\nintenta de nuevo: "))
if número_visual == secret_number:
    print("¡Bien hecho, muggle! Eres libre ahora")
