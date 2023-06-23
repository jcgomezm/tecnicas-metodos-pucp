def sumar(x, y):
    return x + y


print(sumar(2, 3))
# 5


def es_bisiesto(anio):
    if (anio % 400 == 0) and (anio % 100 == 0):
        return True
    elif (anio % 4 == 0) and (anio % 100 != 0):
        return True
    else:
        return False


print(es_bisiesto(2024))
# True


