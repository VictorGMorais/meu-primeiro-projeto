from functools import reduce
# produtos = [{'nome':'arroz', 'preco': 32.89},
#             {'nome':'feijao', 'preco': 6.78},
#             {'nome':'cafe', 'preco': 26.99},
#             {'nome':'açucar', 'preco': 5.89},
#             {'nome':'leite', 'preco': 5.78},
#             {'nome':'macarrao', 'preco': 3.99}]


# def aumentar_porcentagem(valor,porcentagem):
#     return round(valor + (valor * porcentagem / 100),2)

# prod_aumentados = [{**p, 'preco': aumentar_porcentagem(p['preco'],10)} for p in produtos]
# print(prod_aumentados)

# def atualiza_preco(prod):
#     return {**prod, 'preco': aumentar_porcentagem(prod['preco'],1)}

# novos_prod = list(map(atualiza_preco,produtos))

# for i in novos_prod:
#     print(i)
    

# num_x_5 = list(map(lambda x: x*5 , num))
# print(num_x_5)
# num = [{'n':'a','preco':123},
#        {'n':'b','preco':321},
#        {'n':'c','preco':132},
#        {'n':'d','preco':312},
#        {'n':'e','preco':231},
#        {'n':'f','preco':213},]

# novo_preco = reduce(lambda a,p: a +p['preco'], num, 0) 
# print(novo_preco)

def fat(n): #melhor nao usar funçoes recursivas
    if n <= 1:
        return 1
    return n * fat(n - 1)

print(fat(5))