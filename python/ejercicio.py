def indice_simpson(especies):
    suma = sum(especies)
    total = 0
    for cantidad in especies:
        total = total + pow(cantidad / suma, 2)
    return 1 - total


data = {
    'SHINTUYA': [300, 335, 365],
    'HUACYUMBRE': [20, 49, 931],
}

for i in data:
    print('El indice de simpson para la comunidad', i, 'es', indice_simpson(data[i]))

