user_word = input("¿Cuál es tu palabra favorita?")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.

        
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    
    else: 
        print(letter)
