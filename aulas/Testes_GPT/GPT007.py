def diferenca_maxima(lista):
    if len(lista) < 2:
        return None
    return max(lista) - min(lista)

lis = [-5, -1, -10, 0]
print(diferenca_maxima(lis))

# bonus
from collections import Counter

def mais_frequente(lista):
    if not lista:
        return None
    a = Counter(lista)
    return a.most_common()[0][0]

lis = []
print(mais_frequente(lis)) 


        