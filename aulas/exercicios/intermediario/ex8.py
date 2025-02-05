# l1 = [45,56,73,68,43]
# l2 = [98,34,76,32,12]

# def soma_listas(l1,l2):
#     menor = min(len(l1),len(l2))
#     soma_tot = []
#     for i in range(menor):
#         soma_tot.append(l1[i]+l2[i])
#     return soma_tot

# print(soma_listas(l1,l2))

# def soma_list(l1,l2):
#     soma = [x + y for x, y in zip(l1,l2)]
#     return soma

# print(soma_list(l1,l2))
from itertools import groupby


alunos = [{'nome':'Victor','nota':'A'},
          {'nome':'Maya','nota':'A'},
          {'nome':'Thomsd','nota':'C'},
          {'nome':'Hugo','nota':'B'},
          {'nome':'Matheus','nota':'A'},
          {'nome':'Rodrigo','nota':'C'},
          {'nome':'Caio','nota':'B'},
          {'nome':'Hilda','nota':'C'}
]
# print(*alunos, sep='\n')
alunos_ordenados = sorted(alunos , key=lambda x: x['nota'])

grupos = groupby(alunos_ordenados, key=lambda x: x['nota'])

for k,v in grupos:
    print(k)
    print(list(v))
