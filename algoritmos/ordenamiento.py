"""Algoritmos de ordenamiento implementados desde cero (Hito 2)."""


def merge_sort(lista, clave=lambda x: x):
    """Ordena una lista de menor a mayor usando Mergesort.

    Retorna una lista nueva y no modifica la original. Es estable: si dos
    elementos tienen la misma clave, conservan su orden original.

    Complejidad: O(n log n) en el mejor, promedio y peor caso, ya que la
    lista siempre se divide por la mitad (log n niveles) y en cada nivel
    se recorren los n elementos al mezclar.

    Args:
        lista: elementos a ordenar.
        clave: función que, aplicada a cada elemento, entrega el valor por
            el que se ordena (por ejemplo, el costo operativo).

    Returns:
        Una lista nueva con los elementos ordenados.
    """
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
    """Combina dos listas ordenadas en una sola lista ordenada.

    Complejidad: O(n), con n = len(izquierda) + len(derecha).
    """
    resultado = []
    i = 0
    j = 0
    while i < len(izquierda) and j < len(derecha):
        # Con <= se mantiene la estabilidad: en un empate gana la izquierda
        if clave(izquierda[i]) <= clave(derecha[j]):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Una de las dos mitades se acabó: el resto de la otra ya está ordenado
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
