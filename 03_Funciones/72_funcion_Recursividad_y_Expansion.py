#La función fun(25) se expandiría de la siguiente manera:

#fun(25) se expande a 25 + fun(28)
#fun(28) se expande a 28 + fun(31)
#fun(31) devuelve 3 porque a > 30
#28 + 3 es igual a 31, por lo que fun(28) devuelve 31
#25 + 31 es igual a 56, por lo que fun(25) devuelve 56.


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))
