year = int(input("Ingrese un año:"))
month = int(input("Ingrese un mes (1, 2, 3, etc.): "))
day = int(input("Ingrese un día: "))


def days_in_month(year, month):
    if month < 1 or month > 12 or year < 0:
        return None
    if month == 2:
        if year % 4 == 0: #Realizamos el ajuste de días a febrero en caso de que sea año bisiesto
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def day_of_year(year, month, day):
    total_days = day
    for month_user in range (1, month): #Establecemos una sumatoria desde el mes 1, hasta un mes antes del mes que ingresa el usuario.
        total_days += days_in_month(year, month_user) #Por cada mes, se llama a la función "days_in_month" para obtener el número de días de ese mes, y adicionamos la suma al valor inicial de días definidos por el usuario.  
    return total_days

def aviso_bisiesto(year):
    if year % 4 == 0: #Realizamos el ajuste de días a febrero en caso de que sea año bisiesto
        return "Es año bisiesto"
    else:
        return "No es año bisiesto"

print(day_of_year(year, month, day), "días ", aviso_bisiesto(year), sep = "----") #Llamamos a la función, para que nos muestre el resultado (return)

