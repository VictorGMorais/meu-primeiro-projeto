# Crie uma função chamada intersecao_listas(lista1, lista2) que recebe duas 
# listas e retorna uma lista com os elementos que aparecem em ambas.

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

def intersecao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))

print(intersecao_listas(l1,l2))