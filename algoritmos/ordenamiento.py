

def merge_sort(lista, clave=lambda x: x):

    # Caso base: una lista de 0 o 1 elementos ya está ordenada
    if len(lista) <= 1:
        return list(lista)

    # Dividir: ordenar cada mitad por separado
    mitad = len(lista) // 2
    izquierda = merge_sort(lista[:mitad], clave)
    derecha = merge_sort(lista[mitad:], clave)

    # Mezclar: combinar las dos mitades ya ordenadas
    return _mezclar(izquierda, derecha, clave)


def _mezclar(izquierda, derecha, clave):
 
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        if clave(izquierda[i]) <= clave(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Una de las dos mitades se acabó
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
