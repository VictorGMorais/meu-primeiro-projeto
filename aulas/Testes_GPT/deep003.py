# #1.  Criar um dicionário que conte a frequência de cada elemento em uma lista.

# frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"] # cria a lista a ser contada
# cesta = {} # cria o dict que recebera as frutas e o numero referente a quantidade

# for qnt_fruta in frutas: # percorre fruta a fruta da lista
#         cesta[qnt_fruta] = cesta.get(qnt_fruta, 0) + 1 # se nao tiver, cria a fruta na cesta com 1 unidade.add()
        
# for k,v in cesta.items(): # percorre chave e valor da cesta
#     print(f'tem {v} {k} na cesta') #imprime os dados percorridos
    
# #2. Escreva uma função que combine dois dicionários, 
# # somando os valores das chaves que existem em ambos.
# print('\n')   
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 15, 'd': 25}

# def somar_dict(d1,d2):
#     soma_dos_dicts = {} #criando a lista que vai receber a soma das listas
#     soma_dos_dicts = d1.copy() #faz uma copia rasa da primeira lista
#     for i in d2: # percorre key por key do segundo dicionario
#         if i in soma_dos_dicts: #verifica se key conta no dict 1 copiado
#             soma_dos_dicts[i] += d2[i] #se sim, soma os valores da mesma key
#         else:
#             soma_dos_dicts[i] = d2[i] # se nao, adiciona a key no dict1 copiado
#     return soma_dos_dicts #retorna o dict final ja com toda a soma

# print(somar_dict(dict1,dict2)) # chama a funçao com dois dict e ja imprime o dict somado
# print('\n')   

# #3. Dada uma lista de dicionários com alunos e suas notas, 
# # calcule a média de cada aluno e retorne um novo dicionário com o nome e a média.

# alunos = [
#     {'nome': 'João', 'notas': [7, 8, 9]},
#     {'nome': 'Maria', 'notas': [6, 7, 8]},
#     {'nome': 'Pedro', 'notas': [5, 6, 7]}
# ]

# media_alunos = {}

# for nota in alunos:
#     media_alunos[nota['nome']] = sum(nota['notas']) / len(nota['notas'])
 
# print(media_alunos)

# med_alunos = {x['nome']: sum(x['notas']) / len(x['notas']) for x in alunos} 

# print(med_alunos)
# print('\n')   
# print('\n')   

# #bonus. 

dicionario = {'first name': 'victor', 'mid name': 'gomes', 'last name': 'morais'}
def invertendo_key_value(dic):
    invert = {}
    for k,v in dicionario.items():
        invert[v] = k
    return invert

print(invertendo_key_value(dicionario))
    
