# def segunda_maior(notas):
#     nota = list(set(notas))
#     if len(nota) < 2:
#         return None
#     return sorted(nota)[-2]

# print(segunda_maior([12, 23, 46, 7, 12, 23, 67, 7, 34]))


def produto_maximo(lista):
    if len(lista) < 2:
        return None
    maior_prod = lista[0] * lista[1]
    for num in range(len(lista)):
        for j in range(num + 1, len(lista)):
            prod = lista[num] * lista[j]
            if prod > maior_prod:
                maior_prod = prod
    return maior_prod
            
            
print(produto_maximo([-10, -3, -5, 6, -2]))

# def produto_maximo(lista):
#     maior_prod = 0
#     if len(lista) < 2:
#         return None
#     for i in lista:
#         for j in lista:
#             if lista.index(j) == lista.index(i):
#                 continue
#             if not maior_prod:
#                 maior_prod = i * j
#             elif (i * j) > maior_prod:
#                 maior_prod = i * j
#     return maior_prod
            
            
# print(produto_maximo([-10, -10, -5, 6, -2]))