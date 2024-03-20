# Sintaxis 1:
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Sintaxis 2:
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


# Sintaxis 3:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b # expresión universal


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))