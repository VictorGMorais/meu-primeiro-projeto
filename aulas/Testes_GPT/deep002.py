from itertools import combinations, permutations, product,groupby, combinations_with_replacement

def agrupando(lista,key):
    return sorted(lista, key=lambda x: x[key])

jogadores = ['Alice', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
grupos_de_3 = combinations(jogadores,3)
for trios in grupos_de_3:
    print(trios)
    
print('\n')

digitos = [1, 2, 3]
combinaçoes_senhas = permutations(digitos, 3)
for trios in combinaçoes_senhas:
    print(trios)
    
print('\n')

pratos = ['Pizza', 'Hambúrguer']
bebidas = ['Refrigerante', 'Suco']
sobremesas = ['Sorvete', 'Torta']
combinaçoes_combo = product(pratos,bebidas,sobremesas)
for combos in combinaçoes_combo:
    print(combos)
    
print('\n')

alunos = [
    {'nome': 'Alice', 'nota': 8},
    {'nome': 'Bruno', 'nota': 7},
    {'nome': 'Carlos', 'nota': 8},
    {'nome': 'Daniela', 'nota': 9},
    {'nome': 'Eduardo', 'nota': 7},
]
ordenando_por_nota = agrupando(alunos,'nota')
agrupar_por_nota = groupby(ordenando_por_nota, key=lambda x: x['nota'])

for k,v in agrupar_por_nota:
    print(f'notas {k}')
    for j in list(v):
        print(f' -{j['nome']}')
    print()

print('\n')

palavra = 'ABC'

combinaçoes = combinations(palavra,2)
for i in combinaçoes:
    print(i)

print('\n')

permutaçoes = permutations(palavra,2)
for i in permutaçoes:
    print(i)

print('\n')

numeros = [1, 1, 2, 2, 2, 3, 1, 1, 1, 4, 4]

organizando_numeros = sorted(numeros)
grupos_numeros = groupby(organizando_numeros)

for k, grupo in grupos_numeros:
    print(f'{k} : {list(grupo)}')

print('\n')

moedas = [1,2,5]

# for com in range(12,0,-1):
#     for i in list(combinations_with_replacement(moedas,com)):
#         if sum(i) == 10:
#             print(i)

for com in range(1, 11):
    for i in combinations_with_replacement(moedas, com):
        if sum(i) == 10:
            print(i)

print('\n')