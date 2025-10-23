def sumar_elementos_recursivamente(elemento):
    suma_total = 0

    if isinstance(elemento, (int, float)):
        if elemento >= 0:
            return elemento
        else:
            return 0

    elif isinstance(elemento, list):

        if not elemento:
            return 0
        
        for valor in elemento:
            suma_total += sumar_elementos_recursivamente(valor)
        return suma_total

    else:
        return 0

lista_anidada = [
    [
        [1, 2.5, "primer nivel"],
        [3, [4, 5.5, "segundo nivel"], 6],
    ],
    [
        [7.7, 8, None],
        [[], 9, "lista vacía"]
    ],
    [
        ["texto", 10.1, 11],
        [12, [13, "último", 14.4], 15]
    ]
]

suma = sumar_elementos_recursivamente(lista_anidada)
print(suma)