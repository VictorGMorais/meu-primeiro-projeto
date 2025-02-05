# aumente o preço dos produtos a seguir em 10% e gere novos produtos por deep copy.
# crie outra lista por deep copy e ordene a lista produtos em ordem crescente.
# crie outra lista por deep copy e ordene a lista preco em ordem descrescente.

def tabela(lista):
    for i in lista:
        print(f"Produto: {i['nome']:<8} Preço: {i['preco']:>4}")
    print()

import copy
produtos = [
    {'nome': 'livro', 'preco': 23.99},
    {'nome': 'mochila', 'preco': 56.99},
    {'nome': 'relogio', 'preco': 86.99},
    {'nome': 'fone', 'preco': 68.99},
    {'nome': 'lampada', 'preco': 19.99}
]
novos_produtos = copy.deepcopy(produtos)
produtos_por_nome = sorted(copy.deepcopy(produtos), key=lambda k: k['nome'])  
produtos_por_preco = sorted(copy.deepcopy(produtos),key=lambda k: k ['preco'],reverse=True) 

for i in novos_produtos:
    i['preco'] = round( i['preco'] * 1.10 , 2)
    
# produtos[0] = {'nome': 'lapis', 'preco': 66.66} #teste para ver se a cópia é profunda
print('Lista Original')
tabela(produtos)

print('Lista aumento de 10% no preço')
tabela(novos_produtos)

print('Lista ordenada por nome')
tabela(produtos_por_nome)

print('Lista ordenada por preço')
tabela(produtos_por_preco)   




